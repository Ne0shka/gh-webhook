from aiohttp import web

from routes import routes


def init_app():
    _routes = []

    for route in routes:
        if route.__name__ == 'root':
            _routes.append(web.get('/', route))
        else:
            _routes.append(web.get(f'/{route.__name__}', route))

    app = web.Application()
    app.add_routes(_routes)
    return app

if __name__ == '__main__':
    app = init_app()
    web.run_app(app)