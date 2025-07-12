from crewai import Task
from tools import search_tool, calculator_tool
from agents import financial_health_analyzer, document_reviewer, recommendation_engine

financial_analysis_task = Task(
    description="Analyze creditworthiness of {business_type} business: ${annual_revenue} revenue, ${monthly_cash_flow} monthly cash flow, ${current_debt} debt, FICO {credit_score_range}, PayNet {paynet_score}, {years_in_business} years old. Research industry risk factors and credit benchmarks.",
    expected_output="Comprehensive creditworthiness analysis with industry risk assessment, FICO/PayNet score evaluation, debt ratios, and cash flow assessment compared to industry standards.",
    tools=[search_tool, calculator_tool],
    agent=financial_health_analyzer
)

document_requirements_task = Task(
    description="Research lending requirements for {business_type} industry seeking ${loan_amount_needed} loan for {loan_purpose}. Consider FICO {credit_score_range}, PayNet {paynet_score}, and {bank_statements_available} availability. Find credit thresholds and industry-specific criteria.",
    expected_output="Detailed lending requirements including credit score thresholds, required documents, PayNet score expectations, bank statement requirements, and industry-specific lending criteria.",
    tools=[search_tool],
    agent=document_reviewer
)

loan_readiness_task = Task(
    description="Generate comprehensive loan readiness score (0-100) considering FICO score, PayNet score, industry risk, financial health, and document availability. Provide specific improvement recommendations for each factor.",
    expected_output="Complete loan readiness report with weighted score considering all creditworthiness factors: FICO, PayNet, industry risk, financial ratios, and document readiness, plus prioritized improvement action plan.",
    tools=[search_tool, calculator_tool],
    agent=recommendation_engine,
    output_file='loan_readiness_report.md'
)