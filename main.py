from flask import Flask, request, jsonify
from bot.handlers import send_payment_notification
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

@app.route('/paypal-webhook', methods=['POST'])
def paypal_webhook():
    try:
        data = request.json
        app.logger.info(f"Received webhook data: {data}")

        if not data:
            return jsonify({"status": "failure", "message": "No data received"}), 400

        payer_email = data.get("payer_email")
        total_amount = data.get("payment_amount")

        if not payer_email or not total_amount:
            return jsonify({"status": "failure", "message": "Missing email or amount"}), 400

        app.logger.info(f"Payment received from: {payer_email}, Amount: {total_amount}")

        send_payment_notification(payer_email, total_amount)

        return jsonify({"status": "success"}), 200

    except Exception as e:
        app.logger.error(f"Error in webhook: {str(e)}")
        return jsonify({"status": "failure", "message": "Internal server error"}), 500

if __name__ == '__main__':
    app.run(port=5000)
