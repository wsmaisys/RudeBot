# RudeBot 😈

A sarcastic AI chatbot that adds a twist of humor to your conversations. Built for entertainment, RudeBot responds to your questions with witty, sarcastic remarks while still providing relevant information.

## 🎯 Features

- **Sarcastic Responses**: Get your answers served with a side of sass
- **Persistent Memory**: Maintains context throughout your conversation
- **Thread Management**: 
  - Save and reload conversations
  - Start new chat sessions
  - Switch between different chat threads
- **Real-time Streaming**: Watch RudeBot craft its snarky responses in real-time

## 🛠️ Technology Stack

- **[LangGraph](https://github.com/langchain-ai/langgraph)**: For conversation flow management
- **[Streamlit](https://streamlit.io/)**: Powers the interactive web interface
- **[Mistral AI](https://mistral.ai/)**: Drives the conversational AI capabilities

## 🏗️ Architecture

### Conversation Management
- Implements persistent memory to maintain context across conversations
- Unique thread IDs for each conversation
- Runtime storage of chat history
- Ability to reload and resume previous conversations

### User Interface
- Clean, VS Code-inspired dark theme
- Real-time response streaming
- Easy navigation between conversations
- Simple and intuitive chat interface

## ⚠️ Disclaimer

RudeBot is created purely for entertainment purposes. Its responses are intentionally sarcastic and should not be taken personally. The bot's attitude is part of its charm!

## 🚀 Getting Started

### Local Installation

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   streamlit run streamlit_frontend.py
   ```

### Docker Deployment

1. Build the Docker image:
   ```bash
   docker build -t rudebot .
   ```
2. Run the container:
   ```bash
   docker run -p 8501:8501 rudebot
   ```
3. Access the application at `http://localhost:8501`

## 💭 Usage

1. Start a new chat using the "🔄 New Chat" button
2. Type your message in the chat input
3. Watch as RudeBot responds with its signature sass
4. Access previous conversations from the sidebar
5. Switch between different chat threads as needed

## 🤝 Contributing

Feel free to contribute to this project by:
- Adding new features
- Improving the response quality
- Enhancing the UI/UX
- Fixing bugs

## 📝 License

This project is open-source and available for personal use.

---

*Remember: RudeBot's sass is a feature, not a bug! 😉*