from dotenv import load_dotenv
import os
load_dotenv()

from fin_agent.agent import finance_agent
from google.adk.agents import LlmAgent
from google.adk.tools import google_search
investment_agent=LlmAgent(
    name='investment_agent',
    description='Help in the investement works of the user',
    model='gemini-2.5-flash',
    instruction='''You are a friendly agent and help the use in investment banking related tasks 
1)Take the input from the user and look for its key words like the overall amount and the rate of interest
2)Using the keywords found calculate the required result to the nearest decimal
3)Check the result found once more and display it as the result in a friendly manner
''',
tools=[google_search],
sub_agents=[finance_agent],

)
root_agent=investment_agent


