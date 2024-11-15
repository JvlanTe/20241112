from flask import Flask, render_template, jsonify

app = Flask(__name__)

count = 0


@app.route("/")
def index():
    global count
    # globalとはなんだった
    return render_template("index.html", count=count)


@app.route("/increment", methods=["POST"])
def increment():
    global count
    count += 1  # count - count + 1
    return jsonify({"counter": count})


@app.route("/get_json_data")
def get_data():
    data = {
        "name": "PLOT",
        "age": 20,
        "is_student": True,
    }
    return jsonify(data)


@app.route("/decrement", methods=["POST"])
def decrement():
    global count
    count -= 1
    return jsonify({"counter": count})


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)

# fapp
