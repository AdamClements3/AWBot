# AWBot

## Basic Concept
AWBot is an AI chatbot that mimics Albert Wesker from the Resident Evil games. I have a friend who wanted a bot that would just send a message every Wednesday at midnight reminding us that the week was halfway over. I figured that I would build a relatively simple discord bot that would just check the current day of the week once a minute, and if it was Wednesday, send the message and sleep for 24 hours.

## AI Integration
A month or so later, I found out that I had gotten developer access to the GPT API and I thought this bot would be the perfect candidate to get retrofitted with AI Chat capabilities. I reworked the system, and now any member of our discord server can send messages that wil be responded to by AI that mimic Albert Wesker.

## Hosting
As far as hosting is concerned, I don't really want to spend money to keep the bot online, so the solution I came up with was to build a very basic web server with Flask to keep my repl.it instance "alive" and effectively host the bot for free. While inconsistent, it works well enough for our purposes. https://replit.com/@AdamClements1/AWBot#main.py

## Updates
Oct 17 2023: Now has AI Chat Integration

Nov 8 2023: Bot now takes into account the existence of Daylight Savings

## Details
This project mainly uses
- Discord.py - API used for running a bot in a Discord Server
- Flask - Used to host a simple web server to keep the bot running
- OpenAI API - Used to request an AI response from GPT-3.5 (same version of GPT that ChatGPT uses)

  ![WW](https://github.com/AdamClements3/AWBot/assets/12504752/f04b7737-e39d-462c-a2bc-70e089b4ec84)
