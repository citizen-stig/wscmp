from flask import Flask, render_template, abort
from jinja2.exceptions import TemplateNotFound

from constants import HTTP_WS_URL

app = Flask(__name__)
app.config['WS_SERVER'] = 'ws://echo.websocket.org'
WS_ENDPOINT = '127.0.0.1{url}'.format(url=HTTP_WS_URL)
app.config['HTTP_WS_SERVER'] = 'http://' + WS_ENDPOINT
app.config['WS_SERVER'] = 'ws://' + WS_ENDPOINT


LIBRARIES = (
    ('sockjs-client', 'sockjs-client'),
    ('Socket.io', 'Socket.io'),
    ('socket-cluster', 'socket cluster'),
    ('HTML5', 'HTML5 (native)')
)


@app.route("/")
def hello():
    return render_template('index.html', libraries=LIBRARIES)


@app.route('/clients/<string:library_name>')
def socket_client(library_name):
    try:
        return render_template(library_name + '.html')
    except TemplateNotFound:
        return abort(404)


if __name__ == "__main__":
    app.run()
