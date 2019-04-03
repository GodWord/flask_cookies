# -*- coding:utf-8 -*-
import logging

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

from setting.setting import DB_SOURCE

logger = logging.getLogger('DBUtils')


class DBUtils:
    @staticmethod
    def get_session():
        """
        获取数据库session
        :return:session
        """
        # 根据setting配置获取session
        SessionCls = sessionmaker(
            bind=create_engine(DB_SOURCE['default'], pool_size=1000, pool_recycle=3600, echo=False, max_overflow=-1))
        New_SessionCls = scoped_session(SessionCls)
        session = New_SessionCls()
        return session

    @staticmethod
    def save_to_db(model, data):
        try:
            logger.info(data)
            # 获取session
            session = DBUtils.get_session()
            # 在session中添加数据

            session.add(model(**data))
            # commit(这里不提交数据库是不会保存的)
            session.commit()
        except Exception as e:
            logger.error(e)
            logger.error(data)

    @staticmethod
    def update(model, data, field='id'):
        logger.info('开始更新数据')
        session = DBUtils.get_session()
        if hasattr(model, field):
            list(map(lambda x: session.query(model).filter(getattr(model, field) == x[field]).update(x), data))
            session.commit()
        else:
            raise Exception('[%s]没有[%s]属性值' % (model.__name__, field))
