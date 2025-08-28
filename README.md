# Finance Crew AI 🏦

A sophisticated AI-powered financial analysis system built with CrewAI that provides comprehensive financial services through specialized AI agents. This system leverages multiple AI agents working together to deliver professional-grade financial analysis, risk assessment, budget planning, and investment advisory services.

## 🚀 Features

### Core Services
- **Company Financial Analysis**: Comprehensive analysis of financial statements, ratios, and market trends
- **Personal Financial Planning**: Custom budget creation, expense tracking, and financial goal planning
- **Investment Analysis**: Portfolio analysis, risk assessment, and investment recommendations
- **Risk Assessment**: Quantitative risk evaluation with VaR calculations and stress testing

### AI Agents
- **Financial Analyst**: Analyzes financial data, calculates key ratios, and provides investment insights
- **Risk Assessment Specialist**: Evaluates investment risks and provides mitigation strategies
- **Budget Planning Advisor**: Creates budgets and provides financial planning guidance
- **Investment Advisor**: Delivers investment recommendations and portfolio optimization

## 📋 Requirements

- Python 3.8+
- OpenAI API key
- Required Python packages (see requirements.txt)

## 🛠 Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd CrewAgents
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   Create a `.env` file in the project root:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```

4. **Get your OpenAI API key**
   - Visit [OpenAI API Keys](https://platform.openai.com/api-keys)
   - Create a new API key
   - Add it to your `.env` file

## 🚀 Usage

### Quick Start
```bash
python main.py
```

### Demo Mode
```bash
python demo.py
```

### Interactive Menu Options

1. **Company Financial Analysis**
   - Input: Company name (e.g., "Apple Inc.")
   - Output: Comprehensive financial health report with ratios, trends, and recommendations

2. **Personal Financial Planning**
   - Input: Age, income, savings, financial goals
   - Output: Custom budget plan with savings strategies and timelines

3. **Investment Analysis**
   - Input: Investment details (stocks, bonds, portfolio)
   - Output: Risk analysis, diversification recommendations, and optimization strategies

## 💡 Usage Examples

### Company Analysis
```python
from main import FinanceCrew

crew = FinanceCrew()
result = crew.run_financial_analysis("Microsoft")
```

### Personal Finance Planning
```python
client_profile = "Age: 35, Income: $90,000, Savings: $50,000, Goals: Retirement planning"
result = crew.run_personal_finance_planning(client_profile)
```

### Investment Analysis
```python
investment_details = "Diversified tech portfolio with FAANG stocks"
result = crew.run_investment_analysis(investment_details)
```

## 📊 What You Get

### Financial Analysis Reports Include:
- Revenue and profitability trends (3-5 years)
- Key financial ratios (P/E, ROE, ROA, Debt-to-Equity)
- Industry peer comparisons
- Cash flow and liquidity analysis
- Market position assessment

### Risk Assessment Reports Include:
- Market risk analysis (beta, volatility)
- Value at Risk (VaR) calculations
- Stress testing scenarios
- Risk-adjusted return metrics
- Mitigation strategies

### Budget Plans Include:
- Income and expense categorization
- Monthly/annual budget allocations
- Emergency fund recommendations
- Debt repayment strategies
- Savings goals and timelines

### Investment Strategies Include:
- Asset allocation recommendations
- Diversification strategies
- Portfolio rebalancing schedules
- Tax-efficient investment approaches
- Performance monitoring guidelines

## 🏗 Architecture

```
CrewAgents/
├── main.py              # Main application and FinanceCrew class
├── agents.py            # AI agent definitions and configurations
├── tasks.py             # Task definitions for each service type
├── demo.py              # Demo script showcasing capabilities
├── requirements.txt     # Python dependencies
├── test_app.py         # Application tests
└── test_run.py         # Test runner
```

## 🧪 Testing

Run the demo to verify everything is working:
```bash
python demo.py
```

Run tests:
```bash
python test_app.py
```

## 🔧 Configuration

### Environment Variables
- `OPENAI_API_KEY`: Your OpenAI API key (required)

### Model Configuration
The system uses GPT-3.5-turbo by default. You can modify the model in `agents.py`:
```python
self.llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.1)
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests to ensure functionality
5. Submit a pull request

## 📝 License

This project is open source and available under the MIT License.

## ⚠️ Disclaimer

This system provides AI-generated financial analysis and recommendations for educational and informational purposes only. It should not be considered as professional financial advice. Always consult with qualified financial professionals before making investment decisions.

## 🔗 Dependencies

- **CrewAI**: Multi-agent AI framework
- **LangChain**: LLM integration and chaining
- **OpenAI**: GPT model access
- **Python-dotenv**: Environment variable management

## 📞 Support

For issues or questions:
1. Check the demo output for system status
2. Verify your OpenAI API key is correctly configured
3. Ensure all dependencies are installed
4. Review error messages for troubleshooting guidance

---

**Ready to revolutionize your financial analysis with AI! 🚀**