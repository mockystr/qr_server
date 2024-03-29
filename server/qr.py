import os
import datetime
import qrcode
import imgkit
from jinja2 import Environment, FileSystemLoader
from settings import save_path, BASE_DIR

env = Environment(loader=FileSystemLoader(searchpath=f"{BASE_DIR}/tmp"))


def create_qr(text_data: str):
    img = qrcode.make(text_data)
    qr_tmp_path = "{}/tmp{}_{}.jpg".format(save_path,
                                           datetime.datetime.now().strftime(
                                               '%H%M%S'),
                                           text_data[:10])
    img.save(qr_tmp_path)

    template = env.get_template("index.html")
    r = template.render(qr_code=os.path.join(BASE_DIR, qr_tmp_path))

    qr_final_path = '{}/{}_{}.png'.format(save_path,
                                          datetime.datetime.now().strftime(
                                              '%H%M%S'),
                                          text_data[:10])
    config = imgkit.config(wkhtmltoimage='/usr/local/bin/wkhtmltoimage')
    imgkit.from_string(r, qr_final_path, config=config,
                       options={'width': 420, 'height': 600})
    os.remove(qr_tmp_path)
    return qr_final_path
