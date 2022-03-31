from flask import Flask, request, render_template, url_for

app = Flask(__name__)

@app.route("/")
def index_form():
    return render_template("index.html")

@app.route("/result", methods=["GET", "POST"])
def request_form():
    if request.method == "POST":
        print(type(request.files["img"]))
        return render_template("result.html", emotion="不快")
    else:
        return render_template("result.html", emotion="不快")


if __name__ == "__main__":
    app.run(debug=True)