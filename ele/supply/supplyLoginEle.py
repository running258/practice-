class supplyLoginEle(object):

    def __init__(self):
        
        self._userName = "//input[@id='viewhigh-login-username-input']"
        self._password = "//input[@id='viewhigh-login-pwd-input']"
        self._loginButton = "//button[@id='viewhigh-login-login-btn']"

    def userName(self):
        return str(self._userName)
    
    def passWord(self):
        return str(self._password)
    
    def loginButton(self):
        return str(self._loginButton)