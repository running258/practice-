import requests
import json

r = requests.post("https://vhsupply.staging.viewchain.net/api1/auth/login",data = {'identifier':'zhangleyuantest01', 'password':'zhangleyuantest01'})
res = json.loads(r.text)
token = res["result"]["token"]


