# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from sqlalchemy.orm import sessionmaker
from models import Article, db_connect
from scrapy.exceptions import DropItem


class MoumenteiPipeline(object):
    def __init__(self):
        """Initializes database connection and sessionmaker.

        Creates deals table.

        """
        engine = db_connect()
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        if item['content']:
            session = self.Session()
            article = Article(**item)

            try:
                session.add(article)
                session.commit()
            except:
                session.rollback()
                raise
            finally:
                session.close()
            return item
        else:
            raise DropItem("Missing content in %s" % item)