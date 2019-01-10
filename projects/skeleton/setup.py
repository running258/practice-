try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

 config = {
     "description" : "test project",
      "author" : "zly",
      "url" : "",
      "install_requires" : ["nose"]
 }

 setup(**config)