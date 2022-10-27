from aiohttp import web

async def root(request):
    return web.Response(text='It\'s worked!')
