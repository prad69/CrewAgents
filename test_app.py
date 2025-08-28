"""
Simple test script to verify the CrewAI finance application structure
"""

def test_imports():
    """Test if all modules can be imported successfully"""
    try:
        from agents import FinanceAgents
        from tasks import FinanceTasks
        from main import FinanceCrew
        print("✅ All imports successful")
        return True
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False

def test_agent_creation():
    """Test if agents can be created successfully"""
    try:
        from agents import FinanceAgents
        agents = FinanceAgents()
        
        # Test creating each agent
        financial_analyst = agents.financial_analyst_agent()
        risk_analyst = agents.risk_assessment_agent()
        budget_planner = agents.budget_planner_agent()
        investment_advisor = agents.investment_advisor_agent()
        
        print("✅ All agents created successfully")
        print(f"   - Financial Analyst: {financial_analyst.role}")
        print(f"   - Risk Analyst: {risk_analyst.role}")
        print(f"   - Budget Planner: {budget_planner.role}")
        print(f"   - Investment Advisor: {investment_advisor.role}")
        return True
    except Exception as e:
        print(f"❌ Agent creation error: {e}")
        return False

def test_task_creation():
    """Test if tasks can be created successfully"""
    try:
        from agents import FinanceAgents
        from tasks import FinanceTasks
        
        agents = FinanceAgents()
        tasks = FinanceTasks()
        
        # Create a sample agent and task
        analyst = agents.financial_analyst_agent()
        task = tasks.financial_analysis_task(analyst, "Apple Inc.")
        
        print("✅ Task creation successful")
        print(f"   - Task description preview: {task.description[:100]}...")
        return True
    except Exception as e:
        print(f"❌ Task creation error: {e}")
        return False

def test_crew_initialization():
    """Test if the main crew class can be initialized"""
    try:
        from main import FinanceCrew
        
        crew = FinanceCrew()
        print("✅ FinanceCrew initialization successful")
        return True
    except Exception as e:
        print(f"❌ Crew initialization error: {e}")
        return False

if __name__ == "__main__":
    print("🧪 Testing CrewAI Finance Application")
    print("=" * 40)
    
    tests = [
        test_imports,
        test_agent_creation,
        test_task_creation,
        test_crew_initialization
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        print(f"\nRunning {test.__name__}...")
        if test():
            passed += 1
        print("-" * 30)
    
    print(f"\n📊 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! The application structure is ready.")
        print("\nNext steps:")
        print("1. Install dependencies: pip install -r requirements.txt")
        print("2. Set up your OpenAI API key in a .env file")
        print("3. Run the application: python main.py")
    else:
        print("⚠️ Some tests failed. Please check the error messages above.")