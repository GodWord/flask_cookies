import logging

from flask import Flask, request

from models.cookie import Cookie
from utils.db_utils import DBUtils

logger = logging.getLogger('cookies')

app = Flask(__name__)
app.debug = False


@app.route('/push_cookie', methods=['GET', 'POST'])
def push_cookie():
    if request.method == 'GET':
        try:
            data = dict(request.args)
            data['is_mobile'] = eval(data['is_mobile'])
            DBUtils.save_to_db(Cookie, data)
        except Exception as e:
            logger.error(e)
    return ''


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    return 'hello world!'


if __name__ == '__main__':
    app.run()
