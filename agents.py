from crewai import Agent, LLM
from tools import search_tool, calculator_tool
import os
from dotenv import load_dotenv

load_dotenv()

llm = LLM(
    model="gemini/gemini-2.0-flash-exp",
    temperature=0.4,
    max_retries=5,
    timeout=60,
    base_delay=2,
    max_delay=30,
    exponential_base=2,
    jitter=True
)

financial_health_analyzer = Agent(
    role="Financial Health Analyzer",
    goal="Analyze business metrics for {business_type} industry: revenue ${annual_revenue}, cash flow ${monthly_cash_flow}, debt ${current_debt}, FICO {credit_score_range}, PayNet {paynet_score}",
    verbose=True,
    memory=False,
    backstory="You are a financial analyst specializing in small business creditworthiness assessment, FICO scores, PayNet commercial credit scores, and industry-specific benchmarking.",
    tools=[search_tool, calculator_tool],
    allow_delegation=True,
    llm=llm
)

document_reviewer = Agent(
    role="Document Reviewer",
    goal="Research lending requirements for {business_type} industry seeking ${loan_amount_needed} loan with FICO {credit_score_range}, PayNet {paynet_score}, and {bank_statements_available} bank statements",
    verbose=True,
    memory=False,
    backstory="You are a lending specialist who knows document requirements, credit score thresholds, and industry-specific lending criteria for different business types.",
    tools=[search_tool],
    allow_delegation=False,
    llm=llm
)

recommendation_engine = Agent(
    role="Loan Readiness Recommendation Engine",
    goal="Generate comprehensive loan readiness score considering FICO, PayNet, industry risk, and document availability for {business_type} business",
    verbose=True,
    memory=False,
    backstory="You are a business advisor who specializes in creditworthiness assessment, understanding how FICO scores, PayNet scores, industry risk factors, and document readiness affect loan approval odds.",
    tools=[search_tool, calculator_tool],
    allow_delegation=False,
    llm=llm
)