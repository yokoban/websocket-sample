import threading
import time

import websocket

ZKILLBOARD_WEBSOCKET = 'ws://localhost:9999'
ZKILLBOARD_SEND_MESSAGE = '{"action":"sub","channel":"test"}'

def main(url, send_message):
    try:
        print('ws start')
        ws = websocket.create_connection(url)
        ws.send(send_message)

        while True:
            result = ws.recv()
            print(f'recv message\n {result}\n')
    except KeyboardInterrupt:
        print('ws end')
    finally:
        ws.close()
        print('ws close')


if __name__ == '__main__':
    main(ZKILLBOARD_WEBSOCKET, ZKILLBOARD_SEND_MESSAGE)
