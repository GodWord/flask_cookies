# -*- coding:utf-8 -*-
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


DB_SOURCE = {
    'default': r'mysql+pymysql://root:admin@127.0.0.1:3306/dzdp_db?charset=utf8mb4',
}



