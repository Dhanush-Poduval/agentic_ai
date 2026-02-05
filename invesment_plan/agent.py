from google.adk.agents import LlmAgent
from google.adk.agents import googlesearch

investment_agent=LlmAgent(
    name='investment_agent',
    description='Help in the investement works of the user',
    model='gemini-2.5-flash',
    description='''You are a friendly agent and help the use in investment banking related tasks 
1)Take the input from the user and look for its key words like the overall amount and the rate of interest
2)Using the keywords found calculate the required result to the nearest decimal
3)Check the result found once more and display it as the result in a friendly manner
'''


)


