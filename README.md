# DeepInfra Chatbot Streamlit App

## Overview

This Streamlit application creates a simple chatbot interface using the OpenAI API accessed through DeepInfra. It allows users to interact with a specified language model and displays the conversation history in a black and white theme.

## Features

*   **Chat Interface:** A Streamlit-based chat interface for interacting with the language model.
*   **DeepInfra Integration:** Utilizes the DeepInfra API to access OpenAI language models.
*   **Conversation History:** Maintains and displays the history of the conversation within the session.
*   **Black and White Theme:** The interface is styled with a black background and white text for a clean look.
*   **Environment Variable Configuration:** Configures API keys and model name using environment variables for security and flexibility.

## Technologies Used

*   **Streamlit:** For creating the user interface.
*   **openai:** For interacting with the OpenAI API (via DeepInfra).
*   **python-dotenv:** For loading API keys from a `.env` file.

## Prerequisites

1.  **Python:** Make sure you have Python 3.7+ installed.
2.  **DeepInfra API Key:** You will need an API key from DeepInfra.
3.  **Environment Variables:** You need to set `DEEPINFRA_API_KEY`, `DEEPINFRA_BASE_URL`, and `MODEL_NAME` environment variables.

## Installation

1.  **Clone the repository:**
    ```
    git clone https://github.com/Zakaria-Boukeffa/Chatbot-LLM.git
    cd Chatbot-LLM
    ```

2.  **Create a virtual environment (recommended):**
    ```
    python -m venv venv
    source venv/bin/activate   # On Linux/macOS
    venv\Scripts\activate.bat  # On Windows
    ```

3.  **Install the dependencies:**
    ```
    pip install -r requirements.txt
    ```

4.  **Create a `.env` file:**
    Create a `.env` file in the root directory of the project and add your DeepInfra API key and model name:
    ```
    DEEPINFRA_API_KEY=YOUR_DEEPINFRA_API_KEY
    DEEPINFRA_BASE_URL=https://api.deepinfra.com/v1/openai
    MODEL_NAME=mistralai/Mistral-Small-24B-Instruct-2501
    ```
    Replace `YOUR_DEEPINFRA_API_KEY` with your actual API key. Never commit your `.env` file to a public repository.

## Usage

1.  **Run the Streamlit application:**
    ```
    streamlit run chatbot.py.py
    ```

2.  **Access the application in your web browser.** Streamlit will provide the URL (usually `http://localhost:8501`). The interface will have a black background with white text.

3.  **Enter your prompt** in the chat input box and press Enter.

4.  **View the response** from the chatbot, along with the conversation history, all displayed in the black and white theme.

## File Structure

*   `chatbot.py`: Main Streamlit application script.
*   `requirements.txt`: List of Python dependencies.
*   `.env`: File containing environment variables (API keys, model name).
