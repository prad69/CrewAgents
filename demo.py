"""
Demo script to showcase the Finance Crew AI capabilities
"""

import os
from dotenv import load_dotenv
from agents import FinanceAgents
from tasks import FinanceTasks

# Load environment variables
load_dotenv()

def demo_agents():
    """Demonstrate agent creation and basic functionality"""
    print("🤖 Creating Finance Agents...")
    print("=" * 40)
    
    try:
        agents = FinanceAgents()
        
        # Create all agents
        financial_analyst = agents.financial_analyst_agent()
        risk_analyst = agents.risk_assessment_agent()
        budget_planner = agents.budget_planner_agent()
        investment_advisor = agents.investment_advisor_agent()
        
        print("✅ Successfully created all 4 agents:")
        print(f"   1. {financial_analyst.role}")
        print(f"      Goal: {financial_analyst.goal[:80]}...")
        
        print(f"   2. {risk_analyst.role}")
        print(f"      Goal: {risk_analyst.goal[:80]}...")
        
        print(f"   3. {budget_planner.role}")
        print(f"      Goal: {budget_planner.goal[:80]}...")
        
        print(f"   4. {investment_advisor.role}")
        print(f"      Goal: {investment_advisor.goal[:80]}...")
        
        return True
        
    except Exception as e:
        print(f"❌ Error creating agents: {e}")
        return False

def demo_tasks():
    """Demonstrate task crea
    tion"""
    print("\n📋 Creating Finance Tasks...")
    print("=" * 40)
    
    try:
        agents = FinanceAgents()
        tasks = FinanceTasks()
        
        # Create sample agent and tasks
        analyst = agents.financial_analyst_agent()
        
        # Sample tasks
        task1 = tasks.financial_analysis_task(analyst, "Apple Inc.")
        task2 = tasks.risk_assessment_task(analyst, "Technology portfolio")
        
        print("✅ Successfully created sample tasks:")
        print(f"   1. Financial Analysis Task")
        print(f"      Description: {task1.description[:100]}...")
        
        print(f"   2. Risk Assessment Task") 
        print(f"      Description: {task2.description[:100]}...")
        
        return True
        
    except Exception as e:
        print(f"❌ Error creating tasks: {e}")
        return False

def demo_crew_setup():
    """Demonstrate crew setup without running (to avoid API costs)"""
    print("\n🚀 Setting up Finance Crew...")
    print("=" * 40)
    
    try:
        from main import FinanceCrew
        
        # Initialize crew
        finance_crew = FinanceCrew()
        
        print("✅ Successfully initialized FinanceCrew!")
        print("\nAvailable methods:")
        print("   • run_financial_analysis(company_name)")
        print("   • run_personal_finance_planning(client_profile)")
        print("   • run_investment_analysis(investment_details)")
        
        return True
        
    except Exception as e:
        print(f"❌ Error setting up crew: {e}")
        return False

def show_api_setup():
    """Show API setup instructions"""
    print("\n🔑 API Setup Instructions")
    print("=" * 40)
    
    api_key = os.getenv('OPENAI_API_KEY')
    
    if api_key:
        print("✅ OpenAI API key is configured")
        print("   You can run the full application with: python3 main.py")
    else:
        print("⚠️  OpenAI API key not found")
        print("   To use the full application:")
        print("   1. Get an API key from https://platform.openai.com/api-keys")
        print("   2. Create a .env file with: OPENAI_API_KEY=your_key_here")
        print("   3. Run: python3 main.py")

def show_usage_examples():
    """Show practical usage examples"""
    print("\n💡 Usage Examples")
    print("=" * 40)
    
    examples = [
        {
            "service": "Company Financial Analysis",
            "input": "Apple Inc.",
            "output": "Comprehensive analysis of AAPL financial health, ratios, and investment potential"
        },
        {
            "service": "Personal Financial Planning",
            "input": "Age: 30, Income: $75,000, Savings: $25,000, Goals: Buy house in 5 years",
            "output": "Custom budget plan, savings strategy, and timeline for home purchase"
        },
        {
            "service": "Investment Analysis",
            "input": "Tech-heavy portfolio with FAANG stocks",
            "output": "Risk assessment, diversification recommendations, and optimization strategies"
        }
    ]
    
    for i, example in enumerate(examples, 1):
        print(f"\n{i}. {example['service']}")
        print(f"   Input: {example['input']}")
        print(f"   Output: {example['output']}")

if __name__ == "__main__":
    print("🏦 Finance Crew AI - Demo Mode")
    print("=" * 50)
    
    # Run all demos
    tests = [
        ("Agent Creation", demo_agents),
        ("Task Creation", demo_tasks),
        ("Crew Setup", demo_crew_setup),
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"\n🧪 Testing: {test_name}")
        if test_func():
            passed += 1
        print("-" * 30)
    
    # Show additional info
    show_api_setup()
    show_usage_examples()
    
    # Summary
    print(f"\n📊 Demo Results: {passed}/{total} components working correctly")
    
    if passed == total:
        print("🎉 All components are working! The Finance Crew AI is ready to use.")
    else:
        print("⚠️ Some components had issues. Check error messages above.")
    
    print("\n🚀 Ready to solve finance problems with AI agents!")
    