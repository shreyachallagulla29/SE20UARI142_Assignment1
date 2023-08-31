import requests

def send_message_to_server(message):
    url = 'http://SERVER_IP:5000/api/messages'
    data = {'message': message}
    response = requests.post(url, json=data)
    return response.json()

if __name__ == '__main__':
    while True:
        message = input("Enter a message to send to the server (or 'exit' to quit): ")
        if message.lower() == 'exit':
            break
        server_response = send_message_to_server(message)
        print("Server response:", server_response)
