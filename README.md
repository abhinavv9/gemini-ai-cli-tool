# Gemini CLI Tool

A simple Command Line Interface (CLI) tool to interact with Google's Gemini AI models.

## Features

*   Send prompts to Gemini AI models.
*   Specify which Gemini model to use.
*   Easy to use from the terminal.

## Prerequisites

*   Python 3.7+
*   A Google Cloud account with billing enabled.
*   A Google Cloud API key for Gemini.

## Setup

1.  **Clone the repository:**
    ```bash
    git clone <your_repository_url>
    cd gemini-cli-project
    ```
    (If you are not cloning, create the `gemini-cli-project` directory as described in the tutorial.)

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3.  **Install dependencies:**
    ```bash
    pip install google-generativeai
    ```

4.  **Set your API Key:**
    Set your Google Cloud API key as an environment variable named `GOOGLE_API_KEY`.
    ```bash
    export GOOGLE_API_KEY='YOUR_API_KEY' # Replace with your actual API key
    ```
    For permanent storage, add this to your shell's profile file (e.g., `.bashrc`, `.zshrc`).

## Usage

Make the `gemini_cli.py` script executable:

```bash
chmod +x src/gemini_cli.py
```

Run the CLI tool with your prompt:

```bash
./src/gemini_cli.py "Your prompt here."
```

**Examples:**

*   **Basic usage:**
    ```bash
    ./src/gemini_cli.py "Tell me a joke."
    ```

*   **Specify a model:**
    ```bash
    ./src/gemini_cli.py "What is the weather like today?" -m gemini-1.0-pro
    ```

## File Structure

```
gemini-cli-project/
├── src/
│   ├── gemini_api.py
│   └── gemini_cli.py
└── README.md
```
