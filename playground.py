from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.openai import OpenAITools
import openai
import phi.api
import os
import phi
from phi.playground import Playground, serve_playground_app
from dotenv import load_dotenv

#load environment variables from .env file
load_dotenv()

phi.api.api_key = os.getenv("PHI_API_KEY")


# Create a simple finance agent
finance_agent = Agent(
    name="Finance AI Agent",
    model=Groq(api_key=os.getenv("GROQ_API_KEY"), id="llama3-70b-8192"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True, company_news=True)],
    instructions=["Use tables to display the data"],
    show_tools_calls=True,
    markdown=True,
)

# Run the agent
finance_agent.print_response("Summarize analyst recommendation and share the latest news for NVDA", stream=True)


app = Playground(agents=[finance_agent]).get_app()

if __name__ == "__main__":
    serve_playground_app("playground:app", reload=True)