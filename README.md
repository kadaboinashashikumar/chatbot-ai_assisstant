## Project Overview

This project is a Flask web application that allows users to interact with an AI-powered chat assistant. Users can input a task or question along with specific parameters such as persona, output format, style, detail level, and output size. The AI assistant generates a response based on these inputs using OpenAI's GPT-4 model.

## Features

- Customizable AI response based on user inputs (task, persona, format, style, detail level, size).
- A two-section interface: one for taking notes and another for interacting with the AI chat assistant.
- Ability to insert AI-generated responses directly into the notes section.
- Options to hide or display the chat section for a compact interface.

## Tech Stack

- **Backend**: Python, Flask, OpenAI API (GPT-4)
- **Frontend**: HTML, CSS (Bootstrap), JavaScript

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/laxmipreritha/T2T.git
   cd T2T
   ```

2. Set up a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```bash
   pip install Flask openai
   ```

4. Set up your OpenAI API key as an environment variable:
   ```bash
   export OPENAI_API_KEY='your_openai_api_key'
   ```

5. Run the Flask app:
   ```bash
   python app.py
   ```

6. Open a browser and navigate to `http://127.0.0.1:5000/` to use the application.

## API Endpoints

- **GET `/`**: Serves the main page of the AI Task Assistant application.
- **POST `/process_task`**: Processes the user inputs (task, persona, format, style, detail, size, additional instructions) and returns an AI-generated response.

## Usage

1. Fill out the task or question in the input field.
2. Select or input the persona, format, style, and detail level from the dropdown menus or enter a custom value.
3. Set the expected output size in words.
4. (Optional) Add any additional instructions.
5. Click on "Submit" to receive a response from the AI.
6. The generated response will be displayed in the chat section, and you can insert it into the notes section.
