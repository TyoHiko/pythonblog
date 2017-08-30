import orm, asyncio
from models import User, Blog, Comment

@asyncio.coroutine
def test(loop):
    yield from orm.create_pool(loop = loop, user = 'root', password = '123456', db = 'awesome')
    u = User(name = 'Test', email = 'tttest6@example.com', passwd = '1234567890',image = 'about:blank')
    # yield from u.save()
    yield from u.findAll()

loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.close()