# Coding Bot : Generating Programs

This is a simple coding bot that generates programmatic responses using an API. The bot takes user prompts, maintains a history of the conversation, and generates appropriate responses. The application is built using **Streamlit** and integrates with an API hosted locally (can be changed to a public URL).

## Features

- Text-based input for programming prompts.
- History management for prompts, creating a chain of conversations.
- API call to generate responses.
- Displays the generated responses in the Streamlit web app.

## Prerequisites

To run this application, you will need to have the following installed on your machine:

1. **Python 3.8 or higher**
2. **Streamlit**
3. **Requests library**
4. **Ollama** for running **Code Llama** models (required if using Code Llama as the language model).

### Setting up Ollama with Code Llama

You need to install **Ollama** and download **Code Llama** to run the model locally. Follow these steps:

1. **Download and install Ollama**:
   - You can download Ollama from the official site: [https://ollama.com](https://ollama.com).
   - Follow the installation instructions provided there.

2. **Download Code Llama** using Ollama:
   - After installing Ollama, download the Code Llama model by running the following command in your terminal:
     ```bash
     ollama pull codellama
     ```

3. **Start the Ollama API**:
   - Once the model is downloaded, start the API server:
     ```bash
     ollama serve
     ```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/code-bot.git
   cd code-bot
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Update the `url` variable in the `main.py` file to point to the correct API endpoint. If using Ollama locally:
   ```python
   url = "http://localhost:11434/api/generate"
   ```

## Running the App

1. Start the **Ollama** API server (if using Code Llama):
   ```bash
   ollama serve
   ```

2. Run the Streamlit app:
   ```bash
   streamlit run main.py
   ```

3. Open your browser and navigate to `http://localhost:8501` to access the Coding Bot.

## Usage

1. Enter your prompt in the text area.
2. Click the "Generate Response" button.
3. The bot will generate and display a response based on the input.

## Troubleshooting

- If you encounter connection errors, ensure that:
  - The API server is running at the URL specified in the code.
  - The correct port (default `11434`) is being used for the Ollama API.
  - Your system has access to the internet if using an external API.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

### `requirements.txt`

```txt
streamlit==1.24.0
requests==2.31.0
json
ollama  # for Code Llama
```

### Notes:
1. Make sure to modify the `url` variable in your `main.py` file to point to the correct API server (locally or a public one if hosted remotely).
2. The installation of Ollama and downloading the Code Llama model is necessary only if you're using Code Llama as the backend model.
3. If you host your API on a cloud service (e.g., Heroku or AWS), update the URL accordingly in the code.
