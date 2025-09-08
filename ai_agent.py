#!/usr/bin/env python3
"""
AI Agent - Praneeth's Personal Assistant
==========================================

A conversational AI agent designed to assist with various tasks including:
- General conversation and Q&A
- Agriculture and farming guidance
- Research assistance
- Programming and coding help
- Task automation

Author: Praneeth P K
Created: 2024
"""

import json
import os
import sys
import time
from datetime import datetime
from typing import Dict, List, Optional, Any
import argparse

class AIAgent:
    """
    Main AI Agent class with conversational capabilities and specialized knowledge.
    """
    
    def __init__(self, config_path: str = "config.json"):
        """Initialize the AI Agent with configuration."""
        self.config = self.load_config(config_path)
        self.conversation_history = []
        self.agent_name = self.config.get("agent_name", "Praneeth's AI Assistant")
        self.expertise_areas = self.config.get("expertise_areas", [
            "AI/ML", "Agriculture", "Research", "Programming", "Data Science"
        ])
        
        print(f"🤖 {self.agent_name} initialized successfully!")
        print(f"📚 Expertise areas: {', '.join(self.expertise_areas)}")
    
    def load_config(self, config_path: str) -> Dict[str, Any]:
        """Load configuration from JSON file."""
        default_config = {
            "agent_name": "Praneeth's AI Assistant",
            "version": "1.0.0",
            "expertise_areas": ["AI/ML", "Agriculture", "Research", "Programming"],
            "agriculture_knowledge": True,
            "research_mode": True,
            "conversation_memory": 10
        }
        
        if os.path.exists(config_path):
            try:
                with open(config_path, 'r') as f:
                    config = json.load(f)
                    return {**default_config, **config}
            except Exception as e:
                print(f"⚠️  Error loading config: {e}. Using defaults.")
                return default_config
        else:
            # Create default config file
            with open(config_path, 'w') as f:
                json.dump(default_config, f, indent=2)
            return default_config
    
    def get_agriculture_advice(self, query: str) -> str:
        """Provide agriculture-related guidance and advice."""
        agriculture_knowledge = {
            "disease": {
                "keywords": ["disease", "infection", "pest", "fungus", "bacteria", "virus"],
                "response": """🌾 **Agriculture Disease Guidance:**
                
For crop disease diagnosis:
1. **Visual Inspection**: Look for discoloration, spots, wilting, or unusual growth
2. **Common Diseases**: 
   - Leaf spots (fungal infections)
   - Root rot (overwatering/poor drainage)
   - Blight (bacterial/fungal)
   - Mosaic virus (yellowing patterns)
   
3. **Prevention**: Crop rotation, proper spacing, disease-resistant varieties
4. **Treatment**: Targeted fungicides, organic solutions, or biological controls

💡 **Tip**: Document symptoms with photos for better diagnosis!
"""
            },
            "fertilizer": {
                "keywords": ["fertilizer", "nutrient", "soil", "npk", "manure"],
                "response": """🌱 **Fertilizer and Soil Management:**
                
**NPK Basics:**
- **N (Nitrogen)**: Promotes leafy growth
- **P (Phosphorus)**: Root development and flowering
- **K (Potassium)**: Disease resistance and fruit quality

**Soil Testing**: Essential for determining nutrient needs
**Organic Options**: Compost, manure, bio-fertilizers
**Application Timing**: Pre-planting, growth stages, post-harvest

📊 **Recommendation**: Get soil tested annually for optimal fertilizer planning.
"""
            },
            "irrigation": {
                "keywords": ["water", "irrigation", "drought", "watering"],
                "response": """💧 **Smart Irrigation Practices:**
                
**Water Management:**
- **Drip Irrigation**: Most efficient, 90%+ water efficiency
- **Sprinkler Systems**: Good for uniform coverage
- **Smart Sensors**: Soil moisture monitoring
- **Timing**: Early morning or evening to reduce evaporation

**Water Conservation:**
- Mulching to retain moisture
- Rainwater harvesting
- Drought-resistant crop varieties

🎯 **Goal**: Right amount of water at the right time!
"""
            }
        }
        
        query_lower = query.lower()
        for category, info in agriculture_knowledge.items():
            if any(keyword in query_lower for keyword in info["keywords"]):
                return info["response"]
        
        return """🌾 **General Agriculture Guidance:**
        
I can help with:
- Crop disease identification and treatment
- Soil management and fertilization
- Irrigation and water management
- Pest control strategies
- Crop planning and rotation
- Sustainable farming practices

Please specify your question area (disease, fertilizer, irrigation, etc.) for detailed guidance!
"""
    
    def get_programming_help(self, query: str) -> str:
        """Provide programming and coding assistance."""
        programming_help = {
            "python": {
                "keywords": ["python", "py", "pandas", "numpy", "tensorflow", "pytorch"],
                "response": """🐍 **Python Development Help:**
                
**AI/ML Libraries:**
- **TensorFlow/Keras**: Deep learning frameworks
- **PyTorch**: Research-focused deep learning
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computing
- **Scikit-learn**: Traditional ML algorithms

**Best Practices:**
- Use virtual environments (venv, conda)
- Follow PEP 8 style guidelines
- Write unit tests
- Document your code
- Use type hints for better code clarity

💡 **Tip**: Start with small projects and gradually build complexity!
"""
            },
            "ml": {
                "keywords": ["machine learning", "ml", "model", "training", "dataset"],
                "response": """🤖 **Machine Learning Guidance:**
                
**ML Pipeline:**
1. **Data Collection & Cleaning**
2. **Exploratory Data Analysis (EDA)**
3. **Feature Engineering**
4. **Model Selection & Training**
5. **Evaluation & Validation**
6. **Deployment & Monitoring**

**Common Algorithms:**
- **Classification**: Random Forest, SVM, Neural Networks
- **Regression**: Linear/Polynomial Regression, Decision Trees
- **Clustering**: K-Means, DBSCAN
- **Deep Learning**: CNNs, RNNs, Transformers

🎯 **Remember**: Quality data beats complex algorithms!
"""
            },
            "web": {
                "keywords": ["web", "html", "css", "javascript", "react", "api"],
                "response": """🌐 **Web Development Help:**
                
**Frontend Technologies:**
- **React**: Component-based UI library
- **HTML5/CSS3**: Modern web standards
- **JavaScript/TypeScript**: Programming languages
- **Responsive Design**: Mobile-first approach

**Backend & APIs:**
- **RESTful APIs**: Standard for web services
- **Database Integration**: MySQL, MongoDB
- **Authentication**: JWT, OAuth
- **Deployment**: Cloud platforms (AWS, GCP)

🚀 **Project Idea**: Build a portfolio website showcasing your AI projects!
"""
            }
        }
        
        query_lower = query.lower()
        for category, info in programming_help.items():
            if any(keyword in query_lower for keyword in info["keywords"]):
                return info["response"]
        
        return """💻 **Programming Help Available:**
        
I can assist with:
- **Python**: AI/ML, data science, web development
- **JavaScript/TypeScript**: Frontend and backend development
- **Machine Learning**: Model development and deployment
- **Web Technologies**: React, APIs, databases
- **Best Practices**: Code quality, testing, documentation

What specific programming challenge can I help you with?
"""
    
    def get_research_assistance(self, query: str) -> str:
        """Provide research methodology and guidance."""
        return """🔬 **Research Assistance:**
        
**Research Methodology:**
1. **Problem Definition**: Clearly define research questions
2. **Literature Review**: Survey existing work and identify gaps
3. **Methodology Selection**: Choose appropriate research methods
4. **Data Collection**: Gather relevant and quality data
5. **Analysis**: Apply statistical/analytical methods
6. **Documentation**: Write clear, reproducible results

**Research Tools:**
- **Data Analysis**: Python (Pandas, NumPy), R
- **Visualization**: Matplotlib, Seaborn, Plotly
- **Documentation**: LaTeX, Markdown, Jupyter Notebooks
- **Version Control**: Git for tracking changes

**Tips for Success:**
- Start with a focused research question
- Maintain detailed research notes
- Collaborate with peers and mentors
- Present findings clearly and concisely

🎯 **Goal**: Contribute meaningful insights to your field of study!
"""
    
    def process_query(self, user_input: str) -> str:
        """Process user query and provide appropriate response."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Add to conversation history
        self.conversation_history.append({
            "timestamp": timestamp,
            "user": user_input,
            "agent": ""  # Will be filled after generating response
        })
        
        # Keep conversation history within memory limits
        memory_limit = self.config.get("conversation_memory", 10)
        if len(self.conversation_history) > memory_limit:
            self.conversation_history = self.conversation_history[-memory_limit:]
        
        user_input_lower = user_input.lower()
        
        # Agriculture-related queries
        if any(keyword in user_input_lower for keyword in [
            "crop", "farm", "agriculture", "plant", "soil", "fertilizer", 
            "disease", "pest", "irrigation", "harvest"
        ]):
            response = self.get_agriculture_advice(user_input)
        
        # Programming-related queries
        elif any(keyword in user_input_lower for keyword in [
            "code", "programming", "python", "javascript", "ml", "ai", 
            "model", "algorithm", "web", "api", "database"
        ]):
            response = self.get_programming_help(user_input)
        
        # Research-related queries
        elif any(keyword in user_input_lower for keyword in [
            "research", "study", "analysis", "methodology", "paper", 
            "experiment", "data", "statistics"
        ]):
            response = self.get_research_assistance(user_input)
        
        # General greetings and conversation
        elif any(keyword in user_input_lower for keyword in [
            "hello", "hi", "hey", "good morning", "good afternoon", "good evening"
        ]):
            response = f"""👋 **Hello! I'm {self.agent_name}**

I'm here to help you with:
🌾 **Agriculture**: Crop diseases, soil management, farming practices
💻 **Programming**: Python, AI/ML, web development, coding best practices  
🔬 **Research**: Methodology, data analysis, academic guidance
🤖 **AI/ML**: Model development, deployment, data science

How can I assist you today?
"""
        
        # Help command
        elif "help" in user_input_lower:
            response = f"""ℹ️  **{self.agent_name} - Help Menu**

**Available Commands:**
- Ask about agriculture, farming, or crop management
- Get programming help (Python, JavaScript, AI/ML)
- Research assistance and methodology guidance
- General conversation and Q&A

**Example Queries:**
- "How do I identify crop diseases?"
- "Help me with Python machine learning"
- "What's the best research methodology for my project?"
- "Explain React development basics"

**Special Commands:**
- `history` - View conversation history
- `config` - Show current configuration
- `clear` - Clear conversation history
- `exit` - End the session

Type your question naturally - I'll understand the context!
"""
        
        else:
            response = f"""🤔 **I'd love to help!**

I specialize in:
- 🌾 **Agriculture & Farming**
- 💻 **Programming & AI/ML** 
- 🔬 **Research & Analysis**

Could you please specify what you'd like help with? For example:
- "Help with crop disease identification"
- "Python programming question about..."
- "Research methodology for..."

Type `help` for more detailed guidance!
"""
        
        # Update conversation history with response
        self.conversation_history[-1]["agent"] = response
        
        return response
    
    def show_conversation_history(self) -> None:
        """Display conversation history."""
        if not self.conversation_history:
            print("📝 No conversation history yet.")
            return
        
        print("\n📜 **Conversation History:**")
        print("=" * 50)
        
        for i, entry in enumerate(self.conversation_history, 1):
            print(f"\n**[{i}] {entry['timestamp']}**")
            print(f"👤 **You:** {entry['user']}")
            print(f"🤖 **Agent:** {entry['agent'][:100]}...")
    
    def show_config(self) -> None:
        """Display current configuration."""
        print("\n⚙️  **Current Configuration:**")
        print("=" * 40)
        for key, value in self.config.items():
            print(f"• **{key}**: {value}")
    
    def clear_history(self) -> None:
        """Clear conversation history."""
        self.conversation_history.clear()
        print("🗑️  Conversation history cleared!")
    
    def interactive_mode(self) -> None:
        """Run the agent in interactive mode."""
        print(f"\n🚀 **{self.agent_name} - Interactive Mode**")
        print("=" * 50)
        print("Type 'exit' to quit, 'help' for assistance")
        print("=" * 50)
        
        while True:
            try:
                user_input = input("\n👤 You: ").strip()
                
                if not user_input:
                    continue
                
                if user_input.lower() in ['exit', 'quit', 'bye']:
                    print(f"\n👋 Thanks for using {self.agent_name}! Goodbye!")
                    break
                
                elif user_input.lower() == 'history':
                    self.show_conversation_history()
                    continue
                
                elif user_input.lower() == 'config':
                    self.show_config()
                    continue
                
                elif user_input.lower() == 'clear':
                    self.clear_history()
                    continue
                
                # Process the query
                print(f"\n🤖 **{self.agent_name}:**")
                response = self.process_query(user_input)
                print(response)
                
            except KeyboardInterrupt:
                print(f"\n\n👋 Session interrupted. Thanks for using {self.agent_name}!")
                break
            except Exception as e:
                print(f"\n❌ Error: {e}")
                print("Please try again or type 'help' for assistance.")

def main():
    """Main function to run the AI Agent."""
    parser = argparse.ArgumentParser(description="Praneeth's AI Agent")
    parser.add_argument("--config", default="config.json", help="Configuration file path")
    parser.add_argument("--query", help="Single query mode")
    parser.add_argument("--version", action="version", version="AI Agent v1.0.0")
    
    args = parser.parse_args()
    
    # Initialize the agent
    agent = AIAgent(config_path=args.config)
    
    if args.query:
        # Single query mode
        response = agent.process_query(args.query)
        print(f"\n🤖 **Response:**\n{response}")
    else:
        # Interactive mode
        agent.interactive_mode()

if __name__ == "__main__":
    main()