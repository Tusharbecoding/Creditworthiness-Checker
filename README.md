# 🏦 AI-Powered Creditworthiness Checker

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![CrewAI](https://img.shields.io/badge/CrewAI-Enabled-green.svg)](https://crewai.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> **Intelligent Business Credit Assessment Tool** - Leverage AI agents to analyze small business creditworthiness, FICO scores, PayNet ratings, and loan readiness with industry-specific insights.

## 🚀 Overview

The **Creditworthiness Checker** is an advanced AI-powered system that helps small businesses assess their loan readiness and creditworthiness. Using a multi-agent architecture built with CrewAI, it provides comprehensive financial analysis, document requirement assessment, and actionable recommendations for improving loan approval odds.

### 🎯 Key Features

- **🤖 AI-Powered Analysis**: Three specialized AI agents working collaboratively
- **📊 FICO & PayNet Integration**: Comprehensive credit score evaluation
- **🏭 Industry-Specific Assessment**: Tailored analysis for different business types
- **📋 Document Readiness Check**: Lending requirement verification
- **🎯 Loan Readiness Score**: 0-100 weighted scoring system
- **📈 Actionable Recommendations**: Prioritized improvement strategies
- **🔍 Real-time Market Research**: Live industry benchmarking

## 🏗️ Architecture

### AI Agents

1. **Financial Health Analyzer** 💰

   - Analyzes revenue, cash flow, and debt ratios
   - Evaluates FICO and PayNet scores
   - Performs industry-specific benchmarking
   - Calculates financial health metrics

2. **Document Reviewer** 📄

   - Researches lending requirements by industry
   - Validates credit score thresholds
   - Checks bank statement availability
   - Identifies missing documentation

3. **Recommendation Engine** 🎯
   - Generates comprehensive loan readiness score
   - Provides weighted assessment across all factors
   - Creates prioritized action plans
   - Outputs detailed improvement strategies

### Technology Stack

- **🐍 Python 3.8+**: Core programming language
- **🤖 CrewAI**: Multi-agent AI framework
- **🔍 Serper API**: Real-time web search capabilities
- **🧠 Google Gemini**: Advanced language model
- **📊 Custom Tools**: Financial calculators and analyzers

## 🛠️ Installation

### Prerequisites

- Python 3.8 or higher
- Google AI API key
- Serper API key for web searches

### Quick Start

1. **Clone the repository**

   ```bash
   git clone git@github.com:Tusharbecoding/Creditworthiness-Checker.git
   cd creditworthiness-checker
   ```

2. **Create virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**

   ```bash
   # Create .env file
   touch .env

   # Add your API keys
   echo "GOOGLE_API_KEY=your_google_api_key_here" >> .env
   echo "SERPER_API_KEY=your_serper_api_key_here" >> .env
   ```

5. **Run the assessment**
   ```bash
   python crew.py
   ```

## 📊 Usage

### Input Parameters

Configure your business data in `crew.py`:

```python
business_data = {
    'business_type': 'Restaurant',           # Industry type
    'annual_revenue': '450000',              # Annual revenue ($)
    'monthly_cash_flow': '8000',             # Monthly cash flow ($)
    'years_in_business': '3',                # Years in operation
    'current_debt': '45000',                 # Current debt ($)
    'credit_score_range': '700',             # FICO score
    'paynet_score': '75',                    # PayNet commercial score
    'bank_statements_available': '3 years',  # Bank statement history
    'business_structure': 'LLC',             # Legal structure
    'loan_amount_needed': '50000',           # Requested loan amount ($)
    'loan_purpose': 'Equipment purchase'     # Purpose of loan
}
```

### Output

The system generates a comprehensive `loan_readiness_report.md` containing:

- **Credit Score Analysis**: FICO and PayNet evaluation
- **Financial Health Assessment**: Revenue, cash flow, and debt analysis
- **Industry Risk Evaluation**: Sector-specific risk factors
- **Document Readiness Check**: Required documentation status
- **Loan Readiness Score**: 0-100 weighted assessment
- **Improvement Recommendations**: Prioritized action items

## 🔧 Configuration

### Supported Business Types

- Restaurants & Food Service
- Retail & E-commerce
- Professional Services
- Manufacturing
- Healthcare
- Technology
- Construction
- And more...

### Credit Score Ranges

- **FICO Scores**: 300-850 (Personal credit)
- **PayNet Scores**: 1-100 (Commercial credit)
- **Industry Benchmarks**: Automatically researched

### Customization

Modify agent behaviors in `agents.py`:

- Adjust LLM temperature for creativity vs. precision
- Customize agent roles and backstories
- Add industry-specific tools and knowledge

## 📈 Key Metrics Analyzed

### Financial Health Indicators

- **Debt-to-Income Ratio**: Current debt vs. annual revenue
- **Cash Flow Stability**: Monthly cash flow consistency
- **Revenue Growth**: Year-over-year growth trends
- **Profitability Margins**: Industry-specific benchmarks

### Credit Assessment Factors

- **FICO Score Impact**: Personal credit history weight
- **PayNet Score Significance**: Commercial credit behavior
- **Industry Risk Profile**: Sector-specific default rates
- **Business Age Factor**: Operational history consideration

### Document Readiness Score

- **Bank Statements**: Availability and duration
- **Tax Returns**: Business and personal filings
- **Financial Statements**: P&L, balance sheets
- **Legal Documents**: Business registration, licenses

## 🚨 Troubleshooting

### Common Issues

1. **API Rate Limits**

   - Adjust `max_rpm` in crew configuration
   - Implement retry logic for failed requests

2. **Model Overload (503 Error)**

   - Switch to alternative LLM models
   - Implement exponential backoff
   - Consider using different API endpoints

3. **Missing Environment Variables**
   - Verify `.env` file exists and contains required keys
   - Check API key validity and permissions

## 🤝 Contributing

We welcome contributions!

### Development Setup

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

---

**⭐ Star this repository if you find it helpful!**

_Built with ❤️ for the small business community_
