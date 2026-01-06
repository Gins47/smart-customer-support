
from agents import Agent, Runner, function_tool
from pydantic import BaseModel
import uuid
from app.rag.car_manual import CAR_MANUAL_CHUNKS


def normalize(text: str) -> str:
    return text.lower().replace("’", "'")

@function_tool
def check_car_manual(query:str) -> str:
    """
    Searches the car manual text chunks for the query.
    Returns the most relevant chunk as a response.
    """
    query = normalize(query)
    relevant = ""
    for chunk in CAR_MANUAL_CHUNKS:
        chunk_text = normalize(chunk)
        if any(word in chunk_text for word in query.split()):
            return f"""Issue found in car manual : {chunk}"""
    print(f"check_car_manual relevant = {relevant} ")
    return relevant or "Sorry, I could not find the information in the manual."

@function_tool
def create_ticket_number(prefix:str = "TKT") -> str:
    """
    Generates human readable ticker number
    """
    return f"{prefix}-{uuid.uuid4().hex[:8].upper()}"


car_expert_agent = Agent(name="car expert",
                         instructions=""" Your are an car expert agent. 
                         1. Don't make any assumptions
                         2. Use the tool check_car_manual to get the answer for the car query
                         3. Based on the result returned by the tool, formulate the answer in a user understandable manner by only referring to data obtained from the tool
                         4. Don't ask for more details or provide suggestions which are not obtained from the tool
                         5. If you see the issue cannot be fixed by the user themselves ask the user to bring car to the nears authorized dealer for inspection.
                         6. If tool returns "Sorry, I could not find the information in the manual." as the response, inform user that "requested information is not found" and don't respond any assumptions.
                         If the customer asks a question that is not related to the car, transfer back. 
                         
                         """,
                         model="gpt-5-nano", 
                         tools=[check_car_manual]
                        )

class EmailAnalyzerOutput(BaseModel):
    priority:str
    summary:str

email_analyzer_agent = Agent(name="email analyzer agent", 
                             instructions="""
                            You are an email analyzer agent. 
                            1. Review the provided email body.
                            2. If the email contains no customer complaints or requests, set priority = INVALID.
                            3. Otherwise, classify priority as LOW, MEDIUM, HIGH, or CRITICAL.
                            4. Provide a one-sentence summary of the email.
                            5. Output must match EmailAnalyzerOutput: {priority, summary}. 
                            """,
                            model="gpt-5-nano", 
                            output_type=EmailAnalyzerOutput 
                            )

class OrchestratorAgentOutput(BaseModel):
    priority:str
    summary:str
    draft_response: str
    subject: str
    ticket_number: str

orchestrator_agent = Agent(name="orchestrator agent",
                           instructions=""" 
                            You are a customer care car support orchestrator.
                            Process:
                            1. Use email_analyzer to classify priority and summarize.
                            2. If priority == INVALID:
                            - Create a polite rejection response
                            - Do NOT create a ticket
                            3. If priority != INVALID:
                            - Generate a ticket number
                            - Determine if the request is about car operation, maintenance, or faults
                            - ONLY IF it is car-related, call car_expert
                            4. Use car_expert output strictly; do not add assumptions
                            5. Produce a draft email response and subject

                            Output MUST match OrchestratorAgentOutput. 
                           """, 
                           model="gpt-5-nano",
                           tools=[    
                            create_ticket_number,     
                            email_analyzer_agent.as_tool(
                                tool_name="email_analyzer",
                                tool_description="Perform analysis of the email and provide a brief summary and priority of the email",
                            ),         
                            car_expert_agent.as_tool(
                                tool_name="car_expert",
                                tool_description="Provides correct answers regarding the car by referring the car documentation",
                            ),
                           ],
                           output_type=OrchestratorAgentOutput
                           )



async def run_orchestrator_agent(email_text:str) -> OrchestratorAgentOutput:
    result = await Runner.run(orchestrator_agent, email_text)
    return result.final_output