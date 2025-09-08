#!/usr/bin/env python3
"""
Simple tests for Praneeth's AI Agent
====================================

Basic test suite to verify agent functionality.
"""

import sys
import os
import json

# Add current directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_agent_initialization():
    """Test that the agent initializes correctly."""
    print("🧪 Testing agent initialization...")
    
    try:
        from ai_agent import AIAgent
        agent = AIAgent()
        assert agent.agent_name == "Praneeth's AI Assistant"
        assert len(agent.expertise_areas) > 0
        print("✅ Agent initialization: PASSED")
        return True
    except Exception as e:
        print(f"❌ Agent initialization: FAILED - {e}")
        return False

def test_configuration_loading():
    """Test configuration loading functionality."""
    print("🧪 Testing configuration loading...")
    
    try:
        from ai_agent import AIAgent
        
        # Test with existing config
        if os.path.exists("config.json"):
            agent = AIAgent("config.json")
            assert agent.config is not None
            print("✅ Configuration loading: PASSED")
            return True
        else:
            print("⚠️  No config.json found, testing default config creation...")
            agent = AIAgent("test_config.json")
            assert os.path.exists("test_config.json")
            os.remove("test_config.json")  # Cleanup
            print("✅ Default configuration creation: PASSED")
            return True
    except Exception as e:
        print(f"❌ Configuration loading: FAILED - {e}")
        return False

def test_query_processing():
    """Test basic query processing."""
    print("🧪 Testing query processing...")
    
    try:
        from ai_agent import AIAgent
        agent = AIAgent()
        
        # Test different types of queries
        test_queries = [
            "Hello",
            "Help with crop diseases",
            "Python programming question",
            "Research methodology help"
        ]
        
        for query in test_queries:
            response = agent.process_query(query)
            assert isinstance(response, str)
            assert len(response) > 0
        
        print("✅ Query processing: PASSED")
        return True
    except Exception as e:
        print(f"❌ Query processing: FAILED - {e}")
        return False

def test_agriculture_knowledge():
    """Test agriculture-specific functionality."""
    print("🧪 Testing agriculture knowledge...")
    
    try:
        from ai_agent import AIAgent
        agent = AIAgent()
        
        agriculture_queries = [
            "crop disease identification",
            "soil management tips", 
            "irrigation advice"
        ]
        
        for query in agriculture_queries:
            response = agent.get_agriculture_advice(query)
            if not ("🌾" in response or "🌱" in response or "💧" in response or "Agriculture" in response or "Fertilizer" in response or "Irrigation" in response):
                print(f"Failed query: {query}")
                print(f"Response: {response[:100]}")
                raise AssertionError(f"Agriculture response doesn't contain expected content for query: {query}")
        
        print("✅ Agriculture knowledge: PASSED")
        return True
    except Exception as e:
        print(f"❌ Agriculture knowledge: FAILED - {e}")
        return False

def test_programming_help():
    """Test programming assistance functionality."""
    print("🧪 Testing programming help...")
    
    try:
        from ai_agent import AIAgent
        agent = AIAgent()
        
        programming_queries = [
            "Python machine learning",
            "JavaScript web development",
            "ML model training"
        ]
        
        for query in programming_queries:
            response = agent.get_programming_help(query)
            if not ("🐍" in response or "🤖" in response or "🌐" in response or "Programming" in response or "Python" in response or "Machine Learning" in response):
                print(f"Failed query: {query}")
                print(f"Response: {response[:100]}")
                raise AssertionError(f"Programming response doesn't contain expected content for query: {query}")
        
        print("✅ Programming help: PASSED")
        return True
    except Exception as e:
        print(f"❌ Programming help: FAILED - {e}")
        return False

def test_conversation_history():
    """Test conversation history functionality."""
    print("🧪 Testing conversation history...")
    
    try:
        from ai_agent import AIAgent
        agent = AIAgent()
        
        # Add some conversations
        agent.process_query("Hello")
        agent.process_query("Help me with Python")
        
        # Check history
        assert len(agent.conversation_history) == 2
        
        # Test clearing
        agent.clear_history()
        assert len(agent.conversation_history) == 0
        
        print("✅ Conversation history: PASSED")
        return True
    except Exception as e:
        print(f"❌ Conversation history: FAILED - {e}")
        return False

def run_all_tests():
    """Run all tests and report results."""
    print("🚀 **Praneeth's AI Agent - Test Suite**")
    print("=" * 45)
    
    tests = [
        test_agent_initialization,
        test_configuration_loading,
        test_query_processing,
        test_agriculture_knowledge,
        test_programming_help,
        test_conversation_history
    ]
    
    passed_tests = 0
    total_tests = len(tests)
    
    for test in tests:
        if test():
            passed_tests += 1
        print()
    
    print("=" * 45)
    print(f"📊 **Test Results: {passed_tests}/{total_tests} tests passed**")
    
    if passed_tests == total_tests:
        print("🎉 All tests passed! The agent is working correctly.")
        return True
    else:
        print("⚠️  Some tests failed. Please check the errors above.")
        return False

if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)