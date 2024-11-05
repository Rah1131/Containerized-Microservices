from flask import Flask, jsonify
import os
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

@app.route('/transaction', methods=['GET'])
def get_transactions():
    app.logger.info("Transaction endpoint accessed")
    return jsonify({"message": "Transaction service is up!"})

if __name__ == '__main__':
    app_port = int(os.environ.get('PORT', 8082))
    app.run(host='0.0.0.0', port=app_port)
