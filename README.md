# Prompt-Driven Email Productivity Agent

An intelligent, prompt-driven email productivity agent capable of processing an inbox and performing automated tasks such as categorization, action-item extraction, and auto-drafting replies.

## Features

- **Inbox Ingestion**: Load and view emails from a mock inbox.
- **Prompt-Driven Architecture**: Customize the "brain" of the agent by editing prompts for categorization, extraction, and drafting.
- **Email Agent Chat**: Interact with your inbox using natural language (e.g., "Summarize this email", "Draft a reply").
- **Automated Processing**: Automatically categorize emails and extract action items using LLMs.
- **Draft Management**: Review, edit, and save generated email drafts.

## Setup Instructions

1.  **Clone the repository** (if not already done).
2.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
3.  **Configure API Key**:
    - Create a `.env` file in the root directory.
    - Add your Google Gemini API key:
      ```
      GEMINI_API_KEY=your_api_key_here
      ```
4.  **Run the Application**:
    ```bash
    streamlit run app.py
    ```

## Project Structure

- `app.py`: Main Streamlit application.
- `data/`: Contains mock inbox, prompts, and saved drafts.
- `services/`: Backend logic for LLM, email processing, and prompt management.
- `models/`: Data models for emails, prompts, and drafts.
- `utils/`: Helper functions.

## Usage

1.  **Inbox**: View your emails. Click "Process Inbox" to categorize them and extract tasks.
2.  **Prompt Brain**: Go to the "Prompt Brain" page to customize how the agent behaves.
3.  **Email Agent**: Use the chat interface to ask questions about specific emails or your inbox in general.
4.  **Drafts**: View and manage auto-generated drafts.

## Mock Inbox

The application loads a mock inbox from `data/mock_inbox.json` automatically. You can edit this file to test different email scenarios.
