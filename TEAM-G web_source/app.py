from flask import Flask, request, render_template, url_for
import joblib

def  predict(parameters):
    model = joblib.load('./nn.pkl')
    params = parameters.reshape(1,-1)
    pred = model.predict(params)
    return pred

def getName(label):
    print(label)
    if  label == 0:
        return 'Iris Setosa'
    elif label == 1:
        return 'Iris Versicolor'
    elif label == 2:
        return 'Iris Virginica'
    else:
        return 'Error'

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