from flask import Flask, jsonify, request
app = Flask(__name__)

FILE = ""


@app.route("/")
def home():
    resp = {}
    resp["success"] = True
    result_arr = []
    phrase = request.args.get('phrase')
    print phrase
    with open(FILE, "r") as f:
        searchlines = f.readlines()
    for i, line in enumerate(searchlines):
        if phrase in line:
            result_arr.append([i, line])
    resp["result"] = result_arr
    return jsonify(resp)

if __name__ == '__main__':
    app.run(debug=True)
