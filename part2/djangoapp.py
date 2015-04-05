import sys
sys.path.insert(0, './helloworld')
from helloworld import wsgi


app = wsgi.application
