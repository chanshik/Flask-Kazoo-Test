from flask import Flask
from flask.ext.kazoo import Kazoo, kazoo_client

app = Flask(__name__)
kz = Kazoo(app)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/zk')
def zk():
    root_items = kazoo_client.get_children("/")

    return "<BR>".join(root_items)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
