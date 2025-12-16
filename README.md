# Getting Started

This is a mini app for simple interaction with a Large Language Model using LangChain technologies like `create_agent`, `init_chat_model`, etc.

Main Goal: Learn how GitHub Actions works!

## Setup Instructions

1. Clone the repository
   ```bash
   git clone https://github.com/htsago/getting-started-github-actions
   cd getting-started-github-actions
   ```

2. Set up your API key
   - Rename the example environment file:
     ```bash
     mv env.example .env
     ```
   - Open `.env` and add your Groq API key:
     ```env
     GROQ_API_KEY=your_api_key_here
     ```

3. Set up Python virtual environment 
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

5. Run the app
   ```bash
   python3 -m uvicorn main:app --reload --host 0.0.0.0 --port 8888
   ```

The app will be available at: http://localhost:8888

## Notes
- Make sure you have Python 3.8+ installed.
- Never commit your `.env` file to version control! It is already in `.gitignore`.