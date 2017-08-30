' url handlers '
from coroweb import get


@get('/')
def hello():
    return '<h1>hello<h1>'

@get('/hello/{name}')
def hello(name):
    return '<h1>hello, '+name+'<h1>'