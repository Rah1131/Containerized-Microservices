from flask import Flask, jsonify
import os
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

@app.route('/user', methods=['GET'])
def get_users():
    app.logger.info("User endpoint accessed")
    return jsonify({"message": "User service is up!"})

if __name__ == '__main__':
    app_port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=app_port)
