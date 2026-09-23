# 🤖 AK — Personal AI Assistant

> A full-stack AI chatbot web application built with Python and deployed on Hugging Face Spaces.

---

## 🌐 Live Demo

👉 [https://huggingface.co/spaces/akashkomuravelli/ak-chatbot](https://huggingface.co/spaces/akashkomuravelli/ak-chatbot)

---

## 📖 About

AK is a personal AI assistant chatbot built from scratch using Python (Flask) on the backend and pure HTML/CSS/JavaScript on the frontend. It uses the Groq API with the LLaMA 3.3 70B model to deliver fast, intelligent responses. The app is containerized with Docker and hosted for free on Hugging Face Spaces.

---

## ✨ Features

### 🧠 AI & Conversation
- Real-time streaming responses (word-by-word animation)
- Powered by **LLaMA 3.3 70B Versatile** via **Groq API**
- Conversation history with context memory
- Auto-generated follow-up questions after each reply
- Mood/confidence indicator on AI responses
- Quick reply chips (Yes / No / Tell me more / Explain differently)

### 🗣️ Voice
- 🎤 **Speech-to-Text** — speak your questions using Web Speech API
- 🔊 **Text-to-Speech** — AK reads replies aloud (voice responses)
- Multilingual voice recognition across 8 languages

### 🌍 Languages
Supports 8 languages with full UI and voice support:
`English` `Hindi` `Telugu` `French` `German` `Spanish` `Japanese` `Chinese`

### 📄 File Support
- **PDF Upload** — upload any PDF and ask questions about it
- **Image Upload** — share photos directly in chat
- PDF text extraction powered by **PyMuPDF**

### 💻 Code & Formatting
- Syntax highlighted code blocks via **Highlight.js**
- Line-by-line code animation while streaming
- Copy button on every code block
- Supports 30+ programming languages
- Bold, italic, headings, bullet points, tables, blockquotes

### 🎵 Music
- Integrated **Spotify Player** — search songs and embed playlists
- Quick genre buttons: Trending, Hindi, Telugu, Lofi, Workout, Pop
- Paste any Spotify track/playlist/album link to embed and play

### 💬 Chat Management
- Chat history saved in browser (localStorage)
- Multiple chat sessions with session switching
- New chat with auto-save of previous session
- Message search — find any message instantly
- Pin / star important messages
- Edit or delete sent messages
- Emoji reactions on any message
- Export chat as `.txt` or PDF

### 🎨 UI / UX
- Animated AK avatar with pulse ring and idle animation
- Dark / Light mode toggle
- Adjustable font size (A− / A+)
- Particle background animation with connecting lines
- Confetti on first message sent
- Scroll-to-bottom button with unread message badge
- Sidebar with chat history, settings, and pinned messages
- Copy button on every AI reply (hover to reveal)
- Long-press on messages to reveal Edit / Delete / Pin actions
- "2 min ago" style timestamps
- Fully responsive — works on mobile and desktop

### ⌨️ Keyboard Shortcuts
| Shortcut | Action |
|---|---|
| `/` | Focus message input |
| `Ctrl + K` | New chat |
| `Ctrl + F` | Search messages |
| `Ctrl + B` | Toggle sidebar |
| `Ctrl + =` | Increase font size |
| `Ctrl + -` | Decrease font size |
| `Esc` | Close all panels |

---

## 🛠️ Tech Stack

### Backend
| Technology | Purpose |
|---|---|
| Python 3.11 | Core language |
| Flask | Web framework & REST API |
| Gunicorn | Production WSGI server |
| PyMuPDF (fitz) | PDF reading & text extraction |
| Groq API | AI inference (ultra-fast) |
| LLaMA 3.3 70B | Large language model by Meta |

### Frontend
| Technology | Purpose |
|---|---|
| HTML5 / CSS3 | Structure & styling |
| Vanilla JavaScript | All interactivity (no frameworks) |
| Highlight.js | Code syntax highlighting |
| Web Speech API | Speech-to-text (microphone) |
| SpeechSynthesis API | Text-to-speech (voice replies) |
| Canvas API | Animated particle background |
| Canvas Confetti | Confetti animation |
| Spotify Embed API | In-app music player |
| localStorage | Chat history persistence |

### DevOps & Deployment
| Technology | Purpose |
|---|---|
| Docker | Containerization |
| Hugging Face Spaces | Free cloud hosting |
| GitHub | Version control |

---

## 🚀 Getting Started

### Prerequisites
- Python 3.11+
- A free [Groq API key](https://console.groq.com)

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/Akashkomuravelli/ak-chatbot.git
cd ak-chatbot

# 2. Install dependencies
pip install flask groq gunicorn PyMuPDF

# 3. Set your API key
set GROQ_API_KEY=your_api_key_here   # Windows
export GROQ_API_KEY=your_api_key_here # Mac/Linux

# 4. Run the app
python app.py
```

Then open `http://localhost:7860` in your browser.

### Docker

```bash
docker build -t ak-chatbot .
docker run -p 7860:7860 -e GROQ_API_KEY=your_key ak-chatbot
```

---

## 📁 Project Structure

```
ak-chatbot/
├── app.py              # Flask backend & API routes
├── requirements.txt    # Python dependencies
├── Dockerfile          # Docker configuration
├── README.md           # Project documentation
└── templates/
    └── index.html      # Full frontend (HTML + CSS + JS)
```

---

## 🔌 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Serve the chat UI |
| POST | `/chat` | Send message, get AI reply |
| POST | `/upload` | Upload PDF for Q&A |
| GET | `/health` | Health check |

---

## 📸 Screenshots

> AK running on desktop and mobile with dark mode, syntax highlighting, Spotify player, and sidebar chat history.

---

## 🧑‍💻 Author

**Akash Komuravelli**
- GitHub: [@Akashkomuravelli](https://github.com/Akashkomuravelli)
- Live App: [ak-chatbot on Hugging Face](https://huggingface.co/spaces/akashkomuravelli/ak-chatbot)

---

## 📄 License

MIT License — free to use, modify, and distribute.

---

## 🙏 Acknowledgements

- [Groq](https://groq.com) — for ultra-fast AI inference
- [Meta AI](https://ai.meta.com) — for the LLaMA 3.3 model
- [Hugging Face](https://huggingface.co) — for free hosting
- [Highlight.js](https://highlightjs.org) — for code syntax highlighting
- [Spotify](https://developer.spotify.com) — for the embed player API
