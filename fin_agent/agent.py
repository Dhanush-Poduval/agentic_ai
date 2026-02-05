from dotenv import load_dotenv
import os
from /home/dhanush/Desktop/agentic_ai/invesment_plan/agent.py import investment_agent
load_dotenv()
from google.adk.agents import LlmAgent
finance_agent=LlmAgent(
     name='finance_agent_analyser',
     description="Helps user with finance related questions",
     model='gemini-2.5-flash',
     instruction='''1)Take the finance query from the user
     2)Answer the quiestion with required  answer 
     '''

    )
root_agent=finance_agent
