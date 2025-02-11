import sqlite3


class SQLighter:

    def __init__(self, database):
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()

    def select(self, user_id):
        with self.connection:
            result = self.cursor.execute('SELECT * FROM `user` WHERE `user_id` = ?', (user_id,)).fetchall()
            return result

    def insert(self, user_id, user_name, name):
        with self.connection:
            result = self.cursor.execute(
                "INSERT INTO `user` (`user_id`, `user_name`, `name`) VALUES(?,?,?)",
                (user_id, user_name, name)
            )
            return result

    def update(self, name, user, quantity):
        with self.connection:
            result = self.cursor.execute("UPDATE `bucket` SET `quantity` = ? WHERE `user` = ? AND `product_name` = ?",
                                         (quantity, user, name,)).fetchall()
            return result

    def delete(self, name, user):
        with self.connection:
            result = self.cursor.execute("DELETE FROM `bucket` WHERE `product_name` = ? AND `user` = ?",
                                         (name, user,)).fetchall()
            return result

if __name__ == '__main__':
    db = SQLighter('sqlite.db')