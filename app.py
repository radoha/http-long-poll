# Server (app.py)
from flask import Flask, Response
import time

app = Flask(__name__)

@app.route('/long-poll')
def long_poll():
    def generate():
        start_time = time.time()
        while time.time() - start_time < 900:  # 15 minutes = 900 seconds
            yield f"Data: {time.time()}\n\n"
            time.sleep(10)  # Send data every 10 seconds
    return Response(generate(), content_type='text/event-stream')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
