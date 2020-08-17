import asyncio
import re
from proxybroker import Broker
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

prefix = input("Enter prefix (http://) or leave empty: ")

async def show(proxies):
    while True:
        proxy = await proxies.get()
        if proxy is None: break
        pl = re.search('(?<=] ).*?(?=>)', '%s' % proxy)
        print(prefix + pl.group(0))

proxies = asyncio.Queue()
broker = Broker(proxies)
tasks = asyncio.gather(
    broker.find(types=['HTTP', 'HTTPS'], limit=150),
    show(proxies))

loop = asyncio.get_event_loop()
loop.run_until_complete(tasks)
