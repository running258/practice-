import os
from yaml import load

class yamlFile(object):

    def __init__(self,path='ele'):
        self.fileRoot = os.path.abspath('.')+'\\'+path

    def readYamlFile(self,fileName):
        with open(self.fileRoot+fileName,'r') as _yamlFile:
            return load(_yamlFile)