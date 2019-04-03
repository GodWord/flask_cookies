from flask import Flask, request

from models.cookie import Cookie
from utils.DBUtils import DBUtils

app = Flask(__name__)


@app.route('/push_cookie', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'GET':
        data = dict(request.args)
        print(data)
        DBUtils.save_to_db(Cookie, data)
    return ''


if __name__ == '__main__':
    app.run()
