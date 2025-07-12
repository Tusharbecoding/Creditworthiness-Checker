from crewai import Crew, Process
from agents import financial_health_analyzer, document_reviewer, recommendation_engine, llm
from tasks import financial_analysis_task, document_requirements_task, loan_readiness_task

crew = Crew(
    agents=[financial_health_analyzer, document_reviewer, recommendation_engine],
    tasks=[financial_analysis_task, document_requirements_task, loan_readiness_task],
    process=Process.sequential,
    memory=False,
    cache=True,
    max_rpm=100,
    share_crew=True,
    manager_llm=llm
)

business_data = {
    'business_type': 'Adult Entertainment',
    'annual_revenue': '450000',
    'monthly_cash_flow': '8000',
    'years_in_business': '3',
    'current_debt': '45000',
    'credit_score_range': '700',
    'paynet_score': '75',                   
    'bank_statements_available': '3 years', 
    'business_structure': 'S-Corp',
    'loan_amount_needed': '50000',
    'loan_purpose': 'Equipment purchase'
}

result = crew.kickoff(inputs=business_data)
print(result)