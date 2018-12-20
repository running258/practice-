class hospitalLoginEle(object):

    def __init__(self):
        
        self._userName = "//form[@class='el-form login-form login-form2']//input[@placeholder='请输入用户名']"
        self._password = "//input[@placeholder='请输入密码']"
        self._loginButton = "//form[@class='el-form login-form login-form2']//button[@type='button']"

    def userName(self):
        return str(self._userName)
    
    def passWord(self):
        return str(self._password)
    
    def loginButton(self):
        return str(self._loginButton)