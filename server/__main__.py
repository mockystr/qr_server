from aiohttp import web
from server.routes import setup_routes


def main():
    app = web.Application()
    setup_routes(app)
    web.run_app(app)


main()
