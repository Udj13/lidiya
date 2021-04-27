import sqlite3
import logging


# CREATE TABLE Posts (
#     num       INTEGER PRIMARY KEY AUTOINCREMENT,
#     post_id   INTEGER,
#     post_date INTEGER
# );


class Post:
    # post_id: int
    # post_date: int
    # post_text: str
    # group_link: str

    def __init__(self, post_id, post_date, post_text, group_link):
        self.post_id = post_id
        self.post_date = post_date
        self.post_text = post_text
        self.group_link = group_link


class Storage:
    db = None
    cur = None

    def __init__(self):
        self.db = sqlite3.connect('lida.db')
        self.cur = self.db.cursor()
        logging.basicConfig(level=logging.INFO, filename='lida-bot.log',
                            format='%(asctime)s %(filename)s %(levelname)s:%(message)s')

    def close(self):
        self.db.commit()
        self.db.close()

    def check_and_storage_post(self, post: Post):
        result = False

        try:
            self.cur.execute(f"SELECT * FROM Posts WHERE post_id={post.post_id} and post_date={post.post_date}")

            if self.cur.fetchone() is None:
                self.cur.execute(
                    f"INSERT INTO Posts (post_id, post_date) VALUES ('{post.post_id}', '{post.post_date}')"
                )
                self.db.commit()
                result = True

        except Exception as err:
            logging.error(f"Ошибка при попытке работы с базой: {str(err)}")

        return result
