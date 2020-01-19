import time
from datetime import datetime

from websocket_server import WebsocketServer


def new_client(client, server):
    server.send_message(client, f'Hello {client["id"]}')


def message_received(client, server, message):
    while True:
        server.send_message(client, f'{datetime.now()}')
        time.sleep(1)


def client_left(client, server):
    print(f'connection closed: {client["id"]}')


if __name__ == '__main__':
    server = WebsocketServer(9999, host='localhost')
    server.set_fn_new_client(new_client)
    server.set_fn_message_received(message_received)
    server.set_fn_client_left(client_left)

    server.run_forever()
