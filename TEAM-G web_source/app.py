from flask import Flask, request, render_template, url_for
import joblib
import base64
import json
import pprint
import requests


app = Flask(__name__)

@app.route("/")
def index_form():
    return render_template("index.html")

@app.route("/result", methods=["GET", "POST"])
def request_form():
    if request.method == "POST":
        file_path =request.files["img"]
        with open(file_path, 'rb') as f:
          img_file = base64.encodebytes(f.read())

        #③「Face++」に対してリクエストを送る
        endpoint = 'https://api-us.faceplusplus.com'
        response = requests.post(
          endpoint + '/facepp/v3/detect',
          {
              'api_key': "FXNMgLAih_VOGjThYLLnvTsPkDghjfL3",
              'api_secret': "XNlaFLNVyVQVq25wiXqLeUpqjk7ByJo4",
              'image_base64': img_file,
              'return_attributes': 'emotion'
          }
        )

        #④リクエストに対して返ってきた結果を出力する
        json_dict = json.loads(response.text)
        pprint.pprint(json_dict['faces'][0]['attributes']['emotion'])

        return render_template("result.html", emotion="不快")
    else:
        return render_template("result.html", emotion="不快")


if __name__ == "__main__":
    app.run(debug=True)