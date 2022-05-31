from flask import Flask, jsonify
from utils import get_object

app = Flask(__name__)


@app.route('/<itemid>')
def object_info(itemid):
    return jsonify(get_object(itemid))


if __name__ == '__main__':
    app.run()
