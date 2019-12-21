from server.views import generate


def setup_routes(app):
    app.router.add_get('/generate', generate, name='generate')
