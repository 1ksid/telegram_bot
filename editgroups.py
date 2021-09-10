import sqlite3




class EDITgroup:

    def __init__(self, database):
        """Подключаемся к БД и сохраняем курсор соединения"""
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()


    def search_player(self, user_id):
        """Проверяем, есть ли уже юзер в базе"""
        with self.connection:
            result = self.cursor.execute('SELECT * FROM `allusers` WHERE `user_id` = ?', (user_id,)).fetchall()
            return bool(len(result))


    def check_kurva(self, user_id) -> str:
        """Проверяем kurva юзера в базе"""
        with self.connection:
            result = self.cursor.execute('SELECT `kurva` FROM `allusers` WHERE `user_id` = ?', (user_id,)).fetchall()
            user_kurva = result[0]
            return (user_kurva[0])


    def log_my_group(self, group):
        """Подсчет группы"""
        with self.connection:
            result1 = self.cursor.execute("SELECT COUNT(DISTINCT id) FROM `allusers` WHERE `group` = ?", (group,)).fetchall()
            result2 = self.cursor.execute("SELECT COUNT(DISTINCT id) FROM `allusers` WHERE `group` = ? AND `online` = 1", (group,)).fetchall()
            result3 = self.cursor.execute("SELECT COUNT(DISTINCT id) FROM `allusers` WHERE `group` = ? AND `online` = 0", (group,)).fetchall()    
            user_group1 = result1[0]
            user_group2 = result2[0]
            user_group3 = result3[0]
            return (f"Пользователей вступило в группу: {user_group1[0]}\n"
                f"Пользователей с уведомлениями: {user_group2[0]}\n"
                f"Пользователей без уведомлений: {user_group3[0]}\n")


    def set_zad1(self, theform, group_id):
        """редактирование zad1"""
        with self.connection:
            return self.cursor.execute("UPDATE `groups` SET `m_09` = ? WHERE `group_id` = ?", (theform, group_id))


    def set_zad2(self, theform, group_id):
        """редактирование zad2"""
        with self.connection:
            return self.cursor.execute("UPDATE `groups` SET `m_10` = ? WHERE `group_id` = ?", (theform, group_id))


    def set_zad3(self, theform, group_id):
        """редактирование zad3"""
        with self.connection:
            return self.cursor.execute("UPDATE `groups` SET `m_11` = ? WHERE `group_id` = ?", (theform, group_id))


    def set_zad4(self, theform, group_id):
        """редактирование zad4"""
        with self.connection:
            return self.cursor.execute("UPDATE `groups` SET `m_12` = ? WHERE `group_id` = ?", (theform, group_id))


    def set_ne1(self, theform, group_id):
        """редактирование ne1"""
        with self.connection:
            return self.cursor.execute("UPDATE `groups` SET `1_ne` = ? WHERE `group_id` = ?", (theform, group_id))


    def set_ne2(self, theform, group_id):
        """редактирование ne2"""
        with self.connection:
            return self.cursor.execute("UPDATE `groups` SET `2_ne` = ? WHERE `group_id` = ?", (theform, group_id))


    def set_ne3(self, theform, group_id):
        """редактирование ne3"""
        with self.connection:
            return self.cursor.execute("UPDATE `groups` SET `3_ne` = ? WHERE `group_id` = ?", (theform, group_id))


    def set_ne4(self, theform, group_id):
        """редактирование ne4"""
        with self.connection:
            return self.cursor.execute("UPDATE `groups` SET `4_ne` = ? WHERE `group_id` = ?", (theform, group_id))


    def set_ne5(self, theform, group_id):
        """редактирование ne5"""
        with self.connection:
            return self.cursor.execute("UPDATE `groups` SET `5_ne` = ? WHERE `group_id` = ?", (theform, group_id))


    def set_ne6(self, theform, group_id):
        """редактирование ne6"""
        with self.connection:
            return self.cursor.execute("UPDATE `groups` SET `6_ne` = ? WHERE `group_id` = ?", (theform, group_id))


    def set_ch1(self, theform, group_id):
        """редактирование ch1"""
        with self.connection:
            return self.cursor.execute("UPDATE `groups` SET `1_ch` = ? WHERE `group_id` = ?", (theform, group_id))


    def set_ch2(self, theform, group_id):
        """редактирование ch2"""
        with self.connection:
            return self.cursor.execute("UPDATE `groups` SET `2_ch` = ? WHERE `group_id` = ?", (theform, group_id))


    def set_ch3(self, theform, group_id):
        """редактирование ch3"""
        with self.connection:
            return self.cursor.execute("UPDATE `groups` SET `3_ch` = ? WHERE `group_id` = ?", (theform, group_id))


    def set_ch4(self, theform, group_id):
        """редактирование ch4"""
        with self.connection:
            return self.cursor.execute("UPDATE `groups` SET `4_ch` = ? WHERE `group_id` = ?", (theform, group_id))


    def set_ch5(self, theform, group_id):
        """редактирование ch5"""
        with self.connection:
            return self.cursor.execute("UPDATE `groups` SET `5_ch` = ? WHERE `group_id` = ?", (theform, group_id))


    def set_ch6(self, theform, group_id):
        """редактирование ch6"""
        with self.connection:
            return self.cursor.execute("UPDATE `groups` SET `6_ch` = ? WHERE `group_id` = ?", (theform, group_id))


    def close(self):
        """Закрываем соединение с БД"""
        self.connection.close()