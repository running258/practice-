import requests

r = requests.post("https://vhsupply.staging.viewchain.net/api1/auth/login",data = {'identifier':'zhangleyuantest01', 'password':'zhangleyuantest01'})

print(r.text)
# print(r.text["token"])
# print(r.text["status"])
# print(f"token is {r}")