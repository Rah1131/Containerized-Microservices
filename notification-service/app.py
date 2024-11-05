from flask import Flask, jsonify
import os
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

@app.route('/notification', methods=['GET'])
def get_notifications():
    app.logger.info("Notification endpoint accessed")
    return jsonify({"message": "Notification service is up!"})

if __name__ == '__main__':
    app_port = int(os.environ.get('PORT', 8083))
    app.run(host='0.0.0.0', port=app_port)
