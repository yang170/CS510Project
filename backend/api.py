import flask
import bm25
import json
from flask import request, Response
from HttpStatus import Status


app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/ref', methods=['GET'])
def fetch_ref():
    text = request.args.get('text', None)  # query text
    size = request.args.get('size', 1)  # number of relevent docs to return

    if text is None:
        return Response(status=Status.bad_request())

    docs = bm25.rank(text, size)
    return Response(json.dumps(docs), status=Status.ok())


if __name__ == "__main__":
    # example request url: http://localhost:5000/ref?text=hi&size=2
    app.run(host='localhost', port=5000)
