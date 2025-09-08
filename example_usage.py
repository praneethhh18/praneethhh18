#!/usr/bin/env python3
"""
Example Usage of Praneeth's AI Agent
====================================

This script demonstrates various ways to use the AI Agent
and showcases its capabilities across different domains.
"""

from ai_agent import AIAgent
import time

def demo_agent_capabilities():
    """Demonstrate the AI Agent's capabilities."""
    print("🚀 **Praneeth's AI Agent - Capability Demo**")
    print("=" * 50)
    
    # Initialize the agent
    agent = AIAgent()
    
    # Example queries for different domains
    example_queries = [
        {
            "category": "🌾 Agriculture",
            "query": "My wheat crops have yellow spots and wilting. What could be the problem?",
            "description": "Agriculture disease diagnosis"
        },
        {
            "category": "💻 Programming", 
            "query": "How do I implement a machine learning model in Python using TensorFlow?",
            "description": "AI/ML programming help"
        },
        {
            "category": "🔬 Research",
            "query": "What research methodology should I use for analyzing farmer adoption of new technologies?",
            "description": "Research methodology guidance"
        },
        {
            "category": "🌐 Web Development",
            "query": "Help me build a React application with API integration",
            "description": "Web development assistance"
        },
        {
            "category": "💬 General",
            "query": "Hello! Can you tell me about your capabilities?",
            "description": "General conversation"
        }
    ]
    
    print(f"\n🎯 **Testing {len(example_queries)} different query types:**\n")
    
    for i, example in enumerate(example_queries, 1):
        print(f"**[{i}] {example['category']} - {example['description']}**")
        print(f"👤 Query: \"{example['query']}\"")
        print()
        
        # Process the query
        response = agent.process_query(example['query'])
        
        # Show abbreviated response
        response_lines = response.split('\n')
        abbreviated_response = '\n'.join(response_lines[:5])
        if len(response_lines) > 5:
            abbreviated_response += "\n... [response continues] ..."
        
        print(f"🤖 Response: {abbreviated_response}")
        print("\n" + "-" * 60 + "\n")
        
        # Add a small delay for better readability
        time.sleep(1)
    
    print("✅ **Demo completed!** The agent successfully handled all query types.")
    print("\n💡 **To try interactive mode, run:** `python ai_agent.py`")

def test_special_commands():
    """Test special commands and features."""
    print("\n🛠️  **Testing Special Commands:**")
    print("=" * 40)
    
    agent = AIAgent()
    
    # Test configuration display
    print("\n1. Testing configuration display:")
    agent.show_config()
    
    # Test conversation history (after some interactions)
    print("\n2. Testing conversation history:")
    agent.process_query("Hello!")
    agent.process_query("Help with Python")
    agent.show_conversation_history()
    
    # Test history clearing
    print("\n3. Testing history clearing:")
    agent.clear_history()
    
    print("\n✅ Special commands tested successfully!")

def demonstrate_customization():
    """Show how to customize the agent."""
    print("\n🎨 **Customization Example:**")
    print("=" * 35)
    
    # Create custom config
    custom_config = {
        "agent_name": "Custom Agricultural Assistant",
        "expertise_areas": ["Agriculture", "Sustainable Farming", "Crop Science"],
        "conversation_memory": 5,
        "agriculture_knowledge": True,
        "research_mode": False
    }
    
    # Save custom config
    import json
    with open("custom_config.json", "w") as f:
        json.dump(custom_config, f, indent=2)
    
    # Initialize with custom config
    custom_agent = AIAgent("custom_config.json")
    
    print(f"✅ Created custom agent: {custom_agent.agent_name}")
    print(f"📚 Specialized in: {', '.join(custom_agent.expertise_areas)}")
    
    # Test custom agent
    response = custom_agent.process_query("Tell me about sustainable farming practices")
    print(f"\n🌱 Custom agent response preview:")
    print(response[:200] + "..." if len(response) > 200 else response)

def main():
    """Main demo function."""
    print("🎭 **Praneeth's AI Agent - Complete Demo**")
    print("=" * 50)
    print("This demo showcases the agent's capabilities across different domains.")
    print("The agent specializes in agriculture, programming, research, and general assistance.")
    print()
    
    try:
        # Run capability demo
        demo_agent_capabilities()
        
        # Test special commands
        test_special_commands()
        
        # Show customization options
        demonstrate_customization()
        
        print("\n🎉 **Demo Complete!**")
        print("\n🚀 **Next Steps:**")
        print("1. Run `python ai_agent.py` for interactive mode")
        print("2. Try `python ai_agent.py --query 'your question'` for single queries")
        print("3. Customize `config.json` for your specific needs")
        print("4. Extend the agent with your own knowledge areas")
        
    except Exception as e:
        print(f"❌ Error during demo: {e}")
        print("Please ensure ai_agent.py is in the same directory.")

if __name__ == "__main__":
    main()