from crewai import Task

class FinanceTasks:
    def financial_analysis_task(self, agent, company_or_data):
        return Task(
            description=f"""
            Conduct a comprehensive financial analysis for {company_or_data}. Your analysis should include:
            
            1. Revenue and profitability trends over the last 3-5 years
            2. Key financial ratios (P/E, ROE, ROA, Debt-to-Equity, Current Ratio)
            3. Comparison with industry peers and benchmarks
            4. Cash flow analysis and liquidity assessment
            5. Identification of financial strengths and weaknesses
            6. Market position and competitive advantages
            
            Provide clear, actionable insights with supporting data and reasoning.
            """,
            agent=agent,
            expected_output="A detailed financial analysis report with key metrics, trends, and recommendations"
        )
    
    def risk_assessment_task(self, agent, investment_or_portfolio):
        return Task(
            description=f"""
            Perform a thorough risk assessment for {investment_or_portfolio}. Your assessment should cover:
            
            1. Market risk analysis (beta, volatility, correlation with market indices)
            2. Credit risk evaluation (if applicable to bonds or debt instruments)
            3. Liquidity risk assessment
            4. Sector and geographic concentration risks
            5. Interest rate sensitivity analysis
            6. Stress testing under different market scenarios
            7. Value at Risk (VaR) calculations
            8. Risk-adjusted return metrics (Sharpe ratio, Sortino ratio)
            
            Provide specific risk mitigation recommendations and optimal risk levels.
            """,
            agent=agent,
            expected_output="A comprehensive risk assessment report with quantified risk metrics and mitigation strategies"
        )
    
    def budget_planning_task(self, agent, financial_situation):
        return Task(
            description=f"""
            Create a comprehensive budget plan for {financial_situation}. Your plan should include:
            
            1. Income analysis and categorization (salary, investments, other sources)
            2. Expense breakdown by categories (fixed, variable, discretionary)
            3. Monthly and annual budget allocation recommendations
            4. Emergency fund planning (3-6 months of expenses)
            5. Debt repayment strategy (if applicable)
            6. Savings goals and timelines
            7. Budget tracking and monitoring methods
            8. Cost reduction opportunities and optimization strategies
            
            Provide practical, actionable budget recommendations with specific dollar amounts and percentages.
            """,
            agent=agent,
            expected_output="A detailed budget plan with income/expense breakdown, savings targets, and implementation guidance"
        )
    
    def investment_advisory_task(self, agent, investor_profile):
        return Task(
            description=f"""
            Develop a personalized investment strategy for {investor_profile}. Your recommendations should include:
            
            1. Asset allocation strategy based on risk tolerance and time horizon
            2. Specific investment vehicle recommendations (stocks, bonds, ETFs, mutual funds)
            3. Diversification strategy across sectors, geographies, and asset classes
            4. Portfolio rebalancing schedule and triggers
            5. Tax-efficient investment strategies
            6. Investment timeline and milestone targets
            7. Performance monitoring and review schedule
            8. Exit strategies and profit-taking guidelines
            
            Consider the investor's goals, current financial situation, risk tolerance, and investment timeline.
            """,
            agent=agent,
            expected_output="A personalized investment strategy with specific asset allocation, investment recommendations, and implementation plan"
        )
    
    def comprehensive_financial_review_task(self, agent, client_data):
        return Task(
            description=f"""
            Synthesize all financial analysis, risk assessment, budgeting, and investment recommendations 
            for {client_data} into a comprehensive financial review. Your review should:
            
            1. Summarize key findings from all financial analyses
            2. Identify the most critical financial priorities and action items
            3. Create an integrated financial plan that aligns all recommendations
            4. Establish clear timelines and milestones for implementation
            5. Identify potential conflicts or trade-offs between different strategies
            6. Provide a prioritized action plan with short-term and long-term goals
            7. Recommend regular review and adjustment schedules
            
            Ensure all recommendations work together coherently and support the overall financial objectives.
            """,
            agent=agent,
            expected_output="An integrated comprehensive financial plan with prioritized recommendations and implementation roadmap"
        )