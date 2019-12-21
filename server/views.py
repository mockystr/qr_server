import io
import os
import uuid

from aiohttp import web

from server.qr import create_qr


async def generate(request):
    qr_path = create_qr(uuid.uuid4().hex)
    with open(qr_path, 'rb') as f:
        img_bytes = f.read()
    os.remove(qr_path)
    return web.Response(body=img_bytes, content_type='image/jpeg')
