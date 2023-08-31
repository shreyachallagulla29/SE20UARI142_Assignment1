from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/messages', methods=['POST'])
def handle_received_message():
    received_data = request.json
    received_message = received_data.get('message', '')
    print(f"Received message: {received_message}")
    response_data = {"status": "Message received!"}
    return jsonify(response_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
