# 🎤 AI Voice Sales Agent

An advanced AI-powered voice sales agent with RAG (Retrieval-Augmented Generation) capabilities for intelligent conversations about the "AI Mastery Bootcamp" course. Features both custom rule-based responses and AI-powered responses using real-time voice interaction.

## 🚀 Quick Start

1. **Install Python 3.8+** (Recommended: Python 3.11+)
2. **Clone and setup:**
   ```bash
   # Clone the repository
   git clone <repository-url>
   cd "voice sell ai agent"
   
   # Create virtual environment
   python -m venv venv
   venv\Scripts\activate  # On Windows
   
   # Install dependencies
   pip install -r requirements.txt
   ```
3. **Configure environment:**
   ```bash
   # Create .env file and add your API key
   echo GROQ_API_KEY=your_groq_api_key_here > .env
   ```
4. **Run the application:**
   ```bash
   start.bat
   # OR manually: python -m uvicorn main:app --host 0.0.0.0 --port 8000
   ```
5. **Open your browser:** http://localhost:8000

## ✨ Key Features

### 🎙️ Voice Interaction
- ✅ **Real-time Speech Recognition** - Google Speech Recognition with microphone input
- ✅ **Text-to-Speech** - Google TTS with high-quality audio playback
- ✅ **Voice Conversation Flow** - Complete voice-based customer interactions
- ✅ **Ambient Noise Adjustment** - Automatic microphone calibration

### 🤖 AI Intelligence
- ✅ **RAG System** - Retrieval-Augmented Generation with course knowledge base
- ✅ **Groq LLM Integration** - Fast, intelligent responses using Llama3-8b-8192
- ✅ **Custom Rule Engine** - Fallback system for consistent responses
- ✅ **Context Awareness** - Maintains conversation context throughout calls
- ✅ **Sentence Transformers** - High-quality text embeddings for semantic search

### 🔧 Technical Features
- ✅ **FastAPI Backend** - Modern, async REST API with automatic docs
- ✅ **Responsive Web Interface** - Clean, mobile-friendly UI
- ✅ **Real-time Conversation History** - Live chat display with timestamps
- ✅ **Mode Switching** - Toggle between RAG and custom response modes
- ✅ **Error Handling** - Robust error handling with user feedback
- ✅ **Health Monitoring** - RAG status endpoint and system diagnostics

### 🚀 Performance Features
- ✅ **Fast Response Times** - Sub-2 second response generation
- ✅ **Efficient Vector Search** - FAISS-powered semantic similarity
- ✅ **Concurrent Sessions** - Multiple simultaneous call support
- ✅ **Resource Optimization** - CPU-optimized embeddings model

## 🎯 How to Use

### 1. Start a Conversation
- Enter customer name and phone number
- Click **"Start Call"** to begin
- Agent automatically plays welcome message

### 2. Choose Response Mode
- **RAG Mode**: AI-powered responses using course knowledge
- **Custom Mode**: Rule-based responses for consistent messaging

### 3. Voice Interaction
- Click **"🎙️ Simulate Voice Response"**
- Allow microphone permissions when prompted
- Speak clearly when you see "🎙️ Speak now! Listening for 5 seconds..."
- System will show what you said and provide AI response

### 4. Text Interaction (Alternative)
- Type customer responses in the text input
- Click **"Send Response"** for text-based interaction
- Perfect for testing or when microphone isn't available

## 🗣️ Example Voice Interactions

**Customer can say:**
- "Tell me about the AI bootcamp"
- "What's the price?"
- "How long is the course?"
- "I'm interested but it's expensive"
- "I don't have time for this"
- "Not interested"
- "What topics are covered?"

**AI Agent responds intelligently with:**
- Course details and benefits
- Pricing and special offers
- Objection handling
- Lead qualification questions
- Natural conversation flow

## 🔧 API Endpoints

### Core Endpoints
```http
POST /start-call
{
  "customer_name": "John Doe",
  "phone_number": "+1234567890"
}

POST /respond/{call_id}           # Custom rule-based responses
POST /respond-rag/{call_id}       # RAG-powered responses
GET /simulate-call/{call_id}      # Voice input simulation
GET /conversation/{call_id}       # Get conversation history
GET /rag-status                   # Check RAG system status
```


## 🛠️ Technology Stack

### Backend
- **FastAPI** - Modern Python web framework
- **LangChain** - LLM application framework  
- **Groq** - Fast LLM inference (Llama3-8b-8192)
- **FAISS** - Vector similarity search
- **HuggingFace** - Embeddings and transformers
- **Sentence Transformers** - Text embeddings (all-MiniLM-L6-v2)

### Voice & Audio
- **Google Speech Recognition** - Speech-to-text
- **Google TTS (gTTS)** - Text-to-speech
- **PyAudio** - Microphone access
- **Pygame** - Audio playback

### Frontend
- **Vanilla HTML/CSS/JS** - Responsive web interface
- **Real-time updates** - Dynamic conversation display
- **Mobile-friendly** - Works on all devices

## 📦 Dependencies

### Core Dependencies
```txt
fastapi==0.104.1
uvicorn==0.24.0
langchain==0.1.0
langchain-community==0.0.10
langchain-text-splitters==0.0.1
langchain-groq==0.0.1
sentence-transformers==2.7.0
huggingface_hub==0.24.0
transformers==4.48.3
faiss-cpu==1.7.4
python-dotenv==1.0.0
```

### Voice Dependencies
```txt
gtts==2.4.0
speechrecognition==3.10.0
pygame==2.5.2
pyaudio==0.2.14
```

### Additional Requirements
```txt
pydantic==2.5.0
requests==2.31.0
python-multipart==0.0.6
```

## 🔧 Advanced Usage

### Environment Setup
```bash
# Create virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
copy .env.example .env  # Windows
cp .env.example .env    # Linux/Mac
# Add your GROQ_API_KEY to .env file
```

### Manual Server Start
```bash
# Method 1: Using uvicorn directly
python -m uvicorn main:app --host 0.0.0.0 --port 8000 --reload

# Method 2: Using the provided script
python main.py

# Method 3: Using start.bat (Windows)
start.bat
```

### Testing the System
```bash
# Test RAG system functionality
python test_rag.py

# Test API endpoints
python test_api.py

# Test voice service components
python test_voice_service.py

# Test voice simulation endpoints
python test_simulate.py

# Check server health
python check_server.py
```

### Verifying RAG System
```bash
# Check if sentence-transformers is working
python -c "from sentence_transformers import SentenceTransformer; print('✅ Success')"

# Test embeddings model loading
python -c "from sentence_transformers import SentenceTransformer; model = SentenceTransformer('all-MiniLM-L6-v2'); print('✅ Model loaded')"

# Test LLM service initialization
python -c "from llm_service import LLMService; service = LLMService(); print('RAG enabled:', service.rag_enabled)"
```

## 🔧 Configuration

## 📁 Project Structure

```
voice sell ai agent/
├── 📄 main.py                 # FastAPI application entry point
├── 📄 llm_service.py          # LLM and RAG system implementation
├── 📄 voice_service.py        # Voice recognition and TTS service
├── 📄 models.py               # Pydantic data models
├── 📄 index.html              # Web interface frontend
├── 📄 ai_bootcamp_info.txt    # Knowledge base for RAG system
├── 📄 requirements.txt        # Python dependencies
├── 📄 start.bat               # Windows startup script
├── 📄 .env                    # Environment variables (create from .env.example)
├── 🧪 test_api.py             # API endpoint tests
├── 🧪 test_rag.py             # RAG system functionality tests
├── 🧪 test_simulate.py        # Voice simulation tests
├── 🧪 test_voice_service.py   # Voice service tests
├── 🧪 check_server.py         # Server health check
└── 📂 venv/                   # Virtual environment (created after setup)
```

### Key Files Description

- **`main.py`**: FastAPI server with REST API endpoints for call management
- **`llm_service.py`**: Core AI logic with RAG system and fallback responses
- **`voice_service.py`**: Handles speech recognition and text-to-speech
- **`models.py`**: Data structures for API requests/responses
- **`index.html`**: Single-page web application for the user interface
- **`ai_bootcamp_info.txt`**: Course knowledge base used by RAG system
- **`requirements.txt`**: All Python package dependencies with versions
