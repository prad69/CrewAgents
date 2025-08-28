import os
from dotenv import load_dotenv
from crewai import Crew, Process
from agents import FinanceAgents
from tasks import FinanceTasks

# Load environment variables
load_dotenv()


class FinanceCrew:
    def __init__(self):
        self.agents = FinanceAgents()
        self.tasks = FinanceTasks()
    
    def run_financial_analysis(self, company_name):
        """Run a complete financial analysis for a company"""
        
        # Initialize agents
        financial_analyst = self.agents.financial_analyst_agent()
        risk_analyst = self.agents.risk_assessment_agent()
        budget_planner = self.agents.budget_planner_agent()
        investment_advisor = self.agents.investment_advisor_agent()
        
        # Create tasks
        analysis_task = self.tasks.financial_analysis_task(
            agent=financial_analyst,
            company_or_data=company_name
        )
        
        risk_task = self.tasks.risk_assessment_task(
            agent=risk_analyst,
            investment_or_portfolio=f"{company_name} stock investment"
        )
        
        # Create and run crew
        crew = Crew(
            agents=[financial_analyst, risk_analyst],
            tasks=[analysis_task, risk_task],
            verbose=2,
            process=Process.sequential
        )
        
        result = crew.kickoff()
        return result
    
    def run_personal_finance_planning(self, client_profile):
        """Run personal financial planning for an individual"""
        
        # Initialize agents
        budget_planner = self.agents.budget_planner_agent()
        risk_analyst = self.agents.risk_assessment_agent()
        investment_advisor = self.agents.investment_advisor_agent()
        financial_analyst = self.agents.financial_analyst_agent()
        
        # Create tasks
        budget_task = self.tasks.budget_planning_task(
            agent=budget_planner,
            financial_situation=client_profile
        )
        
        investment_task = self.tasks.investment_advisory_task(
            agent=investment_advisor,
            investor_profile=client_profile
        )
        
        comprehensive_review = self.tasks.comprehensive_financial_review_task(
            agent=financial_analyst,
            client_data=client_profile
        )
        
        # Create and run crew
        crew = Crew(
            agents=[budget_planner, investment_advisor, financial_analyst],
            tasks=[budget_task, investment_task, comprehensive_review],
            verbose=2,
            process=Process.sequential
        )
        
        result = crew.kickoff()
        return result
    
    def run_investment_analysis(self, investment_details):
        """Run comprehensive investment analysis"""
        
        # Initialize all agents
        financial_analyst = self.agents.financial_analyst_agent()
        risk_analyst = self.agents.risk_assessment_agent()
        investment_advisor = self.agents.investment_advisor_agent()
        
        # Create tasks
        analysis_task = self.tasks.financial_analysis_task(
            agent=financial_analyst,
            company_or_data=investment_details
        )
        
        risk_task = self.tasks.risk_assessment_task(
            agent=risk_analyst,
            investment_or_portfolio=investment_details
        )
        
        advisory_task = self.tasks.investment_advisory_task(
            agent=investment_advisor,
            investor_profile=f"Analysis for {investment_details}"
        )
        
        # Create and run crew
        crew = Crew(
            agents=[financial_analyst, risk_analyst, investment_advisor],
            tasks=[analysis_task, risk_task, advisory_task],
            verbose=2,
            process=Process.sequential
        )
        
        result = crew.kickoff()
        return result

def main():
    """Main function to demonstrate the finance crew capabilities"""
    
    print("🏦 Welcome to the Finance Crew AI System!")
    print("=" * 50)
    
    finance_crew = FinanceCrew()
    
    while True:
        print("\nAvailable Services:")
        print("1. Company Financial Analysis")
        print("2. Personal Financial Planning") 
        print("3. Investment Analysis")
        print("4. Exit")
        
        choice = input("\nSelect a service (1-4): ").strip()
        
        if choice == "1":
            company = input("Enter company name for analysis: ").strip()
            if company:
                print(f"\n🔍 Running financial analysis for {company}...")
                try:
                    result = finance_crew.run_financial_analysis(company)
                    print("\n" + "="*50)
                    print("FINANCIAL ANALYSIS RESULTS")
                    print("="*50)
                    print(result)
                except Exception as e:
                    print(f"Error: {e}")
            else:
                print("Please enter a valid company name.")
        
        elif choice == "2":
            print("\nPersonal Financial Planning")
            print("Please provide your financial information:")
            age = input("Age: ").strip()
            income = input("Annual income: ").strip()
            savings = input("Current savings: ").strip()
            goals = input("Financial goals: ").strip()
            
            client_profile = f"Age: {age}, Income: {income}, Savings: {savings}, Goals: {goals}"
            
            print(f"\n💰 Creating personal financial plan...")
            try:
                result = finance_crew.run_personal_finance_planning(client_profile)
                print("\n" + "="*50)
                print("PERSONAL FINANCIAL PLAN")
                print("="*50)
                print(result)
            except Exception as e:
                print(f"Error: {e}")
        
        elif choice == "3":
            investment = input("Enter investment details (stock, bond, portfolio): ").strip()
            if investment:
                print(f"\n📊 Analyzing investment: {investment}...")
                try:
                    result = finance_crew.run_investment_analysis(investment)
                    print("\n" + "="*50)
                    print("INVESTMENT A
                    1NALYSIS RESULTS")
                    print("="*50)
                    print(result)
                except Exception as e:
                    print(f"Error: {e}")
            else:
                print("Please enter valid investment details.")
        
        elif choice == "4":
            print("\nThank you for using Finance Crew AI! 👋")
            break
        
        else:
            print("Invalid choice. Please select 1-4.")

if __name__ == "__main__":
    main()