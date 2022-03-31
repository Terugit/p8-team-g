from flask import Flask, request, render_template, url_for
import joblib
import base64
import json
import pprint
import requests
import os

def getName(label):
    print(label)
    if  label == 'anger':
        return '怒り'
    elif label == 'disgust':
        return '不快'
    elif label == 'fear':
        return '恐怖'
    elif label == 'happiness':
        return '幸せ'
    elif label == 'neutral':
        return 'ニュートラル'
    elif label == 'sadness':
        return '悲しみ'
    elif label == 'surprise':
        return '驚き'
    else:
        return 'Error'

app = Flask(__name__)

@app.route("/")
def index_form():
    return render_template("index.html")

@app.route("/result", methods=["GET", "POST"])
def request_form():
    if request.method == "POST":
        file_path = os.path.abspath(request.files["img"].value)
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
        dic = json_dict['faces'][0]['attributes']['emotion']
        max_dict=max(dic)
        emotion_ = getName(max_dict)

        return render_template("result.html", emotion=emotion_)
    else:
        return render_template("result.html", emotion=emotion_)


if __name__ == "__main__":
    app.run(debug=True)