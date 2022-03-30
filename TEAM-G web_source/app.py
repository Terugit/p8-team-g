from flask import Flask, request, render_template, url_for

app = Flask(__name__)

@app.route('/')
def result():
    return render_template('result.html', emotion="不快")
if __name__ == '__main__':
    app.run(debug=True)