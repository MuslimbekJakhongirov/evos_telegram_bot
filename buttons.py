
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup

# buttons for choosing language
language = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton("🇺🇿 O'zbekcha"),
            KeyboardButton("🇷🇺 Ruscha"),
            KeyboardButton("🇬🇧 Inglizcha")   
        ]
    ],
    resize_keyboard=True
)

# button for phone number
phone_number = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton("📞 Telefon raqamni yuborish!", request_contact=True)  
        ]
    ],
    resize_keyboard=True
)

# button for location
location = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton("📍 Joylashuvni yuborish!", request_location=True)  
        ]
    ],
    resize_keyboard=True
)

# buttons for user menu
below_menu = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton("Buyurtma berish! 🧑‍💻")  
        ],
        [
            KeyboardButton("Sozlamalar! 🛠"),
            KeyboardButton("Biz bilan bog'lanish! ☎️")
        ]
    ],
    resize_keyboard=True
)

# InlineKeyboardButton
# main menu
main_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = "Lavash  🌯🌯", callback_data="lavash"),
            InlineKeyboardButton(text = "Hot-dog  🌭🌭", callback_data="hot-dog")
        ],
        [
            InlineKeyboardButton(text = "Clab Sendvich  🥪🥪", callback_data="clab_sendvich"),
            InlineKeyboardButton(text = "Shourma  🌮🌮", callback_data="shourma")
        ],
        [
            InlineKeyboardButton(text = "Burger  🍔🍔", callback_data="burger"),
            InlineKeyboardButton(text = "Donar  🍱🍱", callback_data="donar")
        ],
        [
            InlineKeyboardButton(text = "Gazaklar  🍟🍟", callback_data="gazaklar"),
            InlineKeyboardButton(text = "Ichimliklar  🍹🍹", callback_data="ichimliklar")
        ],
        [
            InlineKeyboardButton(text = "Desertlar  🍰🍰", callback_data="desertlar"),
            InlineKeyboardButton(text = "Pizza  🍕🍕", callback_data="pizza")
        ]
    ]
)

# lavash menu
lavash_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Mol go'shtlik  🥩", callback_data='mol_gosht'),
            InlineKeyboardButton(text="Qalampirli mol go'sht  🥩🌶", callback_data='qalampir_mol_gosht')
        ],
        [
            InlineKeyboardButton(text="Tovuq go'shtlik  🍗", callback_data='tovuq_gosht'),
            InlineKeyboardButton(text="Qalampirli tovuq go'sht  🍗🌶", callback_data='qalampir_tovuq_gosht'),
        ],
        [
            InlineKeyboardButton(text="Pishloqli mol go'shtidan  🥩🧀", callback_data='pishloq_mol_gosht'),
            InlineKeyboardButton(text="Pishloqli tovuq go'shtidan  🍗🧀", callback_data='pishloq_tovuq_gosht'),
        ],
        [
            InlineKeyboardButton(text="Flitter  🥬", callback_data='flitter')
        ],
        [
            InlineKeyboardButton(text="⬅️ Ortga", callback_data='back')
        ]
      
    ]
)

# mol gosht mini_classik
mini_classik = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Mini  👍", callback_data='mini'),
            InlineKeyboardButton(text="Classik  👍", callback_data='classik')
        ],
        [
            InlineKeyboardButton(text="⬅️ Ortga", callback_data='back11')
        ]
    ]
)

# mol gosht numbers mini
numbers = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="1⃣", callback_data='one'),
            InlineKeyboardButton(text="2⃣", callback_data='two'),
            InlineKeyboardButton(text="3⃣", callback_data='three')
        ],
        [
            InlineKeyboardButton(text="4⃣", callback_data='four'),
            InlineKeyboardButton(text="5⃣", callback_data='five'),
            InlineKeyboardButton(text="6⃣", callback_data='six')
        ],
        [
            InlineKeyboardButton(text="7⃣", callback_data='seven'),
            InlineKeyboardButton(text="8⃣", callback_data='eight'),
            InlineKeyboardButton(text="9⃣", callback_data='nine')
        ],
        [
            InlineKeyboardButton(text="⬅️ Ortga", callback_data='back111')
        ]
      
    ]
)

# order
order = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="☎️ Raqam qoldiring!", callback_data='order_phone'),
            InlineKeyboardButton(text="🏘 Manzilini qoldiring!", callback_data='order_location')
        ],
    ]
)

# mol gosht numbers classik
numbers_classik1 = InlineKeyboardMarkup(
    inline_keyboard=[
       [
            InlineKeyboardButton(text="1⃣", callback_data='one'),
            InlineKeyboardButton(text="2⃣", callback_data='two'),
            InlineKeyboardButton(text="3⃣", callback_data='three')
        ],
        [
            InlineKeyboardButton(text="4⃣", callback_data='four'),
            InlineKeyboardButton(text="5⃣", callback_data='five'),
            InlineKeyboardButton(text="6⃣", callback_data='six')
        ],
        [
            InlineKeyboardButton(text="7⃣", callback_data='seven'),
            InlineKeyboardButton(text="8⃣", callback_data='eight'),
            InlineKeyboardButton(text="9⃣", callback_data='nine')
        ],
        [
            InlineKeyboardButton(text="⬅️ Ortga", callback_data='back1111')
        ]
      
    ]
)

# qalampirli mol gosht mini_classik
mini_classik2 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Mini  👍", callback_data='mini2'),
            InlineKeyboardButton(text="Classik  👍", callback_data='classik3')
        ],
        [
            InlineKeyboardButton(text="⬅️ Ortga", callback_data='back2')
        ]
    ]
)

# qalampir mol gosht numbers mini
numbers_mini2 = InlineKeyboardMarkup(
    inline_keyboard=[
       [
            InlineKeyboardButton(text="1⃣", callback_data='one'),
            InlineKeyboardButton(text="2⃣", callback_data='two'),
            InlineKeyboardButton(text="3⃣", callback_data='three')
        ],
        [
            InlineKeyboardButton(text="4⃣", callback_data='four'),
            InlineKeyboardButton(text="5⃣", callback_data='five'),
            InlineKeyboardButton(text="6⃣", callback_data='six')
        ],
        [
            InlineKeyboardButton(text="7⃣", callback_data='seven'),
            InlineKeyboardButton(text="8⃣", callback_data='eight'),
            InlineKeyboardButton(text="9⃣", callback_data='nine')
        ],
        [
            InlineKeyboardButton(text="⬅️ Ortga", callback_data='back22')
        ]
      
    ]
)

# order
order = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="☎️ Raqam qoldiring!", callback_data='order_phone'),
            InlineKeyboardButton(text="🏘 Manzilini qoldiring!", callback_data='order_location')
        ],
    ]
)

# qalampir mol gosht numbers classik
numbers_classik3 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="1⃣", callback_data='one'),
            InlineKeyboardButton(text="2⃣", callback_data='two'),
            InlineKeyboardButton(text="3⃣", callback_data='three')
        ],
        [
            InlineKeyboardButton(text="4⃣", callback_data='four'),
            InlineKeyboardButton(text="5⃣", callback_data='five'),
            InlineKeyboardButton(text="6⃣", callback_data='six')
        ],
        [
            InlineKeyboardButton(text="7⃣", callback_data='seven'),
            InlineKeyboardButton(text="8⃣", callback_data='eight'),
            InlineKeyboardButton(text="9⃣", callback_data='nine')
        ],
        [
            InlineKeyboardButton(text="⬅️ Ortga", callback_data='back222')
        ]
      
    ]
)

# tovuq goshtlik mini_classik
mini_classik4 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Mini  👍", callback_data='mini4'),
            InlineKeyboardButton(text="Classik  👍", callback_data='classik5')
        ],
        [
            InlineKeyboardButton(text="⬅️ Ortga", callback_data='back3')
        ]
    ]
)

# tovuqli numbers mini
numbers_mini4 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="1⃣", callback_data='one'),
            InlineKeyboardButton(text="2⃣", callback_data='two'),
            InlineKeyboardButton(text="3⃣", callback_data='three')
        ],
        [
            InlineKeyboardButton(text="4⃣", callback_data='four'),
            InlineKeyboardButton(text="5⃣", callback_data='five'),
            InlineKeyboardButton(text="6⃣", callback_data='six')
        ],
        [
            InlineKeyboardButton(text="7⃣", callback_data='seven'),
            InlineKeyboardButton(text="8⃣", callback_data='eight'),
            InlineKeyboardButton(text="9⃣", callback_data='nine')
        ],
        [
            InlineKeyboardButton(text="⬅️ Ortga", callback_data='back33')
        ]
      
    ]
)

# order
order = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="☎️ Raqam qoldiring!", callback_data='order_phone'),
            InlineKeyboardButton(text="🏘 Manzilini qoldiring!", callback_data='order_location')
        ],
    ]
)

# tovuqlik numbers classik
numbers_classik5 = InlineKeyboardMarkup(
    inline_keyboard=[
      [
            InlineKeyboardButton(text="1⃣", callback_data='one'),
            InlineKeyboardButton(text="2⃣", callback_data='two'),
            InlineKeyboardButton(text="3⃣", callback_data='three')
        ],
        [
            InlineKeyboardButton(text="4⃣", callback_data='four'),
            InlineKeyboardButton(text="5⃣", callback_data='five'),
            InlineKeyboardButton(text="6⃣", callback_data='six')
        ],
        [
            InlineKeyboardButton(text="7⃣", callback_data='seven'),
            InlineKeyboardButton(text="8⃣", callback_data='eight'),
            InlineKeyboardButton(text="9⃣", callback_data='nine')
        ],
        [
            InlineKeyboardButton(text="⬅️ Ortga", callback_data='back333')
        ]
      
    ]
)

# qalampirli tovuq goshtlik mini_classik
mini_classik6 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Mini  👍", callback_data='mini6'),
            InlineKeyboardButton(text="Classik  👍", callback_data='classik7')
        ],
        [
            InlineKeyboardButton(text="⬅️ Ortga", callback_data='back4')
        ]
    ]
)

# qalampir tovuqli numbers mini
numbers_mini6 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="1⃣", callback_data='one'),
            InlineKeyboardButton(text="2⃣", callback_data='two'),
            InlineKeyboardButton(text="3⃣", callback_data='three')
        ],
        [
            InlineKeyboardButton(text="4⃣", callback_data='four'),
            InlineKeyboardButton(text="5⃣", callback_data='five'),
            InlineKeyboardButton(text="6⃣", callback_data='six')
        ],
        [
            InlineKeyboardButton(text="7⃣", callback_data='seven'),
            InlineKeyboardButton(text="8⃣", callback_data='eight'),
            InlineKeyboardButton(text="9⃣", callback_data='nine')
        ],
        [
            InlineKeyboardButton(text="⬅️ Ortga", callback_data='back44')
        ]
      
    ]
)

# order
order = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="☎️ Raqam qoldiring!", callback_data='order_phone'),
            InlineKeyboardButton(text="🏘 Manzilini qoldiring!", callback_data='order_location')
        ],
    ]
)

# qalampir tovuqlik numbers classik
numbers_classik7 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="1⃣", callback_data='one'),
            InlineKeyboardButton(text="2⃣", callback_data='two'),
            InlineKeyboardButton(text="3⃣", callback_data='three')
        ],
        [
            InlineKeyboardButton(text="4⃣", callback_data='four'),
            InlineKeyboardButton(text="5⃣", callback_data='five'),
            InlineKeyboardButton(text="6⃣", callback_data='six')
        ],
        [
            InlineKeyboardButton(text="7⃣", callback_data='seven'),
            InlineKeyboardButton(text="8⃣", callback_data='eight'),
            InlineKeyboardButton(text="9⃣", callback_data='nine')
        ],
        [
            InlineKeyboardButton(text="⬅️ Ortga", callback_data='back444')
        ]
      
    ]
)

# pishloqli gosht mini_classik
mini_classik8 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Mini  👍", callback_data='mini8'),
            InlineKeyboardButton(text="Classik  👍", callback_data='classik9')
        ],
        [
            InlineKeyboardButton(text="⬅️ Ortga", callback_data='back5')
        ]
    ]
)

# pishloqli mol numbers mini
numbers_mini8 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="1⃣", callback_data='one'),
            InlineKeyboardButton(text="2⃣", callback_data='two'),
            InlineKeyboardButton(text="3⃣", callback_data='three')
        ],
        [
            InlineKeyboardButton(text="4⃣", callback_data='four'),
            InlineKeyboardButton(text="5⃣", callback_data='five'),
            InlineKeyboardButton(text="6⃣", callback_data='six')
        ],
        [
            InlineKeyboardButton(text="7⃣", callback_data='seven'),
            InlineKeyboardButton(text="8⃣", callback_data='eight'),
            InlineKeyboardButton(text="9⃣", callback_data='nine')
        ],
        [
            InlineKeyboardButton(text="⬅️ Ortga", callback_data='back55')
        ]
      
    ]
)

# order
order = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="☎️ Raqam qoldiring!", callback_data='order_phone'),
            InlineKeyboardButton(text="🏘 Manzilini qoldiring!", callback_data='order_location')
        ],
    ]
)

# pishloqli mol numbers classik
numbers_classik9 = InlineKeyboardMarkup(
    inline_keyboard=[
       [
            InlineKeyboardButton(text="1⃣", callback_data='one'),
            InlineKeyboardButton(text="2⃣", callback_data='two'),
            InlineKeyboardButton(text="3⃣", callback_data='three')
        ],
        [
            InlineKeyboardButton(text="4⃣", callback_data='four'),
            InlineKeyboardButton(text="5⃣", callback_data='five'),
            InlineKeyboardButton(text="6⃣", callback_data='six')
        ],
        [
            InlineKeyboardButton(text="7⃣", callback_data='seven'),
            InlineKeyboardButton(text="8⃣", callback_data='eight'),
            InlineKeyboardButton(text="9⃣", callback_data='nine')
        ],
        [
            InlineKeyboardButton(text="⬅️ Ortga", callback_data='back555')
        ]
      
    ]
)

# pishloq_tovuq_gosht mini_classik
mini_classik10 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Mini  👍", callback_data='mini10'),
            InlineKeyboardButton(text="Classik  👍", callback_data='classik11')
        ],
        [
            InlineKeyboardButton(text="⬅️ Ortga", callback_data='back6')
        ]
    ]
)

# pishloqli tovuq numbers mini
numbers_mini10 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="1⃣", callback_data='one'),
            InlineKeyboardButton(text="2⃣", callback_data='two'),
            InlineKeyboardButton(text="3⃣", callback_data='three')
        ],
        [
            InlineKeyboardButton(text="4⃣", callback_data='four'),
            InlineKeyboardButton(text="5⃣", callback_data='five'),
            InlineKeyboardButton(text="6⃣", callback_data='six')
        ],
        [
            InlineKeyboardButton(text="7⃣", callback_data='seven'),
            InlineKeyboardButton(text="8⃣", callback_data='eight'),
            InlineKeyboardButton(text="9⃣", callback_data='nine')
        ],
        [
            InlineKeyboardButton(text="⬅️ Ortga", callback_data='back66')
        ]
      
    ]
)

# order
order = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="☎️ Raqam qoldiring!", callback_data='order_phone'),
            InlineKeyboardButton(text="🏘 Manzilini qoldiring!", callback_data='order_location')
        ],
    ]
)

# pishloqli tovuq numbers classik
numbers_classik11 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="1⃣", callback_data='one'),
            InlineKeyboardButton(text="2⃣", callback_data='two'),
            InlineKeyboardButton(text="3⃣", callback_data='three')
        ],
        [
            InlineKeyboardButton(text="4⃣", callback_data='four'),
            InlineKeyboardButton(text="5⃣", callback_data='five'),
            InlineKeyboardButton(text="6⃣", callback_data='six')
        ],
        [
            InlineKeyboardButton(text="7⃣", callback_data='seven'),
            InlineKeyboardButton(text="8⃣", callback_data='eight'),
            InlineKeyboardButton(text="9⃣", callback_data='nine')
        ],
        [
            InlineKeyboardButton(text="⬅️ Ortga", callback_data='back666')
        ]
      
    ]
)

# flitter mini_classik
mini_classik12 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Mini  👍", callback_data='mini12'),
            InlineKeyboardButton(text="Classik  👍", callback_data='classik13')
        ],
        [
            InlineKeyboardButton(text="⬅️ Ortga", callback_data='back7')
        ]
    ]
)

# flitter numbers mini
numbers_mini12 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="1⃣", callback_data='one'),
            InlineKeyboardButton(text="2⃣", callback_data='two'),
            InlineKeyboardButton(text="3⃣", callback_data='three')
        ],
        [
            InlineKeyboardButton(text="4⃣", callback_data='four'),
            InlineKeyboardButton(text="5⃣", callback_data='five'),
            InlineKeyboardButton(text="6⃣", callback_data='six')
        ],
        [
            InlineKeyboardButton(text="7⃣", callback_data='seven'),
            InlineKeyboardButton(text="8⃣", callback_data='eight'),
            InlineKeyboardButton(text="9⃣", callback_data='nine')
        ],
        [
            InlineKeyboardButton(text="⬅️ Ortga", callback_data='back77')
        ]
      
    ]
)

# order
order = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="☎️ Raqam qoldiring!", callback_data='order_phone'),
            InlineKeyboardButton(text="🏘 Manzilini qoldiring!", callback_data='order_location')
        ],
    ]
)

# flitter numbers classik
numbers_classik13 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="1⃣", callback_data='one'),
            InlineKeyboardButton(text="2⃣", callback_data='two'),
            InlineKeyboardButton(text="3⃣", callback_data='three')
        ],
        [
            InlineKeyboardButton(text="4⃣", callback_data='four'),
            InlineKeyboardButton(text="5⃣", callback_data='five'),
            InlineKeyboardButton(text="6⃣", callback_data='six')
        ],
        [
            InlineKeyboardButton(text="7⃣", callback_data='seven'),
            InlineKeyboardButton(text="8⃣", callback_data='eight'),
            InlineKeyboardButton(text="9⃣", callback_data='nine')
        ],
        [
            InlineKeyboardButton(text="⬅️ Ortga", callback_data='back777')
        ]
      
    ]
)

# hot-dog menu
hot_dog_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Hot Dog Baget dabl  👍👍", callback_data='hot_dog_baget_dabl'),
            InlineKeyboardButton(text="Classik Hot Dog  👍👍", callback_data='classik_hot_dog')
        ],
        [
            InlineKeyboardButton(text="Korolevskiy  👍👍", callback_data='korolevskiy'),
            InlineKeyboardButton(text="Tovuqli Hot Dog  👍👍", callback_data='tovuqli_hot_dog')
        ],
        [
            InlineKeyboardButton(text="⬅️ Ortga", callback_data='back8')
        ]
      
    ]
)

# hot_dog_baget_dabl numbers 
numbers_hot_dog_baget_dabl14 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="1⃣", callback_data='one'),
            InlineKeyboardButton(text="2⃣", callback_data='two'),
            InlineKeyboardButton(text="3⃣", callback_data='three')
        ],
        [
            InlineKeyboardButton(text="4⃣", callback_data='four'),
            InlineKeyboardButton(text="5⃣", callback_data='five'),
            InlineKeyboardButton(text="6⃣", callback_data='six')
        ],
        [
            InlineKeyboardButton(text="7⃣", callback_data='seven'),
            InlineKeyboardButton(text="8⃣", callback_data='eight'),
            InlineKeyboardButton(text="9⃣", callback_data='nine')
        ],
        [
            InlineKeyboardButton(text="⬅️ Ortga", callback_data='back88')
        ]
      
    ]
)

# classik_hot_dog numbers 
numbers_classik_hot_dog15 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="1⃣", callback_data='one'),
            InlineKeyboardButton(text="2⃣", callback_data='two'),
            InlineKeyboardButton(text="3⃣", callback_data='three')
        ],
        [
            InlineKeyboardButton(text="4⃣", callback_data='four'),
            InlineKeyboardButton(text="5⃣", callback_data='five'),
            InlineKeyboardButton(text="6⃣", callback_data='six')
        ],
        [
            InlineKeyboardButton(text="7⃣", callback_data='seven'),
            InlineKeyboardButton(text="8⃣", callback_data='eight'),
            InlineKeyboardButton(text="9⃣", callback_data='nine')
        ],
        [
            InlineKeyboardButton(text="⬅️ Ortga", callback_data='back888')
        ]
      
    ]
)

# korolevskiy
korolevskiy = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="1⃣", callback_data='one'),
            InlineKeyboardButton(text="2⃣", callback_data='two'),
            InlineKeyboardButton(text="3⃣", callback_data='three')
        ],
        [
            InlineKeyboardButton(text="4⃣", callback_data='four'),
            InlineKeyboardButton(text="5⃣", callback_data='five'),
            InlineKeyboardButton(text="6⃣", callback_data='six')
        ],
        [
            InlineKeyboardButton(text="7⃣", callback_data='seven'),
            InlineKeyboardButton(text="8⃣", callback_data='eight'),
            InlineKeyboardButton(text="9⃣", callback_data='nine')
        ],
        [
            InlineKeyboardButton(text="⬅️ Ortga", callback_data='back8888')
        ]
      
    ]
)

# tovuqli_hot_dog
tovuqli_hot_dog = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="1⃣", callback_data='one'),
            InlineKeyboardButton(text="2⃣", callback_data='two'),
            InlineKeyboardButton(text="3⃣", callback_data='three')
        ],
        [
            InlineKeyboardButton(text="4⃣", callback_data='four'),
            InlineKeyboardButton(text="5⃣", callback_data='five'),
            InlineKeyboardButton(text="6⃣", callback_data='six')
        ],
        [
            InlineKeyboardButton(text="7⃣", callback_data='seven'),
            InlineKeyboardButton(text="8⃣", callback_data='eight'),
            InlineKeyboardButton(text="9⃣", callback_data='nine')
        ],
        [
            InlineKeyboardButton(text="⬅️ Ortga", callback_data='back88888')
        ]
      
    ]
)

# clab_sendvich menu
clab_sendvich_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Classik Clab Sendvich  👍👍", callback_data='classik_clab_sandvich'),
            InlineKeyboardButton(text="Tovuqli Sandvich  👍👍", callback_data='tovuqli_sandvich')
        ],
        [
            InlineKeyboardButton(text="⬅️ Ortga", callback_data='back9')
        ]
      
    ]
)

# classik_clab_sandvich numbers 
numbers_classik_clab_sandvich16 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="1⃣", callback_data='one'),
            InlineKeyboardButton(text="2⃣", callback_data='two'),
            InlineKeyboardButton(text="3⃣", callback_data='three')
        ],
        [
            InlineKeyboardButton(text="4⃣", callback_data='four'),
            InlineKeyboardButton(text="5⃣", callback_data='five'),
            InlineKeyboardButton(text="6⃣", callback_data='six')
        ],
        [
            InlineKeyboardButton(text="7⃣", callback_data='seven'),
            InlineKeyboardButton(text="8⃣", callback_data='eight'),
            InlineKeyboardButton(text="9⃣", callback_data='nine')
        ],
        [
            InlineKeyboardButton(text="⬅️ Ortga", callback_data='back99')
        ]
      
    ]
)

# tovuqli_sandvich numbers 
numbers_tovuqli_sandvich17 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="1⃣", callback_data='one'),
            InlineKeyboardButton(text="2⃣", callback_data='two'),
            InlineKeyboardButton(text="3⃣", callback_data='three')
        ],
        [
            InlineKeyboardButton(text="4⃣", callback_data='four'),
            InlineKeyboardButton(text="5⃣", callback_data='five'),
            InlineKeyboardButton(text="6⃣", callback_data='six')
        ],
        [
            InlineKeyboardButton(text="7⃣", callback_data='seven'),
            InlineKeyboardButton(text="8⃣", callback_data='eight'),
            InlineKeyboardButton(text="9⃣", callback_data='nine')
        ],
        [
            InlineKeyboardButton(text="⬅️ Ortga", callback_data='back99')
        ]
      
    ]
)

# shourma menu
shourma_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Mol go'shtli shourma  👍👍", callback_data='mol_gosht_shourma'),
            InlineKeyboardButton(text="Tovuq go'shtli shourma 👍👍", callback_data='tovuq_gosht_shourma')
        ],
        [
            InlineKeyboardButton(text="Mol go'shtli (qalampir) shourma  👍👍", callback_data='mol_gosht_qalampir_shourma'),
            InlineKeyboardButton(text="Tovuq go'shtli (qalampir) shourma 👍👍", callback_data='tovuq_gosht_qalampir_shourma')
        ],
        [
            InlineKeyboardButton(text="⬅️ Ortga", callback_data='back0')
        ]
      
    ]
)

mol_gosht_shourma_mini_classik = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Mini  👍", callback_data='minis'),
            InlineKeyboardButton(text="Classik  👍", callback_data='classiks')
        ],
        [
            InlineKeyboardButton(text="⬅️ Ortga", callback_data='back00')
        ]
    ]
)

tovuq_gosht_shourma_mini_classik = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Mini  👍", callback_data='miniss'),
            InlineKeyboardButton(text="Classik  👍", callback_data='classikss')
        ],
        [
            InlineKeyboardButton(text="⬅️ Ortga", callback_data='back000')
        ]
    ]
)

mol_gosht_qalampir_shourma_shourma_mini_classik = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Mini  👍", callback_data='minisss'),
            InlineKeyboardButton(text="Classik  👍", callback_data='classiksss')
        ],
        [
            InlineKeyboardButton(text="⬅️ Ortga", callback_data='back0000')
        ]
    ]
)

tovuq_gosht_qalampir_shourma_mini_classik = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Mini  👍", callback_data='minissss'),
            InlineKeyboardButton(text="Classik  👍", callback_data='classikssss')
        ],
        [
            InlineKeyboardButton(text="⬅️ Ortga", callback_data='back00000')
        ]
    ]
)

numbers_shourma1 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="1⃣", callback_data='one'),
            InlineKeyboardButton(text="2⃣", callback_data='two'),
            InlineKeyboardButton(text="3⃣", callback_data='three')
        ],
        [
            InlineKeyboardButton(text="4⃣", callback_data='four'),
            InlineKeyboardButton(text="5⃣", callback_data='five'),
            InlineKeyboardButton(text="6⃣", callback_data='six')
        ],
        [
            InlineKeyboardButton(text="7⃣", callback_data='seven'),
            InlineKeyboardButton(text="8⃣", callback_data='eight'),
            InlineKeyboardButton(text="9⃣", callback_data='nine')
        ],
        [
            InlineKeyboardButton(text="⬅️ Ortga", callback_data='back01')
        ]
      
    ]
)

numbers_shourma2 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="1⃣", callback_data='one'),
            InlineKeyboardButton(text="2⃣", callback_data='two'),
            InlineKeyboardButton(text="3⃣", callback_data='three')
        ],
        [
            InlineKeyboardButton(text="4⃣", callback_data='four'),
            InlineKeyboardButton(text="5⃣", callback_data='five'),
            InlineKeyboardButton(text="6⃣", callback_data='six')
        ],
        [
            InlineKeyboardButton(text="7⃣", callback_data='seven'),
            InlineKeyboardButton(text="8⃣", callback_data='eight'),
            InlineKeyboardButton(text="9⃣", callback_data='nine')
        ],
        [
            InlineKeyboardButton(text="⬅️ Ortga", callback_data='back02')
        ]
      
    ]
)

numbers_shourma3 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="1⃣", callback_data='one'),
            InlineKeyboardButton(text="2⃣", callback_data='two'),
            InlineKeyboardButton(text="3⃣", callback_data='three')
        ],
        [
            InlineKeyboardButton(text="4⃣", callback_data='four'),
            InlineKeyboardButton(text="5⃣", callback_data='five'),
            InlineKeyboardButton(text="6⃣", callback_data='six')
        ],
        [
            InlineKeyboardButton(text="7⃣", callback_data='seven'),
            InlineKeyboardButton(text="8⃣", callback_data='eight'),
            InlineKeyboardButton(text="9⃣", callback_data='nine')
        ],
        [
            InlineKeyboardButton(text="⬅️ Ortga", callback_data='back03')
        ]
      
    ]
)

numbers_shourma4 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="1⃣", callback_data='one'),
            InlineKeyboardButton(text="2⃣", callback_data='two'),
            InlineKeyboardButton(text="3⃣", callback_data='three')
        ],
        [
            InlineKeyboardButton(text="4⃣", callback_data='four'),
            InlineKeyboardButton(text="5⃣", callback_data='five'),
            InlineKeyboardButton(text="6⃣", callback_data='six')
        ],
        [
            InlineKeyboardButton(text="7⃣", callback_data='seven'),
            InlineKeyboardButton(text="8⃣", callback_data='eight'),
            InlineKeyboardButton(text="9⃣", callback_data='nine')
        ],
        [
            InlineKeyboardButton(text="⬅️ Ortga", callback_data='back04')
        ]
      
    ]
)

# burger menu
burger_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Gamburger  👍👍", callback_data='gamburger'),
            InlineKeyboardButton(text="Chizburger 👍👍", callback_data='chizburger')
        ],
        [
            InlineKeyboardButton(text="⬅️ Ortga", callback_data='back10')
        ]
      
    ]
)

# gamburger numbers 
numbers_gamburger20 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="1⃣", callback_data='one'),
            InlineKeyboardButton(text="2⃣", callback_data='two'),
            InlineKeyboardButton(text="3⃣", callback_data='three')
        ],
        [
            InlineKeyboardButton(text="4⃣", callback_data='four'),
            InlineKeyboardButton(text="5⃣", callback_data='five'),
            InlineKeyboardButton(text="6⃣", callback_data='six')
        ],
        [
            InlineKeyboardButton(text="7⃣", callback_data='seven'),
            InlineKeyboardButton(text="8⃣", callback_data='eight'),
            InlineKeyboardButton(text="9⃣", callback_data='nine')
        ],
        [
            InlineKeyboardButton(text="⬅️ Ortga", callback_data='back1010')
        ]
      
    ]
)

# chizburger numbers 
numbers_chizburger21 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="1⃣", callback_data='one'),
            InlineKeyboardButton(text="2⃣", callback_data='two'),
            InlineKeyboardButton(text="3⃣", callback_data='three')
        ],
        [
            InlineKeyboardButton(text="4⃣", callback_data='four'),
            InlineKeyboardButton(text="5⃣", callback_data='five'),
            InlineKeyboardButton(text="6⃣", callback_data='six')
        ],
        [
            InlineKeyboardButton(text="7⃣", callback_data='seven'),
            InlineKeyboardButton(text="8⃣", callback_data='eight'),
            InlineKeyboardButton(text="9⃣", callback_data='nine')
        ],
        [
            InlineKeyboardButton(text="⬅️ Ortga", callback_data='back101010')
        ]
      
    ]
)

# donar menu
donar_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Go'shli donar  👍👍", callback_data='goshtli_donar'),
            InlineKeyboardButton(text="Tovuqli donar 👍👍", callback_data='tovuqli_donar')
        ],
        [
            InlineKeyboardButton(text="⬅️ Ortga", callback_data='back12')
        ]
      
    ]
)

# goshtli_donar numbers 
numbers_goshtli_donar22 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="1⃣", callback_data='one'),
            InlineKeyboardButton(text="2⃣", callback_data='two'),
            InlineKeyboardButton(text="3⃣", callback_data='three')
        ],
        [
            InlineKeyboardButton(text="4⃣", callback_data='four'),
            InlineKeyboardButton(text="5⃣", callback_data='five'),
            InlineKeyboardButton(text="6⃣", callback_data='six')
        ],
        [
            InlineKeyboardButton(text="7⃣", callback_data='seven'),
            InlineKeyboardButton(text="8⃣", callback_data='eight'),
            InlineKeyboardButton(text="9⃣", callback_data='nine')
        ],
        [
            InlineKeyboardButton(text="⬅️ Ortga", callback_data='back1212')
        ]
      
    ]
)

# tovuqli_donar numbers 
numbers_tovuqli_donar23 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="1⃣", callback_data='one'),
            InlineKeyboardButton(text="2⃣", callback_data='two'),
            InlineKeyboardButton(text="3⃣", callback_data='three')
        ],
        [
            InlineKeyboardButton(text="4⃣", callback_data='four'),
            InlineKeyboardButton(text="5⃣", callback_data='five'),
            InlineKeyboardButton(text="6⃣", callback_data='six')
        ],
        [
            InlineKeyboardButton(text="7⃣", callback_data='seven'),
            InlineKeyboardButton(text="8⃣", callback_data='eight'),
            InlineKeyboardButton(text="9⃣", callback_data='nine')
        ],
        [
            InlineKeyboardButton(text="⬅️ Ortga", callback_data='back121212')
        ]
      
    ]
)

# gazaklar menu
gazaklar_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Fries 15 gr  👍👍", callback_data='fry_15'),
            InlineKeyboardButton(text="Kartoshka Derevyanski  👍👍", callback_data='kartoshka_derevyanski'),
        ],
        [
            InlineKeyboardButton(text="Gurunch katta  👍👍", callback_data='gurunch_katta'),
            InlineKeyboardButton(text="Gurunch kichik  👍👍", callback_data='gurunch_kichik'),
        ],
        [
            InlineKeyboardButton(text="⬅️ Ortga", callback_data='back13')
        ]
      
    ]
)

# fry_15 numbers 
numbers_fry_15 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="1⃣", callback_data='one'),
            InlineKeyboardButton(text="2⃣", callback_data='two'),
            InlineKeyboardButton(text="3⃣", callback_data='three')
        ],
        [
            InlineKeyboardButton(text="4⃣", callback_data='four'),
            InlineKeyboardButton(text="5⃣", callback_data='five'),
            InlineKeyboardButton(text="6⃣", callback_data='six')
        ],
        [
            InlineKeyboardButton(text="7⃣", callback_data='seven'),
            InlineKeyboardButton(text="8⃣", callback_data='eight'),
            InlineKeyboardButton(text="9⃣", callback_data='nine')
        ],
        [
            InlineKeyboardButton(text="⬅️ Ortga", callback_data='back1313')
        ]
      
    ]
)

# kartoshka_derevyanski numbers 
numbers_kartoshka_derevyanski = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="1⃣", callback_data='one'),
            InlineKeyboardButton(text="2⃣", callback_data='two'),
            InlineKeyboardButton(text="3⃣", callback_data='three')
        ],
        [
            InlineKeyboardButton(text="4⃣", callback_data='four'),
            InlineKeyboardButton(text="5⃣", callback_data='five'),
            InlineKeyboardButton(text="6⃣", callback_data='six')
        ],
        [
            InlineKeyboardButton(text="7⃣", callback_data='seven'),
            InlineKeyboardButton(text="8⃣", callback_data='eight'),
            InlineKeyboardButton(text="9⃣", callback_data='nine')
        ],
        [
            InlineKeyboardButton(text="⬅️ Ortga", callback_data='back131313')
        ]
      
    ]
)

# gurunch_katta numbers 
numbers_gurunch_katta = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="1⃣", callback_data='one'),
            InlineKeyboardButton(text="2⃣", callback_data='two'),
            InlineKeyboardButton(text="3⃣", callback_data='three')
        ],
        [
            InlineKeyboardButton(text="4⃣", callback_data='four'),
            InlineKeyboardButton(text="5⃣", callback_data='five'),
            InlineKeyboardButton(text="6⃣", callback_data='six')
        ],
        [
            InlineKeyboardButton(text="7⃣", callback_data='seven'),
            InlineKeyboardButton(text="8⃣", callback_data='eight'),
            InlineKeyboardButton(text="9⃣", callback_data='nine')
        ],
        [
            InlineKeyboardButton(text="⬅️ Ortga", callback_data='back13131313')
        ]
      
    ]
)

# gurunch_kichik numbers 
numbers_gurunch_kichik = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="1⃣", callback_data='one'),
            InlineKeyboardButton(text="2⃣", callback_data='two'),
            InlineKeyboardButton(text="3⃣", callback_data='three')
        ],
        [
            InlineKeyboardButton(text="4⃣", callback_data='four'),
            InlineKeyboardButton(text="5⃣", callback_data='five'),
            InlineKeyboardButton(text="6⃣", callback_data='six')
        ],
        [
            InlineKeyboardButton(text="7⃣", callback_data='seven'),
            InlineKeyboardButton(text="8⃣", callback_data='eight'),
            InlineKeyboardButton(text="9⃣", callback_data='nine')
        ],
        [
            InlineKeyboardButton(text="⬅️ Ortga", callback_data='back1313131313')
        ]
      
    ]
)

# ichimliklar menu
ichimliklar_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Choy va kofe  👍👍", callback_data='choy_kofe'),
            InlineKeyboardButton(text="Yaxna ichimliklar  👍👍", callback_data='yaxna_ichimliklar')
        ],
        [
            InlineKeyboardButton(text="Fresh va tabiiy soklar  👍👍", callback_data='fresh_tabiy')
        ],
        [
            InlineKeyboardButton(text="⬅️ Ortga", callback_data='back14')
        ]
      
    ]
)

# Choy va kofe
choylar_kofelar = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Choylar  👍👍", callback_data='choylar'),
            InlineKeyboardButton(text="Kofelar  👍👍", callback_data='kofelar')
        ],
        [
            InlineKeyboardButton(text="⬅️ Ortga", callback_data='back144')
        ]
      
    ]
)

# choy_turlari
choy_turlari = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Ko'k choy  👍👍", callback_data='kok_choy'),
            InlineKeyboardButton(text="Qora choy  👍👍", callback_data='qora_choy')
        ],
        [
            InlineKeyboardButton(text="Limon choy  👍👍", callback_data='limon_choy'),
        ],
        [
            InlineKeyboardButton(text="⬅️ Ortga", callback_data='back1444')
        ]
      
    ]
)

# kok_choy_numbers
kok_choy_numbers = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="1⃣", callback_data='one'),
            InlineKeyboardButton(text="2⃣", callback_data='two'),
            InlineKeyboardButton(text="3⃣", callback_data='three')
        ],
        [
            InlineKeyboardButton(text="4⃣", callback_data='four'),
            InlineKeyboardButton(text="5⃣", callback_data='five'),
            InlineKeyboardButton(text="6⃣", callback_data='six')
        ],
        [
            InlineKeyboardButton(text="7⃣", callback_data='seven'),
            InlineKeyboardButton(text="8⃣", callback_data='eight'),
            InlineKeyboardButton(text="9⃣", callback_data='nine')
        ],
        [
            InlineKeyboardButton(text="⬅️ Ortga", callback_data='back14444')
        ]
      
    ]
)

# qora_choy_numbers
qora_choy_numbers = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="1⃣", callback_data='one'),
            InlineKeyboardButton(text="2⃣", callback_data='two'),
            InlineKeyboardButton(text="3⃣", callback_data='three')
        ],
        [
            InlineKeyboardButton(text="4⃣", callback_data='four'),
            InlineKeyboardButton(text="5⃣", callback_data='five'),
            InlineKeyboardButton(text="6⃣", callback_data='six')
        ],
        [
            InlineKeyboardButton(text="7⃣", callback_data='seven'),
            InlineKeyboardButton(text="8⃣", callback_data='eight'),
            InlineKeyboardButton(text="9⃣", callback_data='nine')
        ],
        [
            InlineKeyboardButton(text="⬅️ Ortga", callback_data='back144444')
        ]
      
    ]
)

# limon_choy_numbers
limon_choy_numbers = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="1⃣", callback_data='one'),
            InlineKeyboardButton(text="2⃣", callback_data='two'),
            InlineKeyboardButton(text="3⃣", callback_data='three')
        ],
        [
            InlineKeyboardButton(text="4⃣", callback_data='four'),
            InlineKeyboardButton(text="5⃣", callback_data='five'),
            InlineKeyboardButton(text="6⃣", callback_data='six')
        ],
        [
            InlineKeyboardButton(text="7⃣", callback_data='seven'),
            InlineKeyboardButton(text="8⃣", callback_data='eight'),
            InlineKeyboardButton(text="9⃣", callback_data='nine')
        ],
        [
            InlineKeyboardButton(text="⬅️ Ortga", callback_data='back1444444')
        ]
      
    ]
)

# kofe_turlari
kofe_turlari = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Americano  👍👍", callback_data='americano'),
            InlineKeyboardButton(text="Cappuccino  👍👍", callback_data='cappuccino')
        ],
        [
            InlineKeyboardButton(text="Cofe 3v1  👍👍", callback_data='cofe_3v1'),
            InlineKeyboardButton(text="Latte  👍👍", callback_data='latte')
        ],
        [
            InlineKeyboardButton(text="⬅️ Ortga", callback_data='back155')
        ]
      
    ]
)

# americano_numbers
americano_numbers = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="1⃣", callback_data='one'),
            InlineKeyboardButton(text="2⃣", callback_data='two'),
            InlineKeyboardButton(text="3⃣", callback_data='three')
        ],
        [
            InlineKeyboardButton(text="4⃣", callback_data='four'),
            InlineKeyboardButton(text="5⃣", callback_data='five'),
            InlineKeyboardButton(text="6⃣", callback_data='six')
        ],
        [
            InlineKeyboardButton(text="7⃣", callback_data='seven'),
            InlineKeyboardButton(text="8⃣", callback_data='eight'),
            InlineKeyboardButton(text="9⃣", callback_data='nine')
        ],
        [
            InlineKeyboardButton(text="⬅️ Ortga", callback_data='back1555')
        ]
      
    ]
)

# yaxna_ichimliklar
yaxna = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Fanta  👍👍", callback_data='fanta'),
            InlineKeyboardButton(text="Sprite  👍👍", callback_data='sprite')
        ],
        [
            InlineKeyboardButton(text="Coca Cola  👍👍", callback_data='cola'),
            InlineKeyboardButton(text="Nestle  👍👍", callback_data='nestle')
        ],
        [
            InlineKeyboardButton(text="⬅️ Ortga", callback_data='back16')
        ]
      
    ]
)

# fanta_numbers
fanta_numbers = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="1⃣", callback_data='one'),
            InlineKeyboardButton(text="2⃣", callback_data='two'),
            InlineKeyboardButton(text="3⃣", callback_data='three')
        ],
        [
            InlineKeyboardButton(text="4⃣", callback_data='four'),
            InlineKeyboardButton(text="5⃣", callback_data='five'),
            InlineKeyboardButton(text="6⃣", callback_data='six')
        ],
        [
            InlineKeyboardButton(text="7⃣", callback_data='seven'),
            InlineKeyboardButton(text="8⃣", callback_data='eight'),
            InlineKeyboardButton(text="9⃣", callback_data='nine')
        ],
        [
            InlineKeyboardButton(text="⬅️ Ortga", callback_data='back166')
        ]
      
    ]
)

# fresh_tabiy
fresh_tabiylar = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Bliss 1 l  👍👍", callback_data='bliss'),
            InlineKeyboardButton(text="Olma va sabzi fresh  👍👍", callback_data='olma_sabzi')
        ],
        [
            InlineKeyboardButton(text="⬅️ Ortga", callback_data='back177')
        ]
      
    ]
)

# bliss_numbers
bliss_numbers = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="1⃣", callback_data='one'),
            InlineKeyboardButton(text="2⃣", callback_data='two'),
            InlineKeyboardButton(text="3⃣", callback_data='three')
        ],
        [
            InlineKeyboardButton(text="4⃣", callback_data='four'),
            InlineKeyboardButton(text="5⃣", callback_data='five'),
            InlineKeyboardButton(text="6⃣", callback_data='six')
        ],
        [
            InlineKeyboardButton(text="7⃣", callback_data='seven'),
            InlineKeyboardButton(text="8⃣", callback_data='eight'),
            InlineKeyboardButton(text="9⃣", callback_data='nine')
        ],
        [
            InlineKeyboardButton(text="⬅️ Ortga", callback_data='back1777')
        ]
      
    ]
)

# desertlar menu
desertlar_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Assalim  👍👍", callback_data='assalim'),
            InlineKeyboardButton(text="Qulupnay  👍👍", callback_data='qulupnay'),
        ],
        [
            InlineKeyboardButton(text="Choko  👍👍", callback_data='choko')
        ],
        [
            InlineKeyboardButton(text="⬅️ Ortga", callback_data='back188')
        ]
      
    ]
)

# assalim_numbers
assalim_numbers = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="1⃣", callback_data='one'),
            InlineKeyboardButton(text="2⃣", callback_data='two'),
            InlineKeyboardButton(text="3⃣", callback_data='three')
        ],
        [
            InlineKeyboardButton(text="4⃣", callback_data='four'),
            InlineKeyboardButton(text="5⃣", callback_data='five'),
            InlineKeyboardButton(text="6⃣", callback_data='six')
        ],
        [
            InlineKeyboardButton(text="7⃣", callback_data='seven'),
            InlineKeyboardButton(text="8⃣", callback_data='eight'),
            InlineKeyboardButton(text="9⃣", callback_data='nine')
        ],
        [
            InlineKeyboardButton(text="⬅️ Ortga", callback_data='back1888')
        ]
      
    ]
)

# pizza menu
pizza_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Ananaslik  👍👍", callback_data='ananaslik'),
            InlineKeyboardButton(text="Peperoni  👍👍", callback_data='peperoni'),
        ],
        [
            InlineKeyboardButton(text="Margaritta  👍👍", callback_data='margaritta')
        ],
        [
            InlineKeyboardButton(text="⬅️ Ortga", callback_data='back19')
        ]
      
    ]
)

# ananaslik_numbers
ananaslik_numbers = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="1⃣", callback_data='one'),
            InlineKeyboardButton(text="2⃣", callback_data='two'),
            InlineKeyboardButton(text="3⃣", callback_data='three')
        ],
        [
            InlineKeyboardButton(text="4⃣", callback_data='four'),
            InlineKeyboardButton(text="5⃣", callback_data='five'),
            InlineKeyboardButton(text="6⃣", callback_data='six')
        ],
        [
            InlineKeyboardButton(text="7⃣", callback_data='seven'),
            InlineKeyboardButton(text="8⃣", callback_data='eight'),
            InlineKeyboardButton(text="9⃣", callback_data='nine')
        ],
        [
            InlineKeyboardButton(text="⬅️ Ortga", callback_data='back199')
        ]
      
    ]
)






