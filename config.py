import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    PASSWORD = os.environ.get('PASSWORD') or 'fordbmsproject'
