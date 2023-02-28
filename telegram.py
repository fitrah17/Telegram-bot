#!/usr/bin/python

import openai
import telebot

# Set the API key
openai.api_key = "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"

# Create a Telegram bot
bot = telebot.TeleBot("5895661527:AAEbKVj0pcrmAQZI4aLyXMhAJ-E72mbfhAk")


# Handle the '/generate' command
@bot.message_handler(commands=['search'])
def generate_text(message):
  # Get user input
  text = message.text[10:]

  # Send request to OpenAI API
  response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=text,
    max_tokens=100,
  )

  # Send response back to Telegram
  response_text = response.choices[0].text
  bot.send_message(chat_id=message.chat.id, text=response_text)


# Start the bot
bot.polling(none_stop=True)
