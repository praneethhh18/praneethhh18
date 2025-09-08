# 🤖 Praneeth's AI Agent

An intelligent conversational AI assistant designed to help with agriculture, programming, research, and general tasks. Built with Python and designed to be extensible and practical.

## 🌟 Features

- **🌾 Agriculture Guidance**: Crop disease identification, soil management, irrigation advice
- **💻 Programming Help**: Python, JavaScript, AI/ML, web development assistance  
- **🔬 Research Support**: Methodology guidance, data analysis, academic assistance
- **💬 Interactive Chat**: Natural conversation with context awareness
- **📝 History Tracking**: Conversation memory and session management
- **⚙️ Configurable**: Customizable settings and expertise areas

## 🚀 Quick Start

### Prerequisites
- Python 3.7 or higher
- No external dependencies required for basic functionality

### Installation

1. **Clone or download the repository**
   ```bash
   git clone https://github.com/praneethhh18/praneethhh18.git
   cd praneethhh18
   ```

2. **Run the agent**
   ```bash
   python ai_agent.py
   ```

That's it! The agent will start in interactive mode.

## 📖 Usage

### Interactive Mode (Default)
```bash
python ai_agent.py
```

Start a conversation with the AI agent. Type your questions naturally!

### Single Query Mode
```bash
python ai_agent.py --query "How do I identify crop diseases?"
```

Get a quick response to a specific question.

### Custom Configuration
```bash
python ai_agent.py --config my_config.json
```

Use a custom configuration file.

## 💬 Example Conversations

### Agriculture Help
```
👤 You: My tomato plants have yellow spots on leaves
🤖 Agent: 🌾 Agriculture Disease Guidance:
This sounds like a potential fungal infection...
[Detailed diagnosis and treatment advice]
```

### Programming Assistance  
```
👤 You: Help me with Python machine learning
🤖 Agent: 🐍 Python Development Help:
AI/ML Libraries:
- TensorFlow/Keras: Deep learning frameworks
- PyTorch: Research-focused deep learning...
[Comprehensive programming guidance]
```

### Research Support
```
👤 You: What's the best research methodology for my project?
🤖 Agent: 🔬 Research Assistance:
Research Methodology:
1. Problem Definition: Clearly define research questions...
[Detailed research guidance]
```

## 🛠️ Available Commands

- **General conversation**: Ask questions naturally
- **`help`**: Show help menu and available commands
- **`history`**: View conversation history
- **`config`**: Display current configuration
- **`clear`**: Clear conversation history  
- **`exit`** or **`quit`**: End the session

## ⚙️ Configuration

The agent uses `config.json` for settings. Key options:

```json
{
  "agent_name": "Praneeth's AI Assistant",
  "expertise_areas": ["AI/ML", "Agriculture", "Research", "Programming"],
  "conversation_memory": 10,
  "agriculture_knowledge": true,
  "research_mode": true
}
```

### Configuration Options

- **`agent_name`**: Display name for the agent
- **`expertise_areas`**: List of specialization areas
- **`conversation_memory`**: Number of conversations to remember
- **`agriculture_knowledge`**: Enable agriculture assistance
- **`research_mode`**: Enable research guidance features

## 🎯 Specialized Knowledge Areas

### 🌾 Agriculture & Farming
- Crop disease identification and treatment
- Soil management and fertilization
- Irrigation and water management
- Pest control strategies
- Sustainable farming practices
- Crop planning and rotation

### 💻 Programming & Development
- **Python**: AI/ML, data science, web development
- **JavaScript/TypeScript**: Frontend and backend
- **AI/ML**: TensorFlow, PyTorch, scikit-learn
- **Web**: React, APIs, databases
- **Best Practices**: Code quality, testing, documentation

### 🔬 Research & Analysis
- Research methodology design
- Data collection and analysis
- Statistical methods
- Academic writing guidance
- Literature review assistance
- Experimental design

## 🔧 Extending the Agent

The agent is designed to be easily extensible:

### Adding New Knowledge Areas
```python
def get_custom_advice(self, query: str) -> str:
    """Add your custom knowledge area."""
    # Implement your specialized knowledge
    return "Your custom response"
```

### Integrating External APIs
```python
# Add API integrations in the process_query method
if "weather" in user_input_lower:
    response = self.get_weather_info(user_input)
```

### Custom Configuration
Create new config files for different use cases:
- `agriculture_config.json` - Agriculture-focused setup
- `research_config.json` - Research-oriented configuration
- `programming_config.json` - Development-focused settings

## 📊 Project Structure

```
praneethhh18/
├── ai_agent.py           # Main agent implementation
├── config.json           # Configuration settings
├── requirements.txt      # Dependencies (optional)
├── AGENT_README.md      # This documentation
└── README.md            # Profile README
```

## 🧪 Testing the Agent

### Test Agriculture Knowledge
```bash
python ai_agent.py --query "Tell me about crop diseases"
```

### Test Programming Help
```bash
python ai_agent.py --query "Help with Python machine learning"
```

### Test Research Assistance
```bash
python ai_agent.py --query "Research methodology guidance"
```

### Interactive Testing
```bash
python ai_agent.py
# Then type: help
```

## 🔮 Future Enhancements

Potential areas for expansion:

- **🌐 Web Interface**: Flask/FastAPI web app
- **🗄️ Database Integration**: Store conversation history
- **🔗 API Integration**: Weather, news, external data sources
- **🎙️ Voice Interface**: Speech-to-text and text-to-speech
- **📱 Mobile App**: Flutter or React Native app
- **🤖 Advanced AI**: Integration with GPT/Claude APIs
- **📊 Analytics**: Usage statistics and insights
- **🔐 Authentication**: User accounts and personalization

## 🤝 Contributing

This is Praneeth's personal project, but suggestions and improvements are welcome:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📄 License

This project is open source and available under the MIT License.

## 📞 Contact

**Praneeth P K**
- 🔗 LinkedIn: [praneeth-p-k-0792632ba](https://www.linkedin.com/in/praneeth-p-k-0792632ba/)
- 📧 Email: praneethhh0218@gmail.com
- 📱 WhatsApp: [+91 9483240597](https://wa.me/919483240597)
- 📸 Instagram: [@praneethhh.___](https://www.instagram.com/praneethhh.___)

---

> "Building intelligent solutions for real-world problems" - Praneeth P K

## 🏷️ Tags

`ai` `machine-learning` `agriculture` `research` `python` `assistant` `chatbot` `automation` `farming` `programming-help`