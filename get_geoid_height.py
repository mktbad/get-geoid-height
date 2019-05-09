from urllib.request import urlopen
import json
import argparse
geoid_api_baseurl = 'https://vldb.gsi.go.jp/sokuchi/surveycalc/geoid/calcgh/cgi/geoidcalc.pl?select=0&tanni=1&outputType=json'

def getGeoidHeight(latitude_degree:float, longitude_degree:float):
    req_url = geoid_api_baseurl + '&latitude='+str(latitude_degree)+'&longitude='+str(longitude_degree)
    print('Request URL:', req_url)
    with urlopen(req_url) as res:
        jsondata = json.loads(res.read().decode('utf-8'))
    
    if jsondata['OutputData']['geoidHeight'] == 'データの無効領域です':
        raise ValueError('無効な緯度経度が指定されました')
    
    return float(jsondata['OutputData']['geoidHeight'])

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='日本国内の緯度経度からジオイド高を出すスクリプト')

    parser.add_argument('latitude_degree')
    parser.add_argument('longitude_degree')

    args = parser.parse_args()
    lat = float(args.latitude_degree)
    lon = float(args.longitude_degree)
    print('geoid height:', getGeoidHeight(lat, lon))