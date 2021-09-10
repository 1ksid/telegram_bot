from aiogram import Bot, Dispatcher, executor, types
#----------------------------------------
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import logging
import aiogram.utils.markdown as md
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
#----------------------------------------
from config import TOKEN2
from messages import MESSAGES
from editgroups import EDITgroup
import keyboards as kb


#запуск
#----------------------------------------
logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN2)
dp = Dispatcher(bot, storage=MemoryStorage())

# инициализируем соединение с БД
checkuser = EDITgroup('accounts.db')

# инициализируем форму
class Form(StatesGroup):
    zad1 = State()
    pause1 = State()
    zad2 = State()
    pause2 = State()
    zad3 = State()
    pause3 = State()
    zad4 = State()
    pause4 = State()

    ne1 = State()
    pause5 = State()
    ne2 = State()
    pause6 = State()
    ne3 = State()
    pause7 = State()
    ne4 = State()
    pause8 = State()
    ne5 = State()
    pause9 = State()
    ne6 = State()
    pause10 = State()

    ch1 = State()
    pause11 = State()
    ch2 = State()
    pause12 = State()
    ch3 = State()
    pause13 = State()
    ch4 = State()
    pause14 = State()
    ch5 = State()
    pause15 = State()
    ch6 = State()
    pause16 = State()
#----------------------------------------


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


# получение id фото
#----------------------------------------
# получение токена фото, просто скинуть в бота фото в консоли выдаст токен (не в чате телеграмма)
@dp.message_handler(content_types=['photo'])
async def scan_message(msg: types.Message):
    document_id = msg.photo[0].file_id
    file_info = await bot.get_file(document_id)
    print(f'file_id: {file_info.file_id}')
    print(f'-----------------')
#----------------------------------------


async def anti_spam(*args, **kwargs):
    m = args[0]
    await m.answer("Попробуй позже")


# start help
#----------------------------------------
@dp.message_handler(commands=['start','help'])
@dp.throttled(anti_spam,rate=1)
async def process_start_command(message: types.Message):
    if (not checkuser.search_player(message.from_user.id)):
        pass
    else:
# если юзер в базе
        if (checkuser.check_kurva(message.from_user.id) == 0):
            pass
        elif (checkuser.check_kurva(message.from_user.id) == 1):
            await message.reply(f'🗿 Авторизован:\nКуратор И504Б', reply_markup=kb.menu_kur)
        elif (checkuser.check_kurva(message.from_user.id) == 2):
            await message.reply(f'🗿 Авторизован:\nКуратор И505Б', reply_markup=kb.menu_kur)
        else:
            await message.reply(f'Группа не доступна')
#----------------------------------------


# админ редактирование
#----------------------------------------
# zad1
#----------------------------------------
@dp.message_handler(state=Form.zad1)
async def process_form_zad_1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['zad1'] = message.text
        await bot.send_message(
            message.chat.id,
            md.text(
                md.text('Новый текст:\n\n',data['zad1']),
                sep='\n',
            ),
        )
    await Form.next()
    await message.answer("Изменить задание для сентября?", reply_markup=kb.yes)

@dp.message_handler(lambda message: message.text not in ["Да"], state=Form.pause1)
async def process_pause_invalid1(message: types.Message):
    return await message.answer("/cancel ?", reply_markup=kb.yes)

@dp.message_handler(state=Form.pause1)
async def process_pause1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        checkuser.set_zad1(data['zad1'], checkuser.check_kurva(message.from_user.id))
    await state.finish()
    await message.reply("Изменено", reply_markup=kb.red_2)
#----------------------------------------

# zad2
#----------------------------------------
@dp.message_handler(state=Form.zad2)
async def process_form_zad_2(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['zad2'] = message.text
        await bot.send_message(
            message.chat.id,
            md.text(
                md.text('Новый текст:\n\n',data['zad2']),
                sep='\n',
            ),
        )
    await Form.next()
    await message.answer("Изменить задание для октября?", reply_markup=kb.yes)

@dp.message_handler(lambda message: message.text not in ["Да"], state=Form.pause2)
async def process_pause_invalid2(message: types.Message):
    return await message.answer("/cancel ?", reply_markup=kb.yes)

@dp.message_handler(state=Form.pause2)
async def process_pause2(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        checkuser.set_zad2(data['zad2'], checkuser.check_kurva(message.from_user.id))
    await state.finish()
    await message.reply("Изменено", reply_markup=kb.red_2)
#----------------------------------------

# zad3
#----------------------------------------
@dp.message_handler(state=Form.zad3)
async def process_form_zad_3(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['zad3'] = message.text
        await bot.send_message(
            message.chat.id,
            md.text(
                md.text('Новый текст:\n\n',data['zad3']),
                sep='\n',
            ),
        )
    await Form.next()
    await message.answer("Изменить задание для ноября?", reply_markup=kb.yes)

@dp.message_handler(lambda message: message.text not in ["Да"], state=Form.pause3)
async def process_pause_invalid3(message: types.Message):
    return await message.answer("/cancel ?", reply_markup=kb.yes)

@dp.message_handler(state=Form.pause3)
async def process_pause3(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        checkuser.set_zad3(data['zad3'], checkuser.check_kurva(message.from_user.id))
    await state.finish()
    await message.reply("Изменено", reply_markup=kb.red_2)
#----------------------------------------

# zad4
#----------------------------------------
@dp.message_handler(state=Form.zad4)
async def process_form_zad_4(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['zad4'] = message.text
        await bot.send_message(
            message.chat.id,
            md.text(
                md.text('Новый текст:\n\n',data['zad4']),
                sep='\n',
            ),
        )
    await Form.next()
    await message.answer("Изменить задание для декабря?", reply_markup=kb.yes)

@dp.message_handler(lambda message: message.text not in ["Да"], state=Form.pause4)
async def process_pause_invalid4(message: types.Message):
    return await message.answer("/cancel ?", reply_markup=kb.yes)

@dp.message_handler(state=Form.pause4)
async def process_pause4(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        checkuser.set_zad4(data['zad4'], checkuser.check_kurva(message.from_user.id))
    await state.finish()
    await message.reply("Изменено", reply_markup=kb.red_2)
#----------------------------------------

# понедельник нечет
#----------------------------------------
@dp.message_handler(state=Form.ne1)
async def process_form_ne1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['ne1'] = message.text
        await bot.send_message(
            message.chat.id,
            md.text(
                md.text('Новый текст:\n\n',data['ne1']),
                sep='\n',
            ),
        )
    await Form.next()
    await message.answer("Изменить задание для понедельника (нечет)?", reply_markup=kb.yes)

@dp.message_handler(lambda message: message.text not in ["Да"], state=Form.pause5)
async def process_pause_invalid5(message: types.Message):
    return await message.answer("/cancel ?", reply_markup=kb.yes)

@dp.message_handler(state=Form.pause5)
async def process_pause5(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        checkuser.set_ne1(data['ne1'], checkuser.check_kurva(message.from_user.id))
    await state.finish()
    await message.reply("Изменено", reply_markup=kb.red_2)
#----------------------------------------

# вторник нечет
#----------------------------------------
@dp.message_handler(state=Form.ne2)
async def process_form_ne2(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['ne2'] = message.text
        await bot.send_message(
            message.chat.id,
            md.text(
                md.text('Новый текст:\n\n',data['ne2']),
                sep='\n',
            ),
        )
    await Form.next()
    await message.answer("Изменить задание для вторника (нечет)?", reply_markup=kb.yes)

@dp.message_handler(lambda message: message.text not in ["Да"], state=Form.pause6)
async def process_pause_invalid6(message: types.Message):
    return await message.answer("/cancel ?", reply_markup=kb.yes)

@dp.message_handler(state=Form.pause6)
async def process_pause6(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        checkuser.set_ne2(data['ne2'], checkuser.check_kurva(message.from_user.id))
    await state.finish()
    await message.reply("Изменено", reply_markup=kb.red_2)
#----------------------------------------

# среды нечет
#----------------------------------------
@dp.message_handler(state=Form.ne3)
async def process_form_ne3(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['ne3'] = message.text
        await bot.send_message(
            message.chat.id,
            md.text(
                md.text('Новый текст:\n\n',data['ne3']),
                sep='\n',
            ),
        )
    await Form.next()
    await message.answer("Изменить задание для среды (нечет)?", reply_markup=kb.yes)

@dp.message_handler(lambda message: message.text not in ["Да"], state=Form.pause7)
async def process_pause_invalid7(message: types.Message):
    return await message.answer("/cancel ?", reply_markup=kb.yes)

@dp.message_handler(state=Form.pause7)
async def process_pause7(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        checkuser.set_ne3(data['ne3'], checkuser.check_kurva(message.from_user.id))
    await state.finish()
    await message.reply("Изменено", reply_markup=kb.red_2)
#----------------------------------------

# четверг нечет
#----------------------------------------
@dp.message_handler(state=Form.ne4)
async def process_form_ne4(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['ne4'] = message.text
        await bot.send_message(
            message.chat.id,
            md.text(
                md.text('Новый текст:\n\n',data['ne4']),
                sep='\n',
            ),
        )
    await Form.next()
    await message.answer("Изменить задание для четверга (нечет)?", reply_markup=kb.yes)

@dp.message_handler(lambda message: message.text not in ["Да"], state=Form.pause8)
async def process_pause_invalid8(message: types.Message):
    return await message.answer("/cancel ?", reply_markup=kb.yes)

@dp.message_handler(state=Form.pause8)
async def process_pause8(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        checkuser.set_ne4(data['ne4'], checkuser.check_kurva(message.from_user.id))
    await state.finish()
    await message.reply("Изменено", reply_markup=kb.red_2)
#----------------------------------------

# пятница нечет
#----------------------------------------
@dp.message_handler(state=Form.ne5)
async def process_form_ne5(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['ne5'] = message.text
        await bot.send_message(
            message.chat.id,
            md.text(
                md.text('Новый текст:\n\n',data['ne5']),
                sep='\n',
            ),
        )
    await Form.next()
    await message.answer("Изменить задание для пятницы (нечет)?", reply_markup=kb.yes)

@dp.message_handler(lambda message: message.text not in ["Да"], state=Form.pause9)
async def process_pause_invalid9(message: types.Message):
    return await message.answer("/cancel ?", reply_markup=kb.yes)

@dp.message_handler(state=Form.pause9)
async def process_pause9(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        checkuser.set_ne5(data['ne5'], checkuser.check_kurva(message.from_user.id))
    await state.finish()
    await message.reply("Изменено", reply_markup=kb.red_2)
#----------------------------------------

# суббота нечет
#----------------------------------------
@dp.message_handler(state=Form.ne6)
async def process_form_ne6(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['ne6'] = message.text
        await bot.send_message(
            message.chat.id,
            md.text(
                md.text('Новый текст:\n\n',data['ne6']),
                sep='\n',
            ),
        )
    await Form.next()
    await message.answer("Изменить задание для субботы (нечет)?", reply_markup=kb.yes)

@dp.message_handler(lambda message: message.text not in ["Да"], state=Form.pause10)
async def process_pause_invalid10(message: types.Message):
    return await message.answer("/cancel ?", reply_markup=kb.yes)

@dp.message_handler(state=Form.pause10)
async def process_pause10(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        checkuser.set_ne6(data['ne6'], checkuser.check_kurva(message.from_user.id))
    await state.finish()
    await message.reply("Изменено", reply_markup=kb.red_2)
#----------------------------------------

# понедельник чет
#----------------------------------------
@dp.message_handler(state=Form.ch1)
async def process_form_ch1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['ch1'] = message.text
        await bot.send_message(
            message.chat.id,
            md.text(
                md.text('Новый текст:\n\n',data['ch1']),
                sep='\n',
            ),
        )
    await Form.next()
    await message.answer("Изменить задание для понедельника (чет)?", reply_markup=kb.yes)

@dp.message_handler(lambda message: message.text not in ["Да"], state=Form.pause11)
async def process_pause_invalid11(message: types.Message):
    return await message.answer("/cancel ?", reply_markup=kb.yes)

@dp.message_handler(state=Form.pause11)
async def process_pause11(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        checkuser.set_ch1(data['ch1'], checkuser.check_kurva(message.from_user.id))
    await state.finish()
    await message.reply("Изменено", reply_markup=kb.red_2)
#----------------------------------------

# вторник чет
#----------------------------------------
@dp.message_handler(state=Form.ch2)
async def process_form_ch2(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['ch2'] = message.text
        await bot.send_message(
            message.chat.id,
            md.text(
                md.text('Новый текст:\n\n',data['ch2']),
                sep='\n',
            ),
        )
    await Form.next()
    await message.answer("Изменить задание для вторника (чет)?", reply_markup=kb.yes)

@dp.message_handler(lambda message: message.text not in ["Да"], state=Form.pause12)
async def process_pause_invalid12(message: types.Message):
    return await message.answer("/cancel ?", reply_markup=kb.yes)

@dp.message_handler(state=Form.pause12)
async def process_pause12(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        checkuser.set_ch2(data['ch2'], checkuser.check_kurva(message.from_user.id))
    await state.finish()
    await message.reply("Изменено", reply_markup=kb.red_2)
#----------------------------------------

# среда чет
#----------------------------------------
@dp.message_handler(state=Form.ch3)
async def process_form_ch3(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['ch3'] = message.text
        await bot.send_message(
            message.chat.id,
            md.text(
                md.text('Новый текст:\n\n',data['ch3']),
                sep='\n',
            ),
        )
    await Form.next()
    await message.answer("Изменить задание для среды (чет)?", reply_markup=kb.yes)

@dp.message_handler(lambda message: message.text not in ["Да"], state=Form.pause13)
async def process_pause_invalid13(message: types.Message):
    return await message.answer("/cancel ?", reply_markup=kb.yes)

@dp.message_handler(state=Form.pause13)
async def process_pause13(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        checkuser.set_ch3(data['ch3'], checkuser.check_kurva(message.from_user.id))
    await state.finish()
    await message.reply("Изменено", reply_markup=kb.red_2)
#----------------------------------------

# четверг чет
#----------------------------------------
@dp.message_handler(state=Form.ch4)
async def process_form_ch4(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['ch4'] = message.text
        await bot.send_message(
            message.chat.id,
            md.text(
                md.text('Новый текст:\n\n',data['ch4']),
                sep='\n',
            ),
        )
    await Form.next()
    await message.answer("Изменить задание для четверга (чет)?", reply_markup=kb.yes)

@dp.message_handler(lambda message: message.text not in ["Да"], state=Form.pause14)
async def process_pause_invalid14(message: types.Message):
    return await message.answer("/cancel ?", reply_markup=kb.yes)

@dp.message_handler(state=Form.pause14)
async def process_pause14(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        checkuser.set_ch4(data['ch4'], checkuser.check_kurva(message.from_user.id))
    await state.finish()
    await message.reply("Изменено", reply_markup=kb.red_2)
#----------------------------------------

# пятница чет
#----------------------------------------
@dp.message_handler(state=Form.ch5)
async def process_form_ch5(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['ch5'] = message.text
        await bot.send_message(
            message.chat.id,
            md.text(
                md.text('Новый текст:\n\n',data['ch5']),
                sep='\n',
            ),
        )
    await Form.next()
    await message.answer("Изменить задание для пятницы (чет)?", reply_markup=kb.yes)

@dp.message_handler(lambda message: message.text not in ["Да"], state=Form.pause15)
async def process_pause_invalid15(message: types.Message):
    return await message.answer("/cancel ?", reply_markup=kb.yes)

@dp.message_handler(state=Form.pause15)
async def process_pause15(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        checkuser.set_ch5(data['ch5'], checkuser.check_kurva(message.from_user.id))
    await state.finish()
    await message.reply("Изменено", reply_markup=kb.red_2)
#----------------------------------------

# суббота чет
#----------------------------------------
@dp.message_handler(state=Form.ch6)
async def process_form_ch6(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['ch6'] = message.text
        await bot.send_message(
            message.chat.id,
            md.text(
                md.text('Новый текст:\n\n',data['ch6']),
                sep='\n',
            ),
        )
    await Form.next()
    await message.answer("Изменить задание для субботы (чет)?", reply_markup=kb.yes)

@dp.message_handler(lambda message: message.text not in ["Да"], state=Form.pause16)
async def process_pause_invalid16(message: types.Message):
    return await message.answer("/cancel ?", reply_markup=kb.yes)

@dp.message_handler(state=Form.pause16)
async def process_pause16(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        checkuser.set_ch6(data['ch6'], checkuser.check_kurva(message.from_user.id))
    await state.finish()
    await message.reply("Изменено", reply_markup=kb.red_2)
#----------------------------------------
#----------------------------------------


# куртор
#----------------------------------------
@dp.callback_query_handler(text_contains='kurator_')
async def callback_kurator1(call: types.CallbackQuery):
    if call.data and call.data.startswith("kurator_"):
        code = call.data[-1:]
        if code.isdigit():
            code = int(code)
        if code == 1:
            if (checkuser.check_kurva(call.from_user.id) == 0):
                await call.message.edit_text(f'⚠️ Ошибка доступа')
            else:
                await call.answer(text='Пропиши в оригинальном боте /spam', show_alert=True) 
        if code == 2:
            if (checkuser.check_kurva(call.from_user.id) == 0):
                await call.message.edit_text(f'⚠️ Ошибка доступа')
            else:
                await call.message.edit_text(f'Изменение расписания для:', reply_markup=kb.menu_kur_2)
        if code == 3:
            if (checkuser.check_kurva(call.from_user.id) == 0):
                await call.message.edit_text(f'⚠️ Ошибка доступа')
            else:
                await call.message.edit_text(f'Изменение задание:', reply_markup=kb.menu_kur_3)
        if code == 4:
            if (checkuser.check_kurva(call.from_user.id) == 0):
                await call.message.edit_text(f'⚠️ Ошибка доступа')  
            else:
                await call.message.edit_text(f'Изменение расписания нечетной недели:', reply_markup=kb.menu_kur_2_ne)
        if code == 5:
            if (checkuser.check_kurva(call.from_user.id) == 0):
                await call.message.edit_text(f'⚠️ Ошибка доступа') 
            else:
                await call.message.edit_text(f'Изменение расписания четной недели', reply_markup=kb.menu_kur_2_ch)
        if code == 6:
            if (checkuser.check_kurva(call.from_user.id) == 0):
                await call.message.edit_text(f'⚠️ Ошибка доступа') 
            else:
                answer_message = checkuser.log_my_group(checkuser.check_kurva(call.from_user.id))
                await call.message.edit_text(answer_message, reply_markup=kb.menu_kur_back)
        if code == 7:
            if (checkuser.check_kurva(call.from_user.id) == 0):
                await call.message.edit_text(f'⚠️ Ошибка доступа')
            else:
                await call.message.edit_text(f'Изменение расписания для:', reply_markup=kb.menu_kur_2)
        if code == 8:
            if (checkuser.check_kurva(call.from_user.id) == 0):
                await call.message.edit_text(f'⚠️ Ошибка доступа')
            elif (checkuser.check_kurva(call.from_user.id) == 1):
                await call.message.edit_text(f'🗿 Куратор И504Б', reply_markup=kb.menu_kur)
            elif (checkuser.check_kurva(call.from_user.id) == 2):
                await call.message.edit_text(f'🗿 Куратор И505Б', reply_markup=kb.menu_kur) 
            else:
                await call.message.edit_text(f'⚠️ Ошибка доступа')
        if code == 9:
            if (checkuser.check_kurva(call.from_user.id) == 0):
                await call.message.edit_text(f'⚠️ Ошибка доступа')
            else:
                await call.message.delete()
#----------------------------------------

# расписание нечет
#----------------------------------------
@dp.callback_query_handler(text_contains='kurrasne_')
async def callback_kurator2(call: types.CallbackQuery):
    if call.data and call.data.startswith("kurrasne_"):
        code = call.data[-1:]
        if code.isdigit():
            code = int(code)
        if code == 1:
            if (checkuser.check_kurva(call.from_user.id) == 0):
                await call.message.edit_text(f'⚠️ Ошибка доступа')
            else:
                await call.message.delete()
                await bot.send_message(call.from_user.id, f'Редактор включен - понедельник (нечет)', reply_markup=kb.cancel)
                await Form.ne1.set()  
        if code == 2:
            if (checkuser.check_kurva(call.from_user.id) == 0):
                await call.message.edit_text(f'⚠️ Ошибка доступа')
            else:
                await call.message.delete()
                await bot.send_message(call.from_user.id, f'Редактор включен - вторник (нечет)', reply_markup=kb.cancel)
                await Form.ne2.set()
        if code == 3:
            if (checkuser.check_kurva(call.from_user.id) == 0):
                await call.message.edit_text(f'⚠️ Ошибка доступа')
            else:
                await call.message.delete()
                await bot.send_message(call.from_user.id, f'Редактор включен - среда (нечет)', reply_markup=kb.cancel)
                await Form.ne3.set()
        if code == 4:
            if (checkuser.check_kurva(call.from_user.id) == 0):
                await call.message.edit_text(f'⚠️ Ошибка доступа')
            else:
                await call.message.delete()
                await bot.send_message(call.from_user.id, f'Редактор включен - четверг (нечет)', reply_markup=kb.cancel)
                await Form.ne4.set()
        if code == 5:
            if (checkuser.check_kurva(call.from_user.id) == 0):
                await call.message.edit_text(f'⚠️ Ошибка доступа')
            else:
                await call.message.delete()
                await bot.send_message(call.from_user.id, f'Редактор включен - пятница (нечет)', reply_markup=kb.cancel)
                await Form.ne5.set()
        if code == 6:
            if (checkuser.check_kurva(call.from_user.id) == 0):
                await call.message.edit_text(f'⚠️ Ошибка доступа')
            else:
                await call.message.delete()
                await bot.send_message(call.from_user.id, f'Редактор включен - суббота (нечет)', reply_markup=kb.cancel)
                await Form.ne6.set()
#----------------------------------------

# расписание чет
#----------------------------------------
@dp.callback_query_handler(text_contains='kurrasch_')
async def callback_kurator3(call: types.CallbackQuery):
    if call.data and call.data.startswith("kurrasch_"):
        code = call.data[-1:]
        if code.isdigit():
            code = int(code)
        if code == 1:
            if (checkuser.check_kurva(call.from_user.id) == 0):
                await call.message.edit_text(f'⚠️ Ошибка доступа')
            else:
                await call.message.delete()
                await bot.send_message(call.from_user.id, f'Редактор включен - понедельник (чет)', reply_markup=kb.cancel)
                await Form.ch1.set()  
        if code == 2:
            if (checkuser.check_kurva(call.from_user.id) == 0):
                await call.message.edit_text(f'⚠️ Ошибка доступа')
            else:
                await call.message.delete()
                await bot.send_message(call.from_user.id, f'Редактор включен - вторник (чет)', reply_markup=kb.cancel)
                await Form.ch2.set()
        if code == 3:
            if (checkuser.check_kurva(call.from_user.id) == 0):
                await call.message.edit_text(f'⚠️ Ошибка доступа')
            else:
                await call.message.delete()
                await bot.send_message(call.from_user.id, f'Редактор включен - среда (чет)', reply_markup=kb.cancel)
                await Form.ch3.set()
        if code == 4:
            if (checkuser.check_kurva(call.from_user.id) == 0):
                await call.message.edit_text(f'⚠️ Ошибка доступа')
            else:
                await call.message.delete()
                await bot.send_message(call.from_user.id, f'Редактор включен - четверг (чет)', reply_markup=kb.cancel)
                await Form.ch4.set()
        if code == 5:
            if (checkuser.check_kurva(call.from_user.id) == 0):
                await call.message.edit_text(f'⚠️ Ошибка доступа')
            else:
                await call.message.delete()
                await bot.send_message(call.from_user.id, f'Редактор включен - пятница (чет)', reply_markup=kb.cancel)
                await Form.ch5.set()
        if code == 6:
            if (checkuser.check_kurva(call.from_user.id) == 0):
                await call.message.edit_text(f'⚠️ Ошибка доступа')
            else:
                await call.message.delete()
                await bot.send_message(call.from_user.id, f'Редактор включен - суббота (чет)', reply_markup=kb.cancel)
                await Form.ch6.set()
#----------------------------------------


# задание
#----------------------------------------
@dp.callback_query_handler(text_contains='editzad_')
async def callback_kurator44(call: types.CallbackQuery):
    if call.data and call.data.startswith("editzad_"):
        code = call.data[-1:]
        if code.isdigit():
            code = int(code)
        if code == 1:
            if (checkuser.check_kurva(call.from_user.id) == 0):
                await call.message.edit_text(f'⚠️ Ошибка доступа')
            else:
                await call.message.delete()
                await bot.send_message(call.from_user.id, f'Редактор включен - задание на сентябрь', reply_markup=kb.cancel)
                await Form.zad1.set()    
        if code == 2:
            if (checkuser.check_kurva(call.from_user.id) == 0):
                await call.message.edit_text(f'⚠️ Ошибка доступа')
            else:
                await call.message.delete()
                await bot.send_message(call.from_user.id, f'Редактор включен - задание на октябрь', reply_markup=kb.cancel)
                await Form.zad2.set()
        if code == 3:
            if (checkuser.check_kurva(call.from_user.id) == 0):
                await call.message.edit_text(f'⚠️ Ошибка доступа')
            else:
                await call.message.delete()
                await bot.send_message(call.from_user.id, f'Редактор включен - задание на ноябрь', reply_markup=kb.cancel)
                await Form.zad3.set()
        if code == 4:
            if (checkuser.check_kurva(call.from_user.id) == 0):
                await call.message.edit_text(f'⚠️ Ошибка доступа')
            else:
                await call.message.delete()
                await bot.send_message(call.from_user.id, f'Редактор включен - задание на декабрь', reply_markup=kb.cancel)
                await Form.zad4.set()
#----------------------------------------


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)