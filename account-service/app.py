from flask import Flask, jsonify
import os
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

@app.route('/account', methods=['GET'])
def get_accounts():
    app.logger.info("Account endpoint accessed")
    return jsonify({"message": "Account service is up!"})

if __name__ == '__main__':
    app_port = int(os.environ.get('PORT', 8081))
    app.run(host='0.0.0.0', port=app_port)