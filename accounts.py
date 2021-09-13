import sqlite3




class ALLusers:

    def __init__(self, database):
        """Подключаемся к БД и сохраняем курсор соединения"""
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()


    def search_player(self, user_id):
        """Проверяем, есть ли уже юзер в базе"""
        with self.connection:
            result = self.cursor.execute('SELECT * FROM `allusers` WHERE `user_id` = ?', (user_id,)).fetchall()
            return bool(len(result))


    def add_player(self, user_id, online = True):
        """Добавляем нового подписчика"""
        with self.connection:
            return self.cursor.execute("INSERT INTO `allusers` (`user_id`, 'online') VALUES(?,?)", (user_id,online))


    def update_online(self, user_id, online):
        """Обновляем статус подписки пользователя"""
        with self.connection:
            return self.cursor.execute("UPDATE `allusers` SET `online` = ? WHERE `user_id` = ?", (online, user_id))


    def check_week(self) -> str:
        """проверка недели"""
        with self.connection:
            result = self.cursor.execute('SELECT `week` FROM `settings` WHERE `num` = 1').fetchall()
            temp_answer = result[0]
            return (temp_answer[0])


    def full_check_week(self) -> str:
        """проверка недели"""
        with self.connection:
            result = self.cursor.execute('SELECT `week` FROM `settings` WHERE `num` = 1').fetchall()
            temp_answer = result[0]
            if temp_answer[0] == 0:
                return (f'Изменено: 🔵 нечетная неделя')
            else:
                return (f'Изменено: 🟡 четная неделя')


    def change_week(self, week):
        """Обновляем статус week"""
        with self.connection:
            return self.cursor.execute("UPDATE `settings` SET `week` = ?", (week,))


    def log_info(self):
        """Подсчет пользователей"""
        with self.connection:
            result = self.cursor.execute("SELECT COUNT(DISTINCT id) FROM `allusers`").fetchall()        
            how_id_users = result[0]
            return (f"Всего пользователей зарегистрировано: {how_id_users[0]}\n")


    def setgroup(self, user_id, group):
        """Обновляем статус группы пользователя"""
        with self.connection:
            if group == 0:
                my_group = '🌑 Ты вышел из группы'
            elif group == 1:
                my_group = '🌚 Выбрана группа И504Б'
            elif group == 2:
                my_group = '🌚 Выбрана группа И505Б'
            elif group == 3:
                my_group = '🌚 Выбрана группа И507Б'
            else:
                return (f'⚠️ Группа не найдена. Возможно она была удалена.')

            self.cursor.execute("UPDATE `allusers` SET `group` = ? WHERE `user_id` = ?", (group, user_id))
            return (f'{my_group}')


    def check_group(self, user_id) -> str:
        """Проверяем group юзера в базе"""
        with self.connection:
            result = self.cursor.execute('SELECT `group` FROM `allusers` WHERE `user_id` = ?', (user_id,)).fetchall()
            user_group = result[0]
            return (user_group[0])


    def check_group2(self, user_id) -> str:
        """Проверяем group юзера в базе"""
        with self.connection:
            result22 = self.cursor.execute('SELECT `kurva` FROM `allusers` WHERE `user_id` = ?', (user_id,)).fetchall()
            user_group2 = result22[0]

            if (user_group2[0] == 1):
                group2 = 'И504Б'
            elif (user_group2[0] == 2):
                group2 = 'И505Б'
            elif (user_group2[0] == 3):
                group2 = 'И507Б'
            else:
                group2 = '?'
            return (group2)


    def check_kurva(self, user_id) -> str:
        """Проверяем kurva юзера в базе"""
        with self.connection:
            result = self.cursor.execute('SELECT `kurva` FROM `allusers` WHERE `user_id` = ?', (user_id,)).fetchall()
            user_kurva = result[0]
            return (user_kurva[0])


    def settings_online(self, user_id):
        """Обновляем статус подписки пользователя"""
        with self.connection:
            result = self.cursor.execute('SELECT `online` FROM `allusers` WHERE `user_id` = ?', (user_id,)).fetchall()
            my_online = result[0]
            if my_online[0] == 0:
                self.cursor.execute("UPDATE `allusers` SET `online` = 1 WHERE `user_id` = ?", (user_id,))
                return (f'✅ Уведомления включены')
            elif my_online[0] == 1:
                self.cursor.execute("UPDATE `allusers` SET `online` = 0 WHERE `user_id` = ?", (user_id,))
                return (f'❌ Уведомления выключены')
            else:
                self.cursor.execute("UPDATE `allusers` SET `online` = 1 WHERE `user_id` = ?", (user_id,))
                return (f'✅ Уведомления включены')


    def settings_load(self, user_id) -> str:
        """загрузка настроек"""
        with self.connection:
            result = self.cursor.execute('SELECT `group` FROM `allusers` WHERE `user_id` = ?', (user_id,)).fetchall()
            your_group = result[0]

            result = self.cursor.execute('SELECT `online` FROM `allusers` WHERE `user_id` = ?', (user_id,)).fetchall()
            your_online = result[0]

            if (your_group[0] == 0):
                group = 'Группа не выбрана'
            elif (your_group[0] == 1):
                group = 'И504Б'
            elif (your_group[0] == 2):
                group = 'И505Б'
            elif (your_group[0] == 3):
                group = 'И507Б'
            else:
                group = '⚠️ Группа не найдена. Возможно она была удалена.'

            if (your_online[0] == 0):
                online = '❌ Уведомления выключены'
            elif (your_online[0] == 1):
                online = '✅ Уведомления включены'

            return (f"⚙️ Настройки:\n\n"
                f"👤 Моя группа: {group}\n"
                f"Изменение группы - /setgroup\n\n"
                f"💌 Включение/отключение уведомлений групп - /notifications\n"
                f"{online}\n\n\n"
                f"🌇 Дополнительно:\n\n"
                f"📒 Методички - /met\n"
                f"э̶т̶о̶ ̶п̶р̶а̶в̶д̶а̶ ̶н̶е̶ ̶м̶е̶т̶\n\n"
                f"🏳️‍🌈 Для кураторов - /mm")



    def check_id(self, user_id) -> str:
        """Проверяем id юзера в базе /my_id"""
        with self.connection:
            result = self.cursor.execute('SELECT `user_id` FROM `allusers` WHERE `user_id` = ?', (user_id,)).fetchall()
            player_id = result[0]
            return (f'Ваш TELEGRAM ID - {player_id[0]}')


    def load_met(self):
        """загрузка текста"""
        with self.connection:
            result = self.cursor.execute('SELECT `met` FROM `settings` WHERE `num` = 1').fetchall()
            send_met = result[0]
            return (f'📒 Методички:\n\n{send_met[0]}')


    def set_met(self, themet):
        """редактирование met"""
        with self.connection:
            return self.cursor.execute("UPDATE `settings` SET `met` = ? WHERE `num` = 1", (themet,))


    def load_m_09(self, group_id):
        """загрузка текста"""
        with self.connection:
            result = self.cursor.execute('SELECT `m_09` FROM `groups` WHERE `group_id` = ?', (group_id,)).fetchall()
            send = result[0]
            return (f'Задания на сентябрь:\n\n{send[0]}')


    def load_m_10(self, group_id):
        """загрузка текста"""
        with self.connection:
            result = self.cursor.execute('SELECT `m_10` FROM `groups` WHERE `group_id` = ?', (group_id,)).fetchall()
            send = result[0]
            return (f'Задания на октябрь:\n\n{send[0]}')


    def load_m_11(self, group_id):
        """загрузка текста"""
        with self.connection:
            result = self.cursor.execute('SELECT `m_11` FROM `groups` WHERE `group_id` = ?', (group_id,)).fetchall()
            send = result[0]
            return (f'Задания на ноябрь:\n\n{send[0]}')


    def load_m_12(self, group_id):
        """загрузка текста"""
        with self.connection:
            result = self.cursor.execute('SELECT `m_12` FROM `groups` WHERE `group_id` = ?', (group_id,)).fetchall()
            send = result[0]
            return (f'Задания на декабрь:\n\n{send[0]}')


    def load_m_42(self, group_id):
        """загрузка текста"""
        with self.connection:
            result1 = self.cursor.execute('SELECT `m_09` FROM `groups` WHERE `group_id` = ?', (group_id,)).fetchall()
            the_result1 = result1[0]
            result2 = self.cursor.execute('SELECT `m_10` FROM `groups` WHERE `group_id` = ?', (group_id,)).fetchall()
            the_result2 = result2[0]
            result3 = self.cursor.execute('SELECT `m_11` FROM `groups` WHERE `group_id` = ?', (group_id,)).fetchall()
            the_result3 = result3[0]
            result4 = self.cursor.execute('SELECT `m_12` FROM `groups` WHERE `group_id` = ?', (group_id,)).fetchall()
            the_result4 = result4[0]

            return (f"Все доступные задания:\n\n—————————\nНа сентябрь:\n\n{the_result1[0]}\n\n"
                f"—————————\nНа октябрь:\n\n{the_result2[0]}\n\n"
                f"—————————\nНа ноябрь:\n\n{the_result3[0]}\n\n"
                f"—————————\nНа декабрь:\n\n{the_result4[0]}\n\n—————————\n")


    def load_day_ne_1(self, group_id):
        """загрузка текста"""
        with self.connection:
            result = self.cursor.execute('SELECT `1_ne` FROM `groups` WHERE `group_id` = ?', (group_id,)).fetchall()
            send2 = result[0]
            return (f'Расписание на понедельник:\n\n{send2[0]}')


    def load_day_ne_2(self, group_id):
        """загрузка текста"""
        with self.connection:
            result = self.cursor.execute('SELECT `2_ne` FROM `groups` WHERE `group_id` = ?', (group_id,)).fetchall()
            send2 = result[0]
            return (f'Расписание на вторник:\n\n{send2[0]}')


    def load_day_ne_3(self, group_id):
        """загрузка текста"""
        with self.connection:
            result = self.cursor.execute('SELECT `3_ne` FROM `groups` WHERE `group_id` = ?', (group_id,)).fetchall()
            send2 = result[0]
            return (f'Расписание на среду:\n\n{send2[0]}')


    def load_day_ne_4(self, group_id):
        """загрузка текста"""
        with self.connection:
            result = self.cursor.execute('SELECT `4_ne` FROM `groups` WHERE `group_id` = ?', (group_id,)).fetchall()
            send2 = result[0]
            return (f'Расписание на четверг:\n\n{send2[0]}')


    def load_day_ne_5(self, group_id):
        """загрузка текста"""
        with self.connection:
            result = self.cursor.execute('SELECT `5_ne` FROM `groups` WHERE `group_id` = ?', (group_id,)).fetchall()
            send2 = result[0]
            return (f'Расписание на пятницу:\n\n{send2[0]}')


    def load_day_ne_6(self, group_id):
        """загрузка текста"""
        with self.connection:
            result = self.cursor.execute('SELECT `6_ne` FROM `groups` WHERE `group_id` = ?', (group_id,)).fetchall()
            send2 = result[0]
            return (f'Расписание на субботу:\n\n{send2[0]}')


    def load_day_ch_1(self, group_id):
        """загрузка текста"""
        with self.connection:
            result = self.cursor.execute('SELECT `1_ch` FROM `groups` WHERE `group_id` = ?', (group_id,)).fetchall()
            send2 = result[0]
            return (f'Расписание на понедельник:\n\n{send2[0]}')


    def load_day_ch_2(self, group_id):
        """загрузка текста"""
        with self.connection:
            result = self.cursor.execute('SELECT `2_ch` FROM `groups` WHERE `group_id` = ?', (group_id,)).fetchall()
            send2 = result[0]
            return (f'Расписание на вторник:\n\n{send2[0]}')


    def load_day_ch_3(self, group_id):
        """загрузка текста"""
        with self.connection:
            result = self.cursor.execute('SELECT `3_ch` FROM `groups` WHERE `group_id` = ?', (group_id,)).fetchall()
            send2 = result[0]
            return (f'Расписание на среду:\n\n{send2[0]}')


    def load_day_ch_4(self, group_id):
        """загрузка текста"""
        with self.connection:
            result = self.cursor.execute('SELECT `4_ch` FROM `groups` WHERE `group_id` = ?', (group_id,)).fetchall()
            send2 = result[0]
            return (f'Расписание на четверг:\n\n{send2[0]}')


    def load_day_ch_5(self, group_id):
        """загрузка текста"""
        with self.connection:
            result = self.cursor.execute('SELECT `5_ch` FROM `groups` WHERE `group_id` = ?', (group_id,)).fetchall()
            send2 = result[0]
            return (f'Расписание на пятницу:\n\n{send2[0]}')


    def load_day_ch_6(self, group_id):
        """загрузка текста"""
        with self.connection:
            result = self.cursor.execute('SELECT `6_ch` FROM `groups` WHERE `group_id` = ?', (group_id,)).fetchall()
            send2 = result[0]
            return (f'Расписание на субботу:\n\n{send2[0]}')


    def load_day_ne_all(self, group_id):
        """загрузка текста"""
        with self.connection:
            result1 = self.cursor.execute('SELECT `1_ne` FROM `groups` WHERE `group_id` = ?', (group_id,)).fetchall()
            the_result1 = result1[0]
            result2 = self.cursor.execute('SELECT `2_ne` FROM `groups` WHERE `group_id` = ?', (group_id,)).fetchall()
            the_result2 = result2[0]
            result3 = self.cursor.execute('SELECT `3_ne` FROM `groups` WHERE `group_id` = ?', (group_id,)).fetchall()
            the_result3 = result3[0]
            result4 = self.cursor.execute('SELECT `4_ne` FROM `groups` WHERE `group_id` = ?', (group_id,)).fetchall()
            the_result4 = result4[0]
            result5 = self.cursor.execute('SELECT `5_ne` FROM `groups` WHERE `group_id` = ?', (group_id,)).fetchall()
            the_result5 = result5[0]
            result6 = self.cursor.execute('SELECT `6_ne` FROM `groups` WHERE `group_id` = ?', (group_id,)).fetchall()
            the_result6 = result6[0]

            return (f"🔵 нечетная неделя\n\n—————————\nПонедельник:\n\n{the_result1[0]}\n\n"
                f"—————————\nВторник:\n\n{the_result2[0]}\n\n"
                f"—————————\nСреда:\n\n{the_result3[0]}\n\n"
                f"—————————\nЧетверг:\n\n{the_result4[0]}\n\n"
                f"—————————\nПятница:\n\n{the_result5[0]}\n\n"
                f"—————————\nСуббота:\n\n{the_result6[0]}\n\n—————————\n")


    def load_day_ch_all(self, group_id):
        """загрузка текста"""
        with self.connection:
            result1 = self.cursor.execute('SELECT `1_ch` FROM `groups` WHERE `group_id` = ?', (group_id,)).fetchall()
            the_result1 = result1[0]
            result2 = self.cursor.execute('SELECT `2_ch` FROM `groups` WHERE `group_id` = ?', (group_id,)).fetchall()
            the_result2 = result2[0]
            result3 = self.cursor.execute('SELECT `3_ch` FROM `groups` WHERE `group_id` = ?', (group_id,)).fetchall()
            the_result3 = result3[0]
            result4 = self.cursor.execute('SELECT `4_ch` FROM `groups` WHERE `group_id` = ?', (group_id,)).fetchall()
            the_result4 = result4[0]
            result5 = self.cursor.execute('SELECT `5_ch` FROM `groups` WHERE `group_id` = ?', (group_id,)).fetchall()
            the_result5 = result5[0]
            result6 = self.cursor.execute('SELECT `6_ch` FROM `groups` WHERE `group_id` = ?', (group_id,)).fetchall()
            the_result6 = result6[0]

            return (f"🟡 четная неделя\n\n—————————\nПонедельник:\n\n{the_result1[0]}\n\n"
                f"—————————\nВторник:\n\n{the_result2[0]}\n\n"
                f"—————————\nСреда:\n\n{the_result3[0]}\n\n"
                f"—————————\nЧетверг:\n\n{the_result4[0]}\n\n"
                f"—————————\nПятница:\n\n{the_result5[0]}\n\n"
                f"—————————\nСуббота:\n\n{the_result6[0]}\n\n—————————\n")


    def group_online(self, kurator):
        """Получаем всех людей из группы с уведомлениями"""
        with self.connection:
            return self.cursor.execute("SELECT * FROM `allusers` WHERE `group` = ? AND `online` = 1", (kurator,)).fetchall()


    def close(self):
        """Закрываем соединение с БД"""
        self.connection.close()