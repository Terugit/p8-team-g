#①モジュールをインポートする
import requests
import base64
import json
import pprint

#②画像ファイルの読み込み
file_path = "C:/Users/ktais/Documents/HaitLab/p8-team-g/learning/data/idpic2023.jpeg"
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