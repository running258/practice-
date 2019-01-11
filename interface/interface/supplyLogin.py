import requests
import json

class supplyInit(object):

    def supplyLogin(self, userName, passWord, env="staging"):
        if env == "text":
            _url = "https://vhsupply.text.viewchain.net/api1/auth/login"
        elif env == "staging":
            _url = "https://vhsupply.staging.viewchain.net/api1/auth/login"
        elif env == "demo":
            _url = "https://vhsupply.demo.viewchain.net/api1/auth/login"
        else:
            raise EnvironmentError

        r = requests.post(_url,data = {'identifier':userName, 'password':passWord})
        res = json.loads(r.text)
        token = res["result"]["token"]
        return token

