import requests
import json

class supplyInit(object):

    def supplyLogin(self, userName, passWord, env="staging"):
        if env == "text":
            _url = "https://vhsupply.text.viewchain.net"
        elif env == "staging":
            _url = "https://vhsupply.staging.viewchain.net"
        elif env == "demo":
            _url = "https://vhsupply.demo.viewchain.net"
        else:
            raise EnvironmentError

        _route_login = "/api1/auth/login"

        r = requests.post(_url+_route_login,data = {'identifier':userName, 'password':passWord})
        res = json.loads(r.text)
        authorization = res["result"]["token"]

        _route_getUserRes = "/api1/api/user/base/getUserRes"
        header = {"authorization":authorization}
        userRes = requests.get(_url+_route_getUserRes,headers=header)

        return authorization

