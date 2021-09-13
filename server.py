from aiogram import Bot, Dispatcher, executor, types
#----------------------------------------
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import logging
import aiogram.utils.markdown as md
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
#----------------------------------------
from datetime import datetime
from config import TOKEN
from messages import MESSAGES
from accounts import ALLusers
import keyboards as kb



#запуск
#----------------------------------------
logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
dp = Dispatcher(bot,storage=MemoryStorage())

# инициализируем соединение с БД
checkuser = ALLusers('accounts.db')
#----------------------------------------

class Form(StatesGroup):
    spam = State()
    pause = State()

    met = State()
    pausemet = State()
#----------------------------------------
moderlist = [437185033]
#----------------------------------------


async def anti_spam(*args, **kwargs):
    m = args[0]
    await m.answer("Подожди не много")


# cancel
#----------------------------------------
@dp.message_handler(state='*', commands='cancel')
@dp.message_handler(Text(equals='cancel', ignore_case=True), state='*')
async def cancel_handler(message: types.Message, state: FSMContext):
    """
    Allow user to cancel any action
    """
    current_state = await state.get_state()
    if current_state is None:
        return

    logging.info('Cancelling state %r', current_state)
    # Cancel state and inform user about it
    await state.finish()
    # And remove keyboard (just in case)
    await message.reply('Отмена.', reply_markup=kb.red_2)
#----------------------------------------


# start help
#----------------------------------------
@dp.message_handler(commands=['start','help'])
@dp.throttled(anti_spam,rate=1) # rate - это время, если за 3 секунды отправится более отдного сообщения (от одного юзера), то это флуд
async def process_start_command(message: types.Message):
    if (not checkuser.search_player(message.from_user.id)):
        # если юзера нет в базе, добавляем
        checkuser.add_player(message.from_user.id)
        checkuser.update_online(message.from_user.id, True)
        await message.answer(f'👯‍♀️ Приветствую!\n\n👤 Группа не выбрана - /setgroup\n\n💌 Уведомления включены (уведомления заработают после выбора группы).\nДля отключения - /недоступно\n\n💬 Обратная связь - /feedback')
        if (checkuser.check_week() == 0):
            await message.answer(MESSAGES['start'], reply_markup=kb.menu_0)
           # await bot.send_photo(message.from_user.id, 'тут можно вставить токен фото, получить можно в боте server_redaktor просто отправить фото и в консоли даст ответ', MESSAGES['start'], reply_markup=kb.menu_0)
        else:
            await message.answer(MESSAGES['start'], reply_markup=kb.menu_1)
           # await bot.send_photo(message.from_user.id, 'AgACAgIAAxkBAAMCYTjNZ9GNXdGVcOfPOy7NKx4MhYIAAj61MRskHslJN33M-HgHkhsBAAMCAANzAAMgBA', MESSAGES['start'], reply_markup=kb.menu_1)
    else:
# если юзер в базе
        if (checkuser.check_week() == 0):
            await message.answer(MESSAGES['start'], reply_markup=kb.menu_0)
           # await bot.send_photo(message.from_user.id, 'AgACAgIAAxkBAAMCYTjNZ9GNXdGVcOfPOy7NKx4MhYIAAj61MRskHslJN33M-HgHkhsBAAMCAANzAAMgBA', MESSAGES['start'], reply_markup=kb.menu_0)
        else:
            await message.answer(MESSAGES['start'], reply_markup=kb.menu_1)
           # await bot.send_photo(message.from_user.id, 'AgACAgIAAxkBAAMCYTjNZ9GNXdGVcOfPOy7NKx4MhYIAAj61MRskHslJN33M-HgHkhsBAAMCAANzAAMgBA', MESSAGES['start'], reply_markup=kb.menu_1)

#----------------------------------------


# логи
#----------------------------------------
@dp.message_handler(commands=['admin'])
async def process_how_command(message: types.Message):
    if (message.from_user.id in moderlist):
        await message.answer(f'qq', reply_markup=kb.inline_admin)
    else:
        await message.reply(f'Команда не найдена.\nИспользуйте - /start')
#----------------------------------------


# главное меню
#----------------------------------------
@dp.message_handler(content_types=["text"])
@dp.throttled(anti_spam,rate=0.5) # rate - это время, если за 3 секунды отправится более отдного сообщения (от одного юзера), то это флуд
async def do_main_menu(message: types.Message):
    txt = message.text
    if (not checkuser.search_player(message.from_user.id)):
        await message.reply(MESSAGES['fail'])
    else:
        # главное меню
        if txt == '/feedback':
            await message.answer(MESSAGES['feedback'])
        elif txt == '↪️ Назад':
            if (checkuser.check_week() == 0):
                await message.answer(MESSAGES['start'], reply_markup=kb.menu_0)
            #    await bot.send_photo(message.from_user.id, 'AgACAgIAAxkBAAMCYTjNZ9GNXdGVcOfPOy7NKx4MhYIAAj61MRskHslJN33M-HgHkhsBAAMCAANzAAMgBA', MESSAGES['start'], reply_markup=kb.menu_0)
            else:
                await message.answer(MESSAGES['start'], reply_markup=kb.menu_1)
              #  await bot.send_photo(message.from_user.id, 'AgACAgIAAxkBAAMCYTjNZ9GNXdGVcOfPOy7NKx4MhYIAAj61MRskHslJN33M-HgHkhsBAAMCAANzAAMgBA', MESSAGES['start'], reply_markup=kb.menu_1)
        elif txt == '🔵 нечетная неделя':
            if (checkuser.check_week() == 0):
                await message.answer(f'Сейчас: 🔵 нечетная неделя', reply_markup=kb.week_ne)
                await message.answer(f'🔵 нечетная неделя\n\nВыбери день:', reply_markup=kb.day_ne)
            else:
                await message.answer(f'Сейчас: 🟡 четная неделя', reply_markup=kb.week_ch)
                await message.answer(f'🔵 нечетная неделя\n\nВыбери день:', reply_markup=kb.day_ne)
        elif txt == '🟡 четная неделя':
            if (checkuser.check_week() == 0):
                await message.answer(f'Сейчас: 🔵 нечетная неделя', reply_markup=kb.week_ne)
                await message.answer(f'🟡 четная неделя\n\nВыбери день:', reply_markup=kb.day_ch)
            else:
                await message.answer(f'Сейчас: 🟡 четная неделя', reply_markup=kb.week_ch)
                await message.answer(f'🟡 четная неделя\n\nВыбери день:', reply_markup=kb.day_ch)
        elif txt == 'Сейчас: 🟡 четная неделя':
            if (checkuser.check_week() == 0):
                await message.reply(f'Обновлено: 🔵 нечетная неделя', reply_markup=kb.menu_0)
            else:
                await message.reply(f'Обновлено: 🟡 четная неделя', reply_markup=kb.menu_1)
        elif txt == 'Сейчас: 🔵 нечетная неделя':
            if (checkuser.check_week() == 0):
                await message.reply(f'Обновлено: 🔵 нечетная неделя', reply_markup=kb.menu_0)
            else:
                await message.reply(f'Обновлено: 🟡 четная неделя', reply_markup=kb.menu_1)
        elif txt == '📅 Расписание':
            if (checkuser.check_week() == 0):
                rr = datetime.weekday(datetime.now())
                if (checkuser.check_group(message.from_user.id) == 0):
                    answer_message = f'⚠️ Группа не выбрана.\nИспользуй - /setgroup'
                elif (rr == 0):
                    answer_message = checkuser.load_day_ne_1(checkuser.check_group(message.from_user.id))
                elif (rr == 1):
                    answer_message = checkuser.load_day_ne_2(checkuser.check_group(message.from_user.id))
                elif (rr == 2):
                    answer_message = checkuser.load_day_ne_3(checkuser.check_group(message.from_user.id))
                elif (rr == 3):
                    answer_message = checkuser.load_day_ne_4(checkuser.check_group(message.from_user.id))
                elif (rr == 4):
                    answer_message = checkuser.load_day_ne_5(checkuser.check_group(message.from_user.id))
                elif (rr == 5):
                    answer_message = checkuser.load_day_ne_6(checkuser.check_group(message.from_user.id))
                elif (rr == 6):
                    answer_message = f'Отдыхай, сегодня воскресенье)'
                else:
                    answer_message = f'error'                  

                await message.answer(f'Сейчас: 🔵 нечетная неделя', reply_markup=kb.week_ne)
                await message.answer(answer_message, reply_markup=kb.menu_day_ne_back)  
            else:
                rr = datetime.weekday(datetime.now())
                if (checkuser.check_group(message.from_user.id) == 0):
                    answer_message = f'⚠️ Группа не выбрана.\nИспользуй - /setgroup'
                elif (rr == 0):
                    answer_message = checkuser.load_day_ch_1(checkuser.check_group(message.from_user.id))
                elif (rr == 1):
                    answer_message = checkuser.load_day_ch_2(checkuser.check_group(message.from_user.id))
                elif (rr == 2):
                    answer_message = checkuser.load_day_ch_3(checkuser.check_group(message.from_user.id))
                elif (rr == 3):
                    answer_message = checkuser.load_day_ch_4(checkuser.check_group(message.from_user.id))
                elif (rr == 4):
                    answer_message = checkuser.load_day_ch_5(checkuser.check_group(message.from_user.id))
                elif (rr == 5):
                    answer_message = checkuser.load_day_ch_6(checkuser.check_group(message.from_user.id))
                elif (rr == 6):
                    answer_message = f'Отдыхай, сегодня воскресенье)'
                else:
                    answer_message = f'error'                  

                await message.answer(f'Сейчас: 🟡 четная неделя', reply_markup=kb.week_ch)
                await message.answer(answer_message, reply_markup=kb.menu_day_ch_back)  
        elif txt == '⚙️ Настройки':
            if (checkuser.check_week() == 0):
                await message.answer(checkuser.settings_load(message.from_user.id), reply_markup=kb.menu_0)
            else:
                await message.answer(checkuser.settings_load(message.from_user.id), reply_markup=kb.menu_1)
        elif txt == '/settings':
            if (checkuser.check_week() == 0):
                await message.answer(checkuser.settings_load(message.from_user.id), reply_markup=kb.menu_0)
            else:
                await message.answer(checkuser.settings_load(message.from_user.id), reply_markup=kb.menu_1)
        elif txt == '/my_id':
            answer_message = checkuser.check_id(message.from_user.id)
            await message.reply(answer_message)
        elif txt == '/konsa':
            if (checkuser.check_week() == 0):
                await message.reply(f'⚠️ в разработке', reply_markup=kb.menu_0)
            else:
                await message.reply(f'⚠️ в разработке', reply_markup=kb.menu_1)
        elif txt == '/met':
            if (checkuser.check_week() == 0):
                answer_message = checkuser.load_met()
                await message.answer(answer_message, reply_markup=kb.menu_0)
            else:
                answer_message = checkuser.load_met()
                await message.answer(answer_message, reply_markup=kb.menu_1)
        elif txt == '📚 Задания':
            if (checkuser.check_week() == 0):
                await message.answer(f'Актуально на 2021 год', reply_markup=kb.menu_0)
                await message.answer(f'Выбери месяц', reply_markup=kb.menu_zad)                
            else:
                await message.answer(f'Актуально на 2021 год', reply_markup=kb.menu_1)
                await message.answer(f'Выбери месяц', reply_markup=kb.menu_zad)
        elif txt == '/spam':
            if (checkuser.check_kurva(message.from_user.id) == 0):
                await message.reply(f'🏳️‍🌈 Ты не куратор')
            else:
                await message.reply(f'Введите сообщение:', reply_markup=kb.cancel)
                await Form.spam.set()
        # настройки
        elif txt == '/mm':
            if (checkuser.check_kurva(message.from_user.id) == 0):
                await message.reply(f'🏳️‍🌈 Ты не куратор')
            else:
                await message.reply(f'🏳️‍🌈 Бот для кураторов - @kurator_de_santus_bot')
        elif txt == '/notifications':
            await message.reply(checkuser.settings_online(message.from_user.id))
            await message.answer(checkuser.settings_load(message.from_user.id))
        elif txt == '/setgroup':
            await message.reply(MESSAGES['groups'])
        # настройки - выбор группы
        elif txt == '/setgroup_0':
            await message.reply(checkuser.setgroup(message.from_user.id, 0))
            await message.answer(checkuser.settings_load(message.from_user.id))
        elif txt == '/setgroup_i504b':
            await message.reply(checkuser.setgroup(message.from_user.id, 1))
            await message.answer(checkuser.settings_load(message.from_user.id))
        elif txt == '/setgroup_i505b':
            await message.reply(checkuser.setgroup(message.from_user.id, 2))
            await message.answer(checkuser.settings_load(message.from_user.id))
        elif txt == '/setgroup_i507b':
            await message.reply(checkuser.setgroup(message.from_user.id, 3))
            await message.answer(checkuser.settings_load(message.from_user.id))
        else:
            await message.reply(f'Команда не найдена.\nИспользуйте - /start')
        return
#----------------------------------------

# расписание
#----------------------------------------
# нечетная
#----------------------------------------
@dp.callback_query_handler(text_contains='day_ne_')
@dp.throttled(anti_spam,rate=0.5)
async def callback_day_ne(call: types.CallbackQuery):
    if call.data and call.data.startswith("day_ne_"):
        code = call.data[-1:]
        if code.isdigit():
            code = int(code)
        if code == 1:
            if (checkuser.check_group(call.from_user.id) == 0):
                await call.message.edit_text(f'⚠️ Группа не выбрана.\nИспользуй - /setgroup')           
            else:
                answer_message = checkuser.load_day_ne_1(checkuser.check_group(call.from_user.id))
                await call.message.edit_text(answer_message, reply_markup=kb.menu_day_ne_back)
        if code == 2:
            if (checkuser.check_group(call.from_user.id) == 0):
                await call.message.edit_text(f'⚠️ Группа не выбрана.\nИспользуй - /setgroup')           
            else:
                answer_message = checkuser.load_day_ne_2(checkuser.check_group(call.from_user.id))
                await call.message.edit_text(answer_message, reply_markup=kb.menu_day_ne_back)
        if code == 3:
            if (checkuser.check_group(call.from_user.id) == 0):
                await call.message.edit_text(f'⚠️ Группа не выбрана.\nИспользуй - /setgroup')           
            else:
                answer_message = checkuser.load_day_ne_3(checkuser.check_group(call.from_user.id))
                await call.message.edit_text(answer_message, reply_markup=kb.menu_day_ne_back)
        if code == 4:
            if (checkuser.check_group(call.from_user.id) == 0):
                await call.message.edit_text(f'⚠️ Группа не выбрана.\nИспользуй - /setgroup')           
            else:
                answer_message = checkuser.load_day_ne_4(checkuser.check_group(call.from_user.id))
                await call.message.edit_text(answer_message, reply_markup=kb.menu_day_ne_back)
        if code == 5:
            if (checkuser.check_group(call.from_user.id) == 0):
                await call.message.edit_text(f'⚠️ Группа не выбрана.\nИспользуй - /setgroup')           
            else:
                answer_message = checkuser.load_day_ne_5(checkuser.check_group(call.from_user.id))
                await call.message.edit_text(answer_message, reply_markup=kb.menu_day_ne_back)
        if code == 6:
            if (checkuser.check_group(call.from_user.id) == 0):
                await call.message.edit_text(f'⚠️ Группа не выбрана.\nИспользуй - /setgroup')           
            else:
                answer_message = checkuser.load_day_ne_6(checkuser.check_group(call.from_user.id))
                await call.message.edit_text(answer_message, reply_markup=kb.menu_day_ne_back)
        if code == 8:
            if (checkuser.check_group(call.from_user.id) == 0):
                await call.message.edit_text(f'⚠️ Группа не выбрана.\nИспользуй - /setgroup')           
            else:
                answer_message = checkuser.load_day_ne_all(checkuser.check_group(call.from_user.id))
                await call.message.edit_text(answer_message, reply_markup=kb.menu_day_ne_back)
        if code == 9:
                await call.message.edit_text(f'🔵 нечетная неделя\n\nВыбери день:', reply_markup=kb.day_ne)
# четная
#----------------------------------------
@dp.callback_query_handler(text_contains='day_ch_')
@dp.throttled(anti_spam,rate=0.5)
async def callback_day_ch(call: types.CallbackQuery):
    if call.data and call.data.startswith("day_ch_"):
        code = call.data[-1:]
        if code.isdigit():
            code = int(code)
        if code == 1:
            if (checkuser.check_group(call.from_user.id) == 0):
                await call.message.edit_text(f'⚠️ Группа не выбрана.\nИспользуй - /setgroup')           
            else:
                answer_message = checkuser.load_day_ch_1(checkuser.check_group(call.from_user.id))
                await call.message.edit_text(answer_message, reply_markup=kb.menu_day_ch_back)
        if code == 2:
            if (checkuser.check_group(call.from_user.id) == 0):
                await call.message.edit_text(f'⚠️ Группа не выбрана.\nИспользуй - /setgroup')           
            else:
                answer_message = checkuser.load_day_ch_2(checkuser.check_group(call.from_user.id))
                await call.message.edit_text(answer_message, reply_markup=kb.menu_day_ch_back)
        if code == 3:
            if (checkuser.check_group(call.from_user.id) == 0):
                await call.message.edit_text(f'⚠️ Группа не выбрана.\nИспользуй - /setgroup')           
            else:
                answer_message = checkuser.load_day_ch_3(checkuser.check_group(call.from_user.id))
                await call.message.edit_text(answer_message, reply_markup=kb.menu_day_ch_back)
        if code == 4:
            if (checkuser.check_group(call.from_user.id) == 0):
                await call.message.edit_text(f'⚠️ Группа не выбрана.\nИспользуй - /setgroup')           
            else:
                answer_message = checkuser.load_day_ch_4(checkuser.check_group(call.from_user.id))
                await call.message.edit_text(answer_message, reply_markup=kb.menu_day_ch_back)
        if code == 5:
            if (checkuser.check_group(call.from_user.id) == 0):
                await call.message.edit_text(f'⚠️ Группа не выбрана.\nИспользуй - /setgroup')           
            else:
                answer_message = checkuser.load_day_ch_5(checkuser.check_group(call.from_user.id))
                await call.message.edit_text(answer_message, reply_markup=kb.menu_day_ch_back)
        if code == 6:
            if (checkuser.check_group(call.from_user.id) == 0):
                await call.message.edit_text(f'⚠️ Группа не выбрана.\nИспользуй - /setgroup')           
            else:
                answer_message = checkuser.load_day_ch_6(checkuser.check_group(call.from_user.id))
                await call.message.edit_text(answer_message, reply_markup=kb.menu_day_ch_back)
        if code == 8:
            if (checkuser.check_group(call.from_user.id) == 0):
                await call.message.edit_text(f'⚠️ Группа не выбрана.\nИспользуй - /setgroup')           
            else:
                answer_message = checkuser.load_day_ch_all(checkuser.check_group(call.from_user.id))
                await call.message.edit_text(answer_message, reply_markup=kb.menu_day_ch_back)
        if code == 9:
                await call.message.edit_text(f'🟡 четная неделя\n\nВыбери день:', reply_markup=kb.day_ch)
#----------------------------------------


# задания
#----------------------------------------
@dp.callback_query_handler(text_contains='zad_')
@dp.throttled(anti_spam,rate=0.5)
async def callback_zadanie(call: types.CallbackQuery):
    if call.data and call.data.startswith("zad_"):
        code = call.data[-1:]
        if code.isdigit():
            code = int(code)
        if code == 1:
            if (checkuser.check_group(call.from_user.id) == 0):
                await call.message.edit_text(f'⚠️ Группа не выбрана.\nИспользуй - /setgroup')           
            else:
                answer_message = checkuser.load_m_09(checkuser.check_group(call.from_user.id))
                await call.message.edit_text(answer_message, reply_markup=kb.menu_zad_back)
        if code == 2:
            if (checkuser.check_group(call.from_user.id) == 0):
                await call.message.edit_text(f'⚠️ Группа не выбрана.\nИспользуй - /setgroup')           
            else:
                answer_message = checkuser.load_m_10(checkuser.check_group(call.from_user.id))
                await call.message.edit_text(answer_message, reply_markup=kb.menu_zad_back)
        if code == 3:
            if (checkuser.check_group(call.from_user.id) == 0):
                await call.message.edit_text(f'⚠️ Группа не выбрана.\nИспользуй - /setgroup')           
            else:
                answer_message = checkuser.load_m_11(checkuser.check_group(call.from_user.id))
                await call.message.edit_text(answer_message, reply_markup=kb.menu_zad_back)
        if code == 4:
            if (checkuser.check_group(call.from_user.id) == 0):
                await call.message.edit_text(f'⚠️ Группа не выбрана.\nИспользуй - /setgroup')           
            else:
                answer_message = checkuser.load_m_12(checkuser.check_group(call.from_user.id))
                await call.message.edit_text(answer_message, reply_markup=kb.menu_zad_back)
        if code == 5:
            await call.answer(text='Не доступно', show_alert=True)
        if code == 8:
            if (checkuser.check_group(call.from_user.id) == 0):
                await call.message.edit_text(f'⚠️ Группа не выбрана.\nИспользуй - /setgroup')           
            else:
                answer_message = checkuser.load_m_42(checkuser.check_group(call.from_user.id))
                await call.message.edit_text(answer_message, reply_markup=kb.menu_zad_back)
        if code == 9:
            await call.message.edit_text(f'Выбери месяц', reply_markup=kb.menu_zad)
#----------------------------------------


# admin
#----------------------------------------
@dp.callback_query_handler(text_contains='admin_')
async def callback_admin(call: types.CallbackQuery):
    if call.data and call.data.startswith("admin_"):
        code = call.data[-1:]
        if code.isdigit():
            code = int(code)
        if code == 1:
            answer_message = checkuser.log_info()
            await call.message.delete()
            await bot.send_message(call.from_user.id, text=answer_message, reply_markup=kb.inline_admin)
        if code == 2:
            await call.message.delete()
            await bot.send_message(call.from_user.id, text=f'Изменить неделю на:', reply_markup=kb.inline_admin_2)
        if code == 3:
            checkuser.change_week(0)
            await call.message.delete()
            answer_message = checkuser.full_check_week()
            await bot.send_message(call.from_user.id, text=answer_message, reply_markup=kb.inline_admin)
        if code == 4:
            checkuser.change_week(1)
            await call.message.delete()
            answer_message = checkuser.full_check_week()
            await bot.send_message(call.from_user.id, text=answer_message, reply_markup=kb.inline_admin)
        if code == 5:
            await call.message.delete()
            await bot.send_message(call.from_user.id, text=f'qq', reply_markup=kb.inline_admin)
        if code == 6:
            await call.message.delete()
        if code == 7:
            await call.message.delete()
            await bot.send_message(call.from_user.id, text=f'Редактор включен - методичка', reply_markup=kb.cancel)
            await Form.met.set()
#----------------------------------------


# spam
#----------------------------------------
@dp.message_handler(state=Form.spam)
async def process_form_spam(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['spam'] = message.text
        await bot.send_message(
            message.chat.id,
            md.text(
                md.text('Текст для группы:\n\n',data['spam']),
                sep='\n',
            ),
        )
    await Form.next()
    await message.answer("Отправить?", reply_markup=kb.yes)

@dp.message_handler(lambda message: message.text not in ["Да"], state=Form.pause)
async def process_pause_invalid(message: types.Message):
    return await message.answer("/cancel ?", reply_markup=kb.yes)

@dp.message_handler(state=Form.pause)
async def process_pause(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if (checkuser.check_kurva(message.from_user.id) == 0):
            pass
        else:
            data['user_group'] = checkuser.check_group2(message.from_user.id)
            user_for_spam = (checkuser.group_online(checkuser.check_kurva(message.from_user.id)))
            for s in user_for_spam:
                await bot.send_message(s[1], md.text(md.text('🌝 Уведомление для группы ', data['user_group'], '\n\n',data['spam']),sep='\n',),)
    await state.finish()
    await message.reply("Отправлено", reply_markup=kb.red_2)


# /met
#----------------------------------------
@dp.message_handler(state=Form.met)
async def process_form_met(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['met'] = message.text
        await bot.send_message(
            message.chat.id,
            md.text(
                md.text('Новый текст:\n\n',data['met']),
                sep='\n',
            ),
        )
    await Form.next()
    await message.answer("Изменить методички?", reply_markup=kb.yes)

@dp.message_handler(lambda message: message.text not in ["Да"], state=Form.pausemet)
async def process_pause_invalid_met1(message: types.Message):
    return await message.answer("/cancel ?", reply_markup=kb.yes)

@dp.message_handler(state=Form.pausemet)
async def process_pause1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        checkuser.set_met(data['met'])
    await state.finish()
    await message.reply("Изменено", reply_markup=kb.red_2)
#----------------------------------------
#----------------------------------------


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)