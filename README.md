# Discord-Ai-Text-Bot


This is a simple Discord bot connected to an AI (llama2) model.

# Table of Contents

1. [Description](#description)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Configuration](#configuration)
5. [License](#license)

## Description

This bot utilizes the llama2 AI model to provide responses to user queries on Discord. It's a fun and experimental project that showcases the integration of AI technology with chat platforms.

## Installation

1. Make sure you have Docker and Python 3.11 and poetry installed.

2. Clone this repository:
   ```bash
   git clone https://github.com/your-username/discord-ai-text-bot.git
   ```

3. Navigate to the project directory:
    ```bash
    cd discord-ai-text-bot
    ```

4. Install dependencies using Poetry:
    ```bash
    poetry install
    ```

5. Run the AI and bot using Docker Compose: 
    ```bash
    make run-ai
    ```

6. If its first time running ai, run this command to install llama2:
    ```bash
    make install-llama2
    ```

7. Run the discord bot:
    ```bash
    python main.py bot start
    ```

## Usage

Once the bot is running, you can interact with it on Discord. Here are some available commands:

-     !ask <question>: Ask the bot a question, and it will provide an AI-generated response.

## Configuration

Ensure you have the necessary value to variable on the Discord bot token var on first line of bot.py.

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.
