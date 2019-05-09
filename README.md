# get geoid height JP
日本の緯度経度からジオイド高を出してくれるスクリプト。
内部的な処理としては国土地理院のジオイド高計算サイトのcgiへGETパラメータを送信することでjsonを受け取っています。

## 必要なもの
- Python 3

## 使い方

### コマンドラインから実行する場合
以下のように緯度・経度の順で指定するとジオイド高を出してくれます

```get_geoid_commandline
$ python get_geoid_height.py 40.0 140.0
Request URL: https://vldb.gsi.go.jp/sokuchi/surveycalc/geoid/calcgh/cgi/geoidcalc.pl?select=0&tanni=1&outputType=json&latitude=40.0&longitude=140.0
geoid height: 37.8366
```

### インポートして外部スクリプトから使用する場合
以下のように使用します。

```get_geoid_import_sample.py
from get_geoid_height import getGeoidHeight

latitude = 40.0
longitude = 140.0
geoid_height = getGeoidHeight(latitude, longitude)

```

## ライセンス
MITライセンス。