import eventlet
import socketio


HOST = '0.0.0.0'
PORT = 6464

sio = socketio.Server()

@sio.event
def connect(sid, environ, auth):
    print(f"Client {sid} connected")

@sio.event
def disconnect(sid):
    print(f"Client {sid} disconnected")

@sio.event
def my_message(sid, data):
    print("Received message!")
    print(f"\tSender: {sid}")
    print(f"\tData: {data}\n")
    sio.emit("server_response", "Message received!")

@sio.event
def my_response(sid, data):
    print("Received response!")
    print(f"\tSender: {sid}")
    print(f"\tData: {data}\n")

if __name__ == '__main__':
    app = socketio.WSGIApp(sio)
    print(f"Server listening to {HOST}:{PORT}...")
    eventlet.wsgi.server(eventlet.listen((HOST, PORT)), app, log=None, log_output=False)
