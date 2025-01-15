# Telegram PayPal Bot

This project is a Telegram bot that notifies you of incoming payments from PayPal. It listens to PayPal Webhooks and sends the payment information, such as the payer's email and the payment amount, to a Telegram chat.

## Requirements

- Python 3.8 or higher
- Libraries: `Flask`, `python-telegram-bot`, `requests`

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/telegram-paypal-bot.git
   cd telegram-paypal-bot
   ```

2. Create a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On macOS or Linux
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Set up your Telegram bot:

   - Create a bot on Telegram using BotFather and get the token.
   - Save the token and chat ID in the `bot/config.py` file (instructions below).

5. Set up PayPal webhook:

   - Go to PayPal Developer Portal and create a webhook for payment notifications.
   - Use the URL `http://your-server-url/paypal-webhook` to receive events.

6. Run the application:
   ```bash
   python main.py
   ```

## Features

- Receives payment notifications from PayPal in real time.
- Sends payment details to a specified Telegram chat.
- Supports incoming payments with payer email and amount.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.
