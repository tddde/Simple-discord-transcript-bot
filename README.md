# Simple Discord Transcript Bot

This is a simple Discord bot that generates channel transcripts using `chat_exporter` and sends them as HTML files.

## Features
- Export a text channel's transcript using `+transcript`.
- Supports exporting the current channel if none is specified.
- Sends the transcript as an HTML file.

## Requirements
- Python 3.8+
- `discord.py` and `chat_exporter`

## Installation
1. Clone this repository.
2. Install dependencies:
   ```sh
   pip install discord.py chat_exporter
   ```
3. Set your bot token in the script.
4. Run the bot:
   ```sh
   python bot.py
   ```

## Usage
- Use `+transcript]` to generate a transcript.

## Permissions
- The bot requires `Read Message History` and `Manage Messages` permissions.
- The `!transcript` command is restricted to administrators.


