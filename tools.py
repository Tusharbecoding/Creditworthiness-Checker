from crewai_tools import SerperDevTool
from crewai.tools import tool
import os
from dotenv import load_dotenv

load_dotenv()

search_tool = SerperDevTool(
    api_key=os.getenv('SERPER_API_KEY')
)

@tool("Financial Calculator")
def calculator_tool(expression: str) -> str:
    """Calculate financial ratios and percentages. Input should be a mathematical expression like '45000/450000*100' for debt-to-income ratio."""
    try:
        result = eval(expression)
        return f"Calculation result: {result:.2f}"
    except:
        return "Invalid calculation. Use format like: 45000/450000*100"