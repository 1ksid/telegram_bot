from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import types

closekeyboards = types.ReplyKeyboardRemove()

# при нажатии старт (/start)
#----------------------------------------
button_for_cancel = KeyboardButton('/cancel')
button_after_cancel = KeyboardButton('/start')
red_1 = ReplyKeyboardMarkup(resize_keyboard=True).add(button_for_cancel)
red_2 = ReplyKeyboardMarkup(resize_keyboard=True).add(button_after_cancel)
#----------------------------------------


# при нажатии старт (/start)
#----------------------------------------
button_1a = KeyboardButton('Сейчас: 🔵 нечетная неделя')
button_1b = KeyboardButton('Сейчас: 🟡 четная неделя')
button_2 = KeyboardButton('📅 Расписание')
button_3 = KeyboardButton('📚 Задания')
button_4 = KeyboardButton('⚙️ Настройки')

menu_0 = ReplyKeyboardMarkup(resize_keyboard=True).add(button_1a).add(button_2).add(button_3).add(button_4)
menu_1 = ReplyKeyboardMarkup(resize_keyboard=True).add(button_1b).add(button_2).add(button_3).add(button_4)
# 0 - нечетная / 1 - четная
#----------------------------------------


# расписание
#----------------------------------------
# week 
#----------------------------------------
button_2_3 = KeyboardButton('↪️ Назад')

button_2_1 = KeyboardButton('🔵 нечетная неделя')
button_2_2 = KeyboardButton('🟡 четная неделя')

week_ne = ReplyKeyboardMarkup(resize_keyboard=True).add(button_1a).add(button_2_1, button_2_2).add(button_2_3)
week_ch = ReplyKeyboardMarkup(resize_keyboard=True).add(button_1b).add(button_2_1, button_2_2).add(button_2_3)
#----------------------------------------
# day
#----------------------------------------
# нечетная
day_ne_back = InlineKeyboardButton('Назад', callback_data='day_ne_9')
menu_day_ne_back = InlineKeyboardMarkup().add(day_ne_back)

day_ne_1 = InlineKeyboardButton('Понедельник', callback_data='day_ne_1')
day_ne_2 = InlineKeyboardButton('Вторник', callback_data='day_ne_2')
day_ne_3 = InlineKeyboardButton('Среда', callback_data='day_ne_3')
day_ne_4 = InlineKeyboardButton('Четверг', callback_data='day_ne_4')
day_ne_5 = InlineKeyboardButton('Пятница', callback_data='day_ne_5')
day_ne_6 = InlineKeyboardButton('Суббота', callback_data='day_ne_6')
day_ne_9 = InlineKeyboardButton('Показать на всю неделю', callback_data='day_ne_8')
day_ne = InlineKeyboardMarkup().add(day_ne_1).add(day_ne_2).add(day_ne_3).add(day_ne_4).add(day_ne_5).add(day_ne_6).add(day_ne_9)

# четная
day_ch_back = InlineKeyboardButton('Назад', callback_data='day_ch_9')
menu_day_ch_back = InlineKeyboardMarkup().add(day_ch_back)

day_ch_1 = InlineKeyboardButton('Понедельник', callback_data='day_ch_1')
day_ch_2 = InlineKeyboardButton('Вторник', callback_data='day_ch_2')
day_ch_3 = InlineKeyboardButton('Среда', callback_data='day_ch_3')
day_ch_4 = InlineKeyboardButton('Четверг', callback_data='day_ch_4')
day_ch_5 = InlineKeyboardButton('Пятница', callback_data='day_ch_5')
day_ch_6 = InlineKeyboardButton('Суббота', callback_data='day_ch_6')
day_ch_9 = InlineKeyboardButton('Показать на всю неделю', callback_data='day_ch_8')
day_ch = InlineKeyboardMarkup().add(day_ch_1).add(day_ch_2).add(day_ch_3).add(day_ch_4).add(day_ch_5).add(day_ch_6).add(day_ch_9)
#----------------------------------------


# задания
#----------------------------------------
zad_1 = InlineKeyboardButton('Сентябрь (09)', callback_data='zad_1')
zad_2 = InlineKeyboardButton('Октябрь (10)', callback_data='zad_2')
zad_3 = InlineKeyboardButton('Ноябрь (11)', callback_data='zad_3')
zad_4 = InlineKeyboardButton('Декабрь (12)', callback_data='zad_4')
zad_5 = InlineKeyboardButton('Январь (13)', callback_data='zad_5')
zad_all = InlineKeyboardButton('Показать все', callback_data='zad_8')
menu_zad = InlineKeyboardMarkup().add(zad_all).add(zad_1).add(zad_2).add(zad_3).add(zad_4)

zad_back = InlineKeyboardButton('Назад', callback_data='zad_9')
menu_zad_back = InlineKeyboardMarkup().add(zad_back)
#----------------------------------------


# админ меню
#----------------------------------------
admin_back = InlineKeyboardButton('Назад', callback_data='admin_5')
admin_close = InlineKeyboardButton('Закрыть', callback_data='admin_6')

admin_1 = InlineKeyboardButton('Статистика', callback_data='admin_1')
admin_2 = InlineKeyboardButton('Изменить неделю', callback_data='admin_2')
admin_3 = InlineKeyboardButton('Изменить методичку', callback_data='admin_7')

inline_admin = InlineKeyboardMarkup().add(admin_1).add(admin_2).add(admin_3).add(admin_close)

admin_2_1 = InlineKeyboardButton('Нечетная', callback_data='admin_3')
admin_2_2 = InlineKeyboardButton('Четная', callback_data='admin_4')
inline_admin_2 = InlineKeyboardMarkup().add(admin_2_1, admin_2_2).add(admin_back)
#----------------------------------------



#----------------------------------------
#----------------------------------------
#----------------------------------------
# бот редактор
#----------------------------------------
#----------------------------------------
#----------------------------------------

# меню куратора
#----------------------------------------
# И504Б
kur_close = InlineKeyboardButton('Закрыть', callback_data='kurator_9')
kur_back = InlineKeyboardButton('Назад', callback_data='kurator_8')

kur_log = InlineKeyboardButton('Статистика группы', callback_data='kurator_6')
kur_1 = InlineKeyboardButton('Отправить сообщение группе', callback_data='kurator_1')
kur_2 = InlineKeyboardButton('Изменить расписание', callback_data='kurator_2')
kur_3 = InlineKeyboardButton('Изменить задания', callback_data='kurator_3')

menu_kur_back = InlineKeyboardMarkup().add(kur_back)
menu_kur = InlineKeyboardMarkup().add(kur_log).add(kur_1).add(kur_2).add(kur_3).add(kur_close)

# изменить расписание
kur_back_2 = InlineKeyboardButton('Назад', callback_data='kurator_7')

kur_2_1 = InlineKeyboardButton('нечетная неделя', callback_data='kurator_4')
kur_2_2 = InlineKeyboardButton('четная неделя', callback_data='kurator_5')

menu_kur_2 = InlineKeyboardMarkup().add(kur_2_1).add(kur_2_2).add(kur_close, kur_back)

# нечет расписание
kur_2_1_ne = InlineKeyboardButton('Понедельник (нечет)', callback_data='kurrasne_1')
kur_2_2_ne = InlineKeyboardButton('Вторник (нечет)', callback_data='kurrasne_2')
kur_2_3_ne = InlineKeyboardButton('Среда (нечет)', callback_data='kurrasne_3')
kur_2_4_ne = InlineKeyboardButton('Четверг (нечет)', callback_data='kurrasne_4')
kur_2_5_ne = InlineKeyboardButton('Пятница (нечет)', callback_data='kurrasne_5')
kur_2_6_ne = InlineKeyboardButton('Суббота (нечет)', callback_data='kurrasne_6')

menu_kur_2_ne = InlineKeyboardMarkup().add(kur_2_1_ne).add(kur_2_2_ne).add(kur_2_3_ne).add(kur_2_4_ne).add(kur_2_5_ne).add(kur_2_6_ne).add(kur_close, kur_back_2)

# чет расписание
kur_2_1_ch = InlineKeyboardButton('Понедельник (чет)', callback_data='kurrasch_1')
kur_2_2_ch = InlineKeyboardButton('Вторник (чет)', callback_data='kurrasch_2')
kur_2_3_ch = InlineKeyboardButton('Среда (чет)', callback_data='kurrasch_3')
kur_2_4_ch = InlineKeyboardButton('Четверг (чет)', callback_data='kurrasch_4')
kur_2_5_ch = InlineKeyboardButton('Пятница (чет)', callback_data='kurrasch_5')
kur_2_6_ch = InlineKeyboardButton('Суббота (чет)', callback_data='kurrasch_6')

menu_kur_2_ch = InlineKeyboardMarkup().add(kur_2_1_ch).add(kur_2_2_ch).add(kur_2_3_ch).add(kur_2_4_ch).add(kur_2_5_ch).add(kur_2_6_ch).add(kur_close, kur_back_2)

# задания
#----------------------------------------
kur_3_09 = InlineKeyboardButton('Сентябрь', callback_data='editzad_1')
kur_3_10 = InlineKeyboardButton('Октябрь', callback_data='editzad_2')
kur_3_11 = InlineKeyboardButton('Ноябрь', callback_data='editzad_3')
kur_3_12 = InlineKeyboardButton('Декабрь', callback_data='editzad_4')

menu_kur_3 = InlineKeyboardMarkup().add(kur_3_09).add(kur_3_10).add(kur_3_11).add(kur_3_12).add(kur_close, kur_back)
#----------------------------------------


# куратор редактор
#----------------------------------------
button_cancel = KeyboardButton('/cancel')
cancel = ReplyKeyboardMarkup(resize_keyboard=True).add(button_cancel)

yes_1 = KeyboardButton('Да')
yes = ReplyKeyboardMarkup(resize_keyboard=True).add(yes_1).add(button_cancel)
#----------------------------------------