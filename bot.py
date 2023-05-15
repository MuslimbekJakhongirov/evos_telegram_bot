

import logging

from aiogram import Bot, Dispatcher, executor, types
from config import API_TOKEN
from buttons import * 

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Tilni tanglang: ", reply_markup=language)

@dp.message_handler(text="🇺🇿 O'zbekcha")
async def echo(message: types.Message):
    await message.answer("Telefon raqamingizni yuboring: ", reply_markup=phone_number)

@dp.message_handler(content_types='contact')
async def echo(message: types.Message):
    await message.answer("Joylashuvni yuboring: ", reply_markup=location)

@dp.message_handler(content_types='location')
async def echo(message: types.Message):
    await message.answer("Siz ro'yxatdan o'tdingiz!\n\nKategoriyalardan birini tanlang: ", reply_markup=below_menu)

@dp.message_handler(text="Buyurtma berish! 🧑‍💻")
async def echo(message: types.Message):
    await message.answer("Marhamat menu! Tanlang...", reply_markup=main_menu)

@dp.message_handler(text="Sozlamalar! 🛠")
async def echo(message: types.Message):
    await message.answer("Sozlanmoqda!!!")

@dp.message_handler(text="Biz bilan bog'lanish! ☎️")
async def echo(message: types.Message):
    await message.answer("Sozlanmoqda!!!")    

# backs ===========================================================================
# lavash  
@dp.callback_query_handler(text='back')
async def my_func(call: types.CallbackQuery):
    await call.message.answer("Marhamat menu!\nTanlang...", reply_markup=main_menu)

# mol gosht mini_classik  
@dp.callback_query_handler(text='back11')
async def my_func(call: types.CallbackQuery):
    await call.message.answer("✅Marxamat lavashlar menusi!!! ", reply_markup=lavash_menu)

# mol gosht numbers mini 
@dp.callback_query_handler(text='back111')
async def my_func(call: types.CallbackQuery):
    await call.message.answer("✅Kategoriyalardan birini tanlang!!! ", reply_markup=mini_classik)

# mol gosht numbers classik   
@dp.callback_query_handler(text='back1111')
async def my_func(call: types.CallbackQuery):
    await call.message.answer("✅Kategoriyalardan birini tanlang!!! ", reply_markup=mini_classik)

# qalampirli mol gosht mini_classik   
@dp.callback_query_handler(text='back2')
async def my_func(call: types.CallbackQuery):
    await call.message.answer("✅Marxamat lavashlar menusi!!! ", reply_markup=lavash_menu)

# qalampir mol gosht numbers mini 
@dp.callback_query_handler(text='back22')
async def my_func(call: types.CallbackQuery):
    await call.message.answer("✅Kategoriyalardan birini tanlang!!! ", reply_markup=mini_classik2)

# qalampir mol gosht numbers classik   
@dp.callback_query_handler(text='back222')
async def my_func(call: types.CallbackQuery):
    await call.message.answer("✅Kategoriyalardan birini tanlang!!! ", reply_markup=mini_classik2)

# tovuq goshtlik mini_classik 
@dp.callback_query_handler(text='back3')
async def my_func(call: types.CallbackQuery):
    await call.message.answer("✅Marxamat lavashlar menusi!!! ", reply_markup=lavash_menu)

# tovuqli numbers mini   
@dp.callback_query_handler(text='back33')
async def my_func(call: types.CallbackQuery):
    await call.message.answer("✅Kategoriyalardan birini tanlang!!! ", reply_markup=mini_classik4)

# tovuqlik numbers classik   
@dp.callback_query_handler(text='back333')
async def my_func(call: types.CallbackQuery):
    await call.message.answer("✅Kategoriyalardan birini tanlang!!! ", reply_markup=mini_classik4)

# qalampirli tovuq goshtlik mini_classik 
@dp.callback_query_handler(text='back4')
async def my_func(call: types.CallbackQuery):
    await call.message.answer("✅Marxamat lavashlar menusi!!! ", reply_markup=lavash_menu)

# qalampir tovuqlik numbers mini   
@dp.callback_query_handler(text='back44')
async def my_func(call: types.CallbackQuery):
    await call.message.answer("✅Kategoriyalardan birini tanlang!!! ", reply_markup=mini_classik6)

# qalampir tovuqlik numbers classik   
@dp.callback_query_handler(text='back444')
async def my_func(call: types.CallbackQuery):
    await call.message.answer("✅Kategoriyalardan birini tanlang!!! ", reply_markup=mini_classik6)

# pishloqli gosht mini_classik  
@dp.callback_query_handler(text='back5')
async def my_func(call: types.CallbackQuery):
    await call.message.answer("✅Marxamat lavashlar menusi!!! ", reply_markup=lavash_menu)

# pishloqli mol numbers mini 
@dp.callback_query_handler(text='back55')
async def my_func(call: types.CallbackQuery):
    await call.message.answer("✅Kategoriyalardan birini tanlang!!! ", reply_markup=mini_classik8)

# pishloqli mol numbers classik 
@dp.callback_query_handler(text='back555')
async def my_func(call: types.CallbackQuery):
    await call.message.answer("✅Kategoriyalardan birini tanlang!!! ", reply_markup=mini_classik8)

# pishloq_tovuq_gosht mini_classik
@dp.callback_query_handler(text='back6')
async def my_func(call: types.CallbackQuery):
    await call.message.answer("✅Marxamat lavashlar menusi!!! ", reply_markup=lavash_menu)

# pishloqli tovuq numbers mini 
@dp.callback_query_handler(text='back66')
async def my_func(call: types.CallbackQuery):
    await call.message.answer("✅Kategoriyalardan birini tanlang!!! ", reply_markup=mini_classik10)

# pishloqli tovuq numbers classik  
@dp.callback_query_handler(text='back666')
async def my_func(call: types.CallbackQuery):
    await call.message.answer("✅Kategoriyalardan birini tanlang!!! ", reply_markup=mini_classik10)

# flitter mini_classik   
@dp.callback_query_handler(text='back7')
async def my_func(call: types.CallbackQuery):
    await call.message.answer("✅Marxamat lavashlar menusi!!! ", reply_markup=lavash_menu)


# flitter numbers mini  
@dp.callback_query_handler(text='back77')
async def my_func(call: types.CallbackQuery):
    await call.message.answer("✅Kategoriyalardan birini tanlang!!! ", reply_markup=mini_classik12)

# flitter numbers classik 
@dp.callback_query_handler(text='back777')
async def my_func(call: types.CallbackQuery):
    await call.message.answer("✅Kategoriyalardan birini tanlang!!! ", reply_markup=mini_classik12)


# hot-dog    
@dp.callback_query_handler(text='back8')
async def my_func(call: types.CallbackQuery):
    await call.message.answer("Marhamat menu!\nTanlang...", reply_markup=main_menu)

# hot_dog_baget_dabl numbers  
@dp.callback_query_handler(text='back88')
async def my_func(call: types.CallbackQuery):
    await call.message.answer("Marhamat menu!\nTanlang...", reply_markup=hot_dog_menu)

# numbers_classik_hot_dog15       
@dp.callback_query_handler(text='back888')
async def my_func(call: types.CallbackQuery):
    await call.message.answer("Marhamat menu!\nTanlang...", reply_markup=hot_dog_menu)

# korolevskiy     
@dp.callback_query_handler(text='back8888')
async def my_func(call: types.CallbackQuery):
    await call.message.answer("Marhamat menu!\nTanlang...", reply_markup=hot_dog_menu)

# tovuqli_hot_dog     
@dp.callback_query_handler(text='back88888')
async def my_func(call: types.CallbackQuery):
    await call.message.answer("Marhamat menu!\nTanlang...", reply_markup=hot_dog_menu)


# clab_sendvich    
@dp.callback_query_handler(text='back9')
async def my_func(call: types.CallbackQuery):
    await call.message.answer("Marhamat menu!\nTanlang...", reply_markup=main_menu)

# numbers_classik_clab_sandvich16 numbers  
@dp.callback_query_handler(text='back99')
async def my_func(call: types.CallbackQuery):
    await call.message.answer("Marhamat menu!\nTanlang...", reply_markup=clab_sendvich_menu)


# numbers_tovuqli_sandvich17 numbers  
@dp.callback_query_handler(text='back999')
async def my_func(call: types.CallbackQuery):
    await call.message.answer("Marhamat menu!\nTanlang...", reply_markup=clab_sendvich_menu)


# shourma    
@dp.callback_query_handler(text='back0')
async def my_func(call: types.CallbackQuery):
    await call.message.answer("Marhamat menu!\nTanlang...", reply_markup=main_menu)

# mol_gosht_shourma_mini_classik 
@dp.callback_query_handler(text='back00')
async def my_func(call: types.CallbackQuery):
    await call.message.answer("Marhamat menu!\nTanlang...", reply_markup=shourma_menu)

@dp.callback_query_handler(text='back01')
async def my_func(call: types.CallbackQuery):
    await call.message.answer("Marhamat menu!\nTanlang...", reply_markup=mol_gosht_shourma_mini_classik)

@dp.callback_query_handler(text='back000')
async def my_func(call: types.CallbackQuery):
    await call.message.answer("Marhamat menu!\nTanlang...", reply_markup=shourma_menu)

@dp.callback_query_handler(text='back02')
async def my_func(call: types.CallbackQuery):
    await call.message.answer("Marhamat menu!\nTanlang...", reply_markup=tovuq_gosht_shourma_mini_classik)

@dp.callback_query_handler(text='back0000')
async def my_func(call: types.CallbackQuery):
    await call.message.answer("Marhamat menu!\nTanlang...", reply_markup=shourma_menu)

@dp.callback_query_handler(text='back03')
async def my_func(call: types.CallbackQuery):
    await call.message.answer("Marhamat menu!\nTanlang...", reply_markup=mol_gosht_qalampir_shourma_shourma_mini_classik)    

@dp.callback_query_handler(text='back00000')
async def my_func(call: types.CallbackQuery):
    await call.message.answer("Marhamat menu!\nTanlang...", reply_markup=shourma_menu)

@dp.callback_query_handler(text='back04')
async def my_func(call: types.CallbackQuery):
    await call.message.answer("Marhamat menu!\nTanlang...", reply_markup=tovuq_gosht_qalampir_shourma_mini_classik)


# burger    
@dp.callback_query_handler(text='back10')
async def my_func(call: types.CallbackQuery):
    await call.message.answer("Marhamat menu!\nTanlang...", reply_markup=main_menu)

# gamburger numbers 
@dp.callback_query_handler(text='back1010')
async def my_func(call: types.CallbackQuery):
    await call.message.answer("Marhamat menu!\nTanlang...", reply_markup=burger_menu)

# chizburger numbers 
@dp.callback_query_handler(text='back101010')
async def my_func(call: types.CallbackQuery):
    await call.message.answer("Marhamat menu!\nTanlang...", reply_markup=burger_menu)


# donar    
@dp.callback_query_handler(text='back12')
async def my_func(call: types.CallbackQuery):
    await call.message.answer("Marhamat menu!\nTanlang...", reply_markup=main_menu)

# numbers_goshtli_donar22 numbers 
@dp.callback_query_handler(text='back1212')
async def my_func(call: types.CallbackQuery):
    await call.message.answer("Marhamat menu!\nTanlang...", reply_markup=donar_menu)

# tovuqli_donar numbers 
@dp.callback_query_handler(text='back121212')
async def my_func(call: types.CallbackQuery):
    await call.message.answer("Marhamat menu!\nTanlang...", reply_markup=donar_menu)


# gazaklar   
@dp.callback_query_handler(text='back13')
async def my_func(call: types.CallbackQuery):
    await call.message.answer("Marhamat menu!\nTanlang...", reply_markup=main_menu)

# numbers_fry_15_24 numbers 
@dp.callback_query_handler(text='back1313')
async def my_func(call: types.CallbackQuery):
    await call.message.answer("Marhamat menu!\nTanlang...", reply_markup=gazaklar_menu)

# numbers_kartoshka_derevyanski numbers 
@dp.callback_query_handler(text='back131313')
async def my_func(call: types.CallbackQuery):
    await call.message.answer("Marhamat menu!\nTanlang...", reply_markup=gazaklar_menu)

# numbers_gurunch_katta numbers 
@dp.callback_query_handler(text='back13131313')
async def my_func(call: types.CallbackQuery):
    await call.message.answer("Marhamat menu!\nTanlang...", reply_markup=gazaklar_menu)

# numbers_gurunch_kichik numbers 
@dp.callback_query_handler(text='back1313131313')
async def my_func(call: types.CallbackQuery):
    await call.message.answer("Marhamat menu!\nTanlang...", reply_markup=gazaklar_menu)


# ichimliklar_menu    
@dp.callback_query_handler(text='back14')
async def my_func(call: types.CallbackQuery):
    await call.message.answer("Marhamat menu!\nTanlang...", reply_markup=main_menu)

# choylar_kofelar  
@dp.callback_query_handler(text='back144')
async def my_func(call: types.CallbackQuery):
    await call.message.answer("Marhamat menu!\nTanlang...", reply_markup=ichimliklar_menu)

# choy_turlari  
@dp.callback_query_handler(text='back1444')
async def my_func(call: types.CallbackQuery):
    await call.message.answer("Marhamat menu!\nTanlang...", reply_markup=choylar_kofelar)

# kok_choy_numbers  
@dp.callback_query_handler(text='back14444')
async def my_func(call: types.CallbackQuery):
    await call.message.answer("Marhamat menu!\nTanlang...", reply_markup=choy_turlari)

# qora_choy_numbers  
@dp.callback_query_handler(text='back144444')
async def my_func(call: types.CallbackQuery):
    await call.message.answer("Marhamat menu!\nTanlang...", reply_markup=choy_turlari)

# limon_choy_numbers  
@dp.callback_query_handler(text='back1444444')
async def my_func(call: types.CallbackQuery):
    await call.message.answer("Marhamat menu!\nTanlang...", reply_markup=choy_turlari)

# kofe_turlari  
@dp.callback_query_handler(text='back15')
async def my_func(call: types.CallbackQuery):
    await call.message.answer("Marhamat menu!\nTanlang...", reply_markup=ichimliklar_menu)

# kofe_turlari  
@dp.callback_query_handler(text='back155')
async def my_func(call: types.CallbackQuery):
    await call.message.answer("Marhamat menu!\nTanlang...", reply_markup=choylar_kofelar)

# americano_numbers  
@dp.callback_query_handler(text='back1555')
async def my_func(call: types.CallbackQuery):
    await call.message.answer("Marhamat menu!\nTanlang...", reply_markup=kofe_turlari)

# yaxna_ichimliklar  
@dp.callback_query_handler(text='back16')
async def my_func(call: types.CallbackQuery):
    await call.message.answer("Marhamat menu!\nTanlang...", reply_markup=ichimliklar_menu)

# fanta_numbers  
@dp.callback_query_handler(text='back166')
async def my_func(call: types.CallbackQuery):
    await call.message.answer("Marhamat menu!\nTanlang...", reply_markup=yaxna)

# fresh_tabiylar  
@dp.callback_query_handler(text='back177')
async def my_func(call: types.CallbackQuery):
    await call.message.answer("Marhamat menu!\nTanlang...", reply_markup=ichimliklar_menu)

# bliss_numbers numbers  
@dp.callback_query_handler(text='back1777')
async def my_func(call: types.CallbackQuery):
    await call.message.answer("Marhamat menu!\nTanlang...", reply_markup=fresh_tabiylar)


# desertlar_menu  
@dp.callback_query_handler(text='back188')
async def my_func(call: types.CallbackQuery):
    await call.message.answer("Marhamat menu!\nTanlang...", reply_markup=main_menu)

# assalim_numbers  
@dp.callback_query_handler(text='back1888')
async def my_func(call: types.CallbackQuery):
    await call.message.answer("Marhamat menu!\nTanlang...", reply_markup=desertlar_menu)

# pizza_menu  
@dp.callback_query_handler(text='back19')
async def my_func(call: types.CallbackQuery):
    await call.message.answer("Marhamat menu!\nTanlang...", reply_markup=main_menu)

# ananaslik_numbers  
@dp.callback_query_handler(text='back199')
async def my_func(call: types.CallbackQuery):
    await call.message.answer("Marhamat menu!\nTanlang...", reply_markup=pizza_menu)

# backs ===========================================================================

# InlineKeyboardButtons
# lavash
@dp.callback_query_handler(text='lavash')
async def my_func(call: types.CallbackQuery):
    await call.message.answer("✅Marxamat lavashlar menusi!!! ", reply_markup=lavash_menu)

# mol_gosht
@dp.callback_query_handler(text='mol_gosht')
async def my_func(call: types.CallbackQuery):
    await call.message.answer("✅Kategoriyalardan birini tanlang!!! ", reply_markup=mini_classik)

@dp.callback_query_handler(text='mini')
async def my_func(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open("images/lavash_mini.jpg", 'rb'),
        caption="""✅Narxi: 18 000 ming so'm 
Tarkibi:Xamir,go'sht,chips,pomidor,bodring,sous,moyonez
Miqdorini tanlang... """, reply_markup=numbers)

@dp.callback_query_handler(text='classik')
async def my_func(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open("images/lavash_mini.jpg", 'rb'),
        caption="""✅Narxi: 20 000 ming so'm 
Tarkibi: Xamir,go'sht,chips,pomidor,bodring,sous,moyonez
Miqdorini tanlang... """, reply_markup=numbers_classik1)

# qalampir_mol_gosht
@dp.callback_query_handler(text='qalampir_mol_gosht')
async def my_func(call: types.CallbackQuery):
    await call.message.answer("✅Kategoriyalardan birini tanlang!!! ", reply_markup=mini_classik2)

@dp.callback_query_handler(text='mini2')
async def my_func(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo = open("images/qalampir_mini.jpg", 'rb'),
        caption = """✅Narxi: 19 000 ming so'm 
Tarkibi: Xamir, garimdori go'sht,chips,pomidor,bodring,sous,moyonez
Miqdorini tanlang... """, reply_markup=numbers_mini2)

@dp.callback_query_handler(text='classik3')
async def my_func(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo = open("images/qalampir_mini.jpg", 'rb'),
        caption = """Narxi: 20 000 ming so'm 
Tarkibi: Xamir,garimdori go'sht,chips,pomidor,bodring,sous,moyonez
Miqdorini tanlang...""", reply_markup=numbers_classik3)

# tovuq_gosht
@dp.callback_query_handler(text='tovuq_gosht')
async def my_func(call: types.CallbackQuery):
    await call.message.answer("✅Kategoriyalardan birini tanlang!!! ", reply_markup=mini_classik4)

@dp.callback_query_handler(text='mini4')
async def my_func(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo = open("images/tovuq_mini.jpg", 'rb'),
        caption = """✅Narxi: 19 000 ming so'm 
Tarkibi: Xamir,tovuq go'sht,chips,pomidor,bodring,sous,moyonez
Miqdorini tanlang...""", reply_markup=numbers_mini4)

@dp.callback_query_handler(text='classik5')
async def my_func(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo = open("images/tovuq_mini.jpg", 'rb'),
        caption = """✅Narxi: 22 000 ming so'm 
Tarkibi: Xamir,tovuq go'sht,chips,pomidor,bodring,sous,moyonez
Miqdorini tanlang... """, reply_markup=numbers_classik5)

# qalampir_tovuq_gosht
@dp.callback_query_handler(text='qalampir_tovuq_gosht')
async def my_func(call: types.CallbackQuery):
    await call.message.answer("✅Kategoriyalardan birini tanlang!!! ", reply_markup=mini_classik6)

@dp.callback_query_handler(text='mini6')
async def my_func(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo = open("images/tovuq_qalampir_mini.jpg", 'rb'),
        caption = """✅Narxi: 17 000 ming so'm 
Tarkibi: Xamir,garimdori,tovuq go'sht,chips,pomidor,bodring,sous,moyonez
Miqdorini tanlang... """, reply_markup=numbers_mini6)

@dp.callback_query_handler(text='classik7')
async def my_func(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo = open("images/tovuq_qalampir_mini.jpg", 'rb'),
        caption = """✅Narxi: 20 000 ming so'm 
Tarkibi:Xamir,garimdori tovuq go'sht,chips,pomidor,bodring,sous,moyonez
Miqdorini tanlang... """, reply_markup=numbers_classik7)

# pishloq_mol_gosht
@dp.callback_query_handler(text='pishloq_mol_gosht')
async def my_func(call: types.CallbackQuery):
    await call.message.answer("✅Kategoriyalardan birini tanlang!!! ", reply_markup=mini_classik8)

@dp.callback_query_handler(text='mini8')
async def my_func(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo = open("images/pishloq_mol.jpg", 'rb'),
        caption = """✅Narxi: 18 000 ming so'm 
Tarkibi: Pishloq, xamir,mol go'sht,pishloq,chips,pomidor,bodring,sous,moyonez
Miqdorini tanlang... """, reply_markup=numbers_mini8)

@dp.callback_query_handler(text='classik9')
async def my_func(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo = open("images/pishloq_mol.jpg", 'rb'),
        caption = """✅Narxi:20 000 ming so'm 
Tarkibi: Pishloq,xamir,mol go'sht,pishloq,chips,pomidor,bodring,sous,moyonez
Miqdorini tanlang """, reply_markup=numbers_classik9)

# pishloq_tovuq_gosht
@dp.callback_query_handler(text='pishloq_tovuq_gosht')
async def my_func(call: types.CallbackQuery):
    await call.message.answer("✅Kategoriyalardan birini tanlang!!! ", reply_markup=mini_classik10)

@dp.callback_query_handler(text='mini10')
async def my_func(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo = open("images/pishloq_tovuq.jpg", 'rb'),
        caption = """✅Narxi: 18 000 ming so'm 
Tarkibi:Xamir,tovuq go'sht,pishloq,chips,pomidor,bodring,sous,moyonez
Miqdorini tanlang... """, reply_markup=numbers_mini10)

@dp.callback_query_handler(text='classik11')
async def my_func(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo = open("images/pishloq_tovuq.jpg", 'rb'),
        caption = """✅Narxi: 20 000 ming so'm 
Tarkibi:Xamir,tovuq go'sht,pishloq,chips,pomidor,bodring,sous,moyonez
Miqdorini tanlang... """, reply_markup=numbers_classik11)

# flitter
@dp.callback_query_handler(text='flitter')
async def my_func(call: types.CallbackQuery):
    await call.message.answer("✅Kategoriyalardan birini tanlang!!! ", reply_markup=mini_classik12)

@dp.callback_query_handler(text='mini12')
async def my_func(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo = open("images/pishloq_tovuq.jpg", 'rb'),
        caption = """✅Narxi: 19 000 ming so'm 
Tarkibi: Xamir, qarsildoq muztogʼ salati,chips,pomidor,bodring,sous,moyonez
Miqdorini tanlang...""", reply_markup=numbers_mini12)

@dp.callback_query_handler(text='classik13')
async def my_func(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo = open("images/pishloq_tovuq.jpg", 'rb'),
        caption = """✅Narxi: 21 000 ming so'm 
Tarkibi: Xamir, qarsildoq muztogʼ salati,chips,pomidor,bodring,sous,moyonez
Miqdorini tanlang...""", reply_markup=numbers_classik13)

# hot-dog
@dp.callback_query_handler(text='hot-dog')
async def my_func(call: types.CallbackQuery):
    await call.message.answer("✅Marxamat hot-doglar menusi!!! ", reply_markup=hot_dog_menu)

# hot_dog_baget_dabl
@dp.callback_query_handler(text='hot_dog_baget_dabl')
async def my_func(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo = open("images/hot_dog_dabl.jpg", 'rb'),
        caption = """✅Narxi: 18 000 ming so'm 
Tarkibi: Kulcha,sosiska 2x,ketchup va xantal,qovurilgan piyoz.
Miqdorini tanlang... """, reply_markup=numbers_hot_dog_baget_dabl14)

# classik_hot_dog
@dp.callback_query_handler(text='classik_hot_dog')
async def my_func(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo = open("images/hot_dog_classik.jpg", 'rb'),
        caption = """✅Narxi: 8 000 ming so'm 
Tarkibi: Kulcha,sosiska,ketchup va xantal,qovurilgan piyoz.
Miqdorini tanlang... """, reply_markup=numbers_classik_hot_dog15)

# korolevskiy
@dp.callback_query_handler(text='korolevskiy')
async def my_func(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo = open("images/hot_dog_korolevski.jpg", 'rb'),
        caption = """✅Narxi: 15 000 ming so'm 
Tarkibi Kulcha,sosiska,ketchup va xantal,qovurilgan piyoz.
Miqdorini tanlang... """, reply_markup=numbers_classik_hot_dog15)

# tovuqli_hot_dog
@dp.callback_query_handler(text='tovuqli_hot_dog')
async def my_func(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo = open("images/hot_dog_tovuqli.jpg", 'rb'),
        caption = """✅Narxi: 17 000 ming so'm 
Tarkibi: Kulcha,sosiska,ketchup va xantal,qovurilgan piyoz.
Miqdorini tanlang... """, reply_markup=numbers_classik_hot_dog15)

# clab_sendvich
@dp.callback_query_handler(text='clab_sendvich')
async def my_func(call: types.CallbackQuery):
    await call.message.answer("✅Marxamat Clab Sendvichlar menusi!!! ", reply_markup=clab_sendvich_menu)

# classik_clab_sandvich
@dp.callback_query_handler(text='classik_clab_sandvich')
async def my_func(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo = open("images/sendvich_classik.jpg", 'rb'),
        caption = """✅Narxi: 22 000 ming so'm 
Tarkibi: Kulcha, tovuq go'shti, pomidor, sous,  piyoz.
Miqdorini tanlang... """, reply_markup=numbers_classik_clab_sandvich16)

# tovuqli_sandvich
@dp.callback_query_handler(text='tovuqli_sandvich')
async def my_func(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo = open("images/sendvich_classik.jpg", 'rb'),
        caption = """✅Narxi: 24 000 ming so'm 
Tarkibi: Kulcha, tovuq go'shti, pomidor, sous,  piyoz.
Miqdorini tanlang...""", reply_markup=numbers_tovuqli_sandvich17)

# shourma
@dp.callback_query_handler(text='shourma')
async def my_func(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo = open("images/shourma.jpg", 'rb'),
        caption = "✅Marxamat Shourmalar menusi!!! ", reply_markup=shourma_menu)

# mol_gosht_shourma
@dp.callback_query_handler(text='mol_gosht_shourma')
async def my_func(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo = open("images/shourma_mol.jpg", 'rb'),
        caption = """✅Kategoriyalardan birini tanlang...""", reply_markup=mol_gosht_shourma_mini_classik)

@dp.callback_query_handler(text='minis')
async def my_func(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo = open("images/shourma_mol.jpg", 'rb'),
        caption = """✅Narxi: 18 000 ming so'm
Kulcha, mol go'sht, pomidor, sous,  piyoz. 
Miqdorini tanlang... """, reply_markup=numbers_shourma1)

@dp.callback_query_handler(text='classiks')
async def my_func(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo = open("images/shourma_mol.jpg", 'rb'),
        caption = """✅Narxi: 22 000 ming so'm
Kulcha, mol go'sht, pomidor, sous,  piyoz. 
Miqdorini tanlang... """, reply_markup=numbers_shourma1)

# tovuq_gosht_shourma
@dp.callback_query_handler(text='tovuq_gosht_shourma')
async def my_func(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo = open("images/shourma_tovuq.jpg", 'rb'),
        caption = """✅Kategoriyalardan birini tanlang...""", reply_markup=tovuq_gosht_shourma_mini_classik)

@dp.callback_query_handler(text='miniss')
async def my_func(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo = open("images/shourma_tovuq.jpg", 'rb'),
        caption = """✅Narxi: 17 000 ming so'm
Kulcha, tovuq go'sht, pomidor, sous,  piyoz. 
Miqdorini tanlang...""", reply_markup=numbers_shourma2)

@dp.callback_query_handler(text='classikss')
async def my_func(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo = open("images/shourma_tovuq.jpg", 'rb'),
        caption = """✅Narxi: 20 000 ming so'm
Kulcha, tovuq go'sht, pomidor, sous,  piyoz. 
Miqdorini tanlang...""", reply_markup=numbers_shourma2)

# mol_gosht_qalampir_shourma
@dp.callback_query_handler(text='mol_gosht_qalampir_shourma')
async def my_func(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo = open("images/shourma_mol.jpg", 'rb'),
        caption = """✅Kategoriyalardan birini tanlang...""", reply_markup=mol_gosht_qalampir_shourma_shourma_mini_classik)

@dp.callback_query_handler(text='minisss')
async def my_func(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo = open("images/shourma_mol.jpg", 'rb'),
        caption = """✅Narxi: 23 000 ming so'm
Kulcha, mol go'sht, pomidor, sous,  piyoz. 
Miqdorini tanlang...""", reply_markup=numbers_shourma3)

@dp.callback_query_handler(text='classiksss')
async def my_func(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo = open("images/shourma_mol.jpg", 'rb'),
        caption = """✅Narxi: 25 000 ming so'm
Kulcha, mol go'sht, pomidor, sous,  piyoz. 
Miqdorini tanlang...""", reply_markup=numbers_shourma3)

# tovuq_gosht_qalampir_shourma
@dp.callback_query_handler(text='tovuq_gosht_qalampir_shourma')
async def my_func(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo = open("images/shourma_tovuq.jpg", 'rb'),
        caption = """✅Kategoriyalardan birini tanlang...""", reply_markup=tovuq_gosht_qalampir_shourma_mini_classik)

@dp.callback_query_handler(text='minissss')
async def my_func(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo = open("images/shourma_tovuq.jpg", 'rb'),
        caption = """✅Narxi: 20 000 ming so'm
Kulcha, tovuq go'sht, garimdori, pomidor, sous,  piyoz. 
Miqdorini tanlang... """, reply_markup=numbers_shourma4)

@dp.callback_query_handler(text='classikssss')
async def my_func(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo = open("images/shourma_tovuq.jpg", 'rb'),
        caption = """✅Narxi: 24 000 ming so'm
Kulcha, tovuq go'sht,garimdori, pomidor, sous,  piyoz. 
Miqdorini tanlang... """, reply_markup=numbers_shourma4)

# burger
@dp.callback_query_handler(text='burger')
async def my_func(call: types.CallbackQuery):
    await call.message.answer("✅Marxamat Burgerlar menusi!!! ", reply_markup=burger_menu)

# gamburger
@dp.callback_query_handler(text='gamburger')
async def my_func(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo = open("images/burger_gamburger.jpg", 'rb'),
        caption = """✅Narxi: 22 000 ming so'm 
Miqdorini tanlang... """, reply_markup=numbers_gamburger20)

# chizburger
@dp.callback_query_handler(text='chizburger')
async def my_func(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo = open("images/burger_chizburger.jpg", 'rb'),
        caption = """✅Narxi: 20 000 ming so'm 
Miqdorini tanlang... """, reply_markup=numbers_chizburger21)

# donar
@dp.callback_query_handler(text='donar')
async def my_func(call: types.CallbackQuery):
    await call.message.answer("✅Marxamat Donarlar menusi!!! ", reply_markup=donar_menu)

# goshtli_donar
@dp.callback_query_handler(text='goshtli_donar')
async def my_func(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo = open("images/donar_goshtli.jpg", 'rb'),
        caption = """✅Narxi: 23 000 ming so'm 
Tarkib: Kulcha, mol go'sht, pomidor, sous,  piyoz.    
Miqdorini tanlang...""", reply_markup=numbers_goshtli_donar22)

# tovuqli_donar
@dp.callback_query_handler(text='tovuqli_donar')
async def my_func(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo = open("images/donar_tovuqli.jpg", 'rb'),
        caption = """✅Narxi: 23 000 ming so'm 
Tarkib: Kulcha, tovuq go'sht, pomidor, sous, piyoz.     
Miqdorini tanlang... """, reply_markup=numbers_tovuqli_donar23)

# gazaklar
@dp.callback_query_handler(text='gazaklar')
async def my_func(call: types.CallbackQuery):
    await call.message.answer("✅Marxamat Fries menusi!!! ", reply_markup=gazaklar_menu)

# fry_15
@dp.callback_query_handler(text='fry_15')
async def my_func(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo = open("images/gazaklar_fry.jpg", 'rb'),
        caption = """✅Narxi: 6 000 ming so'm 
Tarkib: kartoshka, sous....   
Miqdorini tanlang...""", reply_markup=numbers_fry_15)

# kartoshka_derevyanski
@dp.callback_query_handler(text='kartoshka_derevyanski')
async def my_func(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo = open("images/gazaklar_derevyanski.jpg", 'rb'),
        caption = """✅Narxi: 10 000 ming so'm
Tarkib: kartoshka, sous...      
Miqdorini tanlang...""", reply_markup=numbers_kartoshka_derevyanski)

# gurunch_katta
@dp.callback_query_handler(text='gurunch_katta')
async def my_func(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo = open("images/gazaklar_gurunch_katta.jpg", 'rb'),
        caption = """✅Narxi: 8 000 ming so'm
Tarkib: gurunch, salat bargi, sous...     
Miqdorini tanlang...""", reply_markup=numbers_gurunch_katta)

# gurunch_kichik
@dp.callback_query_handler(text='gurunch_kichik')
async def my_func(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo = open("images/gazaklar_gurunch_katta.jpg", 'rb'),
        caption = """✅Narxi: 10 000 ming so'm
Tarkib: gurunch, salat bargi, sous...     
Miqdorini tanlang...""", reply_markup=numbers_gurunch_kichik)

# 04.05.2023
# ichimliklar
@dp.callback_query_handler(text='ichimliklar')
async def my_func(call: types.CallbackQuery):
    await call.message.answer("✅Marxamat Ichimliklar menusi!!! ", reply_markup=ichimliklar_menu)

# choy_kofe
@dp.callback_query_handler(text='choy_kofe')
async def my_func(call: types.CallbackQuery):
    await call.message.answer("""✅Kategoriyalardan birini tanlang!!! """, reply_markup=choylar_kofelar)

# choylar
@dp.callback_query_handler(text='choylar')
async def my_func(call: types.CallbackQuery):
    await call.message.answer("""✅Kategoriyalardan birini tanlang!!! """, reply_markup=choy_turlari)

# kok_choy
@dp.callback_query_handler(text='kok_choy')
async def my_func(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo = open("images/ichimliklar_kok.jpg", 'rb'),
        caption = """✅Ko'k choy \nNarxi: 3 000 so'm! """, reply_markup=kok_choy_numbers)

# qora_choy
@dp.callback_query_handler(text='qora_choy')
async def my_func(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo = open("images/ichimliklar_kok.jpg", 'rb'),
        caption = """✅Qora choy \nNarxi: 3 000 so'm! """, reply_markup=qora_choy_numbers)

# limon_choy
@dp.callback_query_handler(text='limon_choy')
async def my_func(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo = open("images/ichimliklar_limon.jpg", 'rb'),
        caption = """✅Limon choy \nNarxi: 5 000 so'm! """, reply_markup=limon_choy_numbers)

# kofelar
@dp.callback_query_handler(text='kofelar')
async def my_func(call: types.CallbackQuery):
    await call.message.answer("""✅Kategoriyalardan birini tanlang!!! """, reply_markup=kofe_turlari)

# americano
@dp.callback_query_handler(text='americano')
async def my_func(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo = open("images/ichimliklar_americano.jpg", 'rb'),
        caption = """✅Americano \nNarxi: 12 000 so'm! """, reply_markup=americano_numbers)

# cappuccino
@dp.callback_query_handler(text='cappuccino')
async def my_func(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo = open("images/ichimliklar_cappucino.jpg", 'rb'),
        caption = """✅Cappuccino \nNarxi: 18 000 so'm! """, reply_markup=americano_numbers)

# cofe_3v1
@dp.callback_query_handler(text='cofe_3v1')
async def my_func(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo = open("images/ichimliklar_3v1.jpg", 'rb'),
        caption = """✅Cofe 3v1 \nNarxi: 3 000 so'm! """, reply_markup=americano_numbers)

# latte
@dp.callback_query_handler(text='latte')
async def my_func(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo = open("images/ichimliklar_latte.jpg", 'rb'),
        caption = """✅Latte big 120g☕️\nNarxi: 15 000 so'm! """, reply_markup=americano_numbers)

# yaxna_ichimliklar
@dp.callback_query_handler(text='yaxna_ichimliklar')
async def my_func(call: types.CallbackQuery):
    await call.message.answer("✅Kategoriyalardan birini tanlang! ", reply_markup=yaxna)

# fanta
@dp.callback_query_handler(text='fanta')
async def my_func(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo = open("images/ichimliklar_fanta.jpg", 'rb'),
        caption = """✅Fanta\nNarxi: 11 000 so'm! """, reply_markup=fanta_numbers)

# sprite
@dp.callback_query_handler(text='sprite')
async def my_func(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo = open("images/ichimliklar_sprite.jpg", 'rb'),
        caption = """✅Sprite\nNarxi: 13 000 so'm! """, reply_markup=fanta_numbers)

# cola
@dp.callback_query_handler(text='cola')
async def my_func(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo = open("images/ichimliklar_cola.jpg", 'rb'),
        caption = """✅Coca Cola\nNarxi: 12 000 so'm! """, reply_markup=fanta_numbers)

# nestle
@dp.callback_query_handler(text='nestle')
async def my_func(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo = open("images/ichimliklar_nestle.jpg", 'rb'),
        caption = """✅Nestle\nNarxi: 4 000 so'm! """, reply_markup=fanta_numbers)

# fresh_tabiy
@dp.callback_query_handler(text='fresh_tabiy')
async def my_func(call: types.CallbackQuery):
    await call.message.answer("""✅Kategoriyalardan birini tanlang!""", reply_markup=fresh_tabiylar)

# bliss
@dp.callback_query_handler(text='bliss')
async def my_func(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo = open("images/ichimliklar_bliss.jpg", 'rb'),
        caption = """✅Sok Bliss\nNarxi: 10 000 so'm! """, reply_markup=bliss_numbers)

# olma_sabzi
@dp.callback_query_handler(text='olma_sabzi')
async def my_func(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo = open("images/ichimliklar_fresh.jpg", 'rb'),
        caption = """✅Fresh sabzi + olma\nNarxi: 13 000 so'm! """, reply_markup=bliss_numbers)

# desertlar
@dp.callback_query_handler(text='desertlar')
async def my_func(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo = open("images/desertlar.jpg", 'rb'),
        caption = "✅Marxamat Desertlar menusi!!! ", reply_markup=desertlar_menu)

# assalim
@dp.callback_query_handler(text='assalim')
async def my_func(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo = open("images/desertlar_assalim.jpg", 'rb'),
        caption = """✅Narxi: 14 000 so'm 
Аnʼnaviy taʼm - asal asosidagi biskvit va krem
Miqdorini tanlang""", reply_markup=assalim_numbers)

# qulupnay
@dp.callback_query_handler(text='qulupnay')
async def my_func(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo = open("images/desertlar_qulupnay.jpg", 'rb'),
        caption = """✅Narxi: 15 000 so'm 
Qulupnayli Muss.
Miqdorini tanlang""", reply_markup=assalim_numbers)

# choko
@dp.callback_query_handler(text='choko')
async def my_func(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo = open("images/desertlar_choko.jpg", 'rb'),
        caption = """✅Narxi: 17 000 ming so'm 
Аnʼnaviy taʼm - shokolat asosidagi biskvit va krem.
Miqdorini tanlangg""", reply_markup=assalim_numbers)

# pizza
@dp.callback_query_handler(text='pizza')
async def my_func(call: types.CallbackQuery):
    await call.message.answer("✅Marxamat Pizzalar menusi!!! ", reply_markup=pizza_menu)

# ananaslik
@dp.callback_query_handler(text='ananaslik')
async def my_func(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo = open("images/pizza_ananaslik.jpg", 'rb'),
        caption = """✅Narxi: 65 000 so'm 
Пицца с Ананасом.
Пицца с Колбасой     33см.
Соус Томатный Для Пиццы
3 вида колбас 130гр.
Тонкое тесто
Кукуруза
Сыр 100гр.
ГрибыMiqdorini tanlang...""", reply_markup=ananaslik_numbers)

# peperoni
@dp.callback_query_handler(text='peperoni')
async def my_func(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo = open("images/pizza_peperoni.jpg", 'rb'),
        caption = """✅Narxi: 75 000 ming so'm 
Пицца Пепперони
Пицца Пепперони     33см.
Соус Томатный Для Пиццы
Тонкое тесто.
Сыр 110 гр.
Miqdorini tanlang...""", reply_markup=ananaslik_numbers)

# margaritta
@dp.callback_query_handler(text='margaritta')
async def my_func(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo = open("images/pizza_margaritta.jpg", 'rb'),
        caption = """✅Narxi: 60 000 ming so'm 
Пицца Маргарита
Пицца Маргарита  33см.
Соус Томатный Для Пиццы 
Тонкое тесто 
Сыр 100гр.
Помидоры
Miqdorini tanlang...""", reply_markup=ananaslik_numbers)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)



# https://t.me/evos_user_bot this bot can be used 
# completed on 11.05.2023  

