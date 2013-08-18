__author__ = 'peter'

import jieba
from sqlalchemy.orm import sessionmaker
from moumentei.models import Article, db_connect

class Stutter(object):
    def __init__(self):
        engine = db_connect()
        self.Session = sessionmaker(bind=engine)

    def segment(self):
        step=5000
        for offset in range(0, 1552492, step):
            session = self.Session()
            try:
                for article in session.query(Article).order_by(Article.id)[offset: step]:
                    article.segmented=jieba.cut(article.content)
                session.commit()
            except:
                session.rollback()
                raise
            finally:
                session.close()


if __name__ == "__main__":
    stutter = Stutter()
    stutter.segment()
