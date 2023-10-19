from waitress import serve

from flask import Flask, request

app = Flask(__name__)


@app.route("/", methods=["POST"])
def send_locus():
    print(request.get_json()["id"])
    return {"status": True}


if __name__ == "__main__":
    # app.run()
    serve(app, host="0.0.0.0", port=5000)
