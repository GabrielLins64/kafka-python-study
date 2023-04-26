import socketio
from time import sleep


HOST = 'localhost'
PORT = 6464

sio = socketio.Client()
waiting_for_server_response = False

@sio.event
def connect():
    print("Connection established")

@sio.event
def disconnect():
    print("Disconnected from server")

@sio.event
def server_response(data):
    global waiting_for_server_response
    print("Server msg received!")
    print(f"\tdata: {data}")
    waiting_for_server_response = False

if __name__ == '__main__':
    sio.connect(f"http://{HOST}:{PORT}")

    while True:
        user_input = input("Send a message to the server:")

        waiting_for_server_response = True
        sio.emit('my_message', {'message': user_input})

        while(waiting_for_server_response):
            sleep(0.5)
