# -----------------------Імпорт бібліотеки----------------------------------------------
import telebot
from telebot import types
from telebot.types import InputMediaPhoto

# ------------------------ID Telegram bota-------------------------------------------------
bot = telebot.TeleBot('5265305201:AAE9hcDcyrEgBk76cfNz5UzF2kKuQPWCo-E')
bot_url = 'https://mtefk.herokuapp.com/'

# ------------------------------------------Команда стар, початок телеграм бота--------------------------------
# @bot.message_handler(commands=['start'])
# def start(message):
#     mess = f'Доброго дня, <b>{message.from_user.first_name} {message.from_user.last_name}</b>'
#     bot.send_message(message.chat.id, mess, parse_mode='html')


# -----------------------------------------------Кінець ------------------------------------------------------
# ------------------------------------Привітання--------------------------------------------------------
# @bot.message_handler()
# def get_user_text(message):
#     if message.text == "Привіт":
#         bot.send_message(message.chat.id,"І тобі привіт, радий тебе бачити тут, давай ",parse_mode= 'html')
#     else:
#         bot.send_message(message.chat.id,"Вибач, я тебе не розумію, вибери одну із кнопок",parse_mode= 'html')

# -------------------Кнопки  Inline----------------------
# @bot.message_handler(content_types=['text'])
# def Inline(message):
#     if message.chat.type == 'private':
#         if message.text == 'ЗНО':
#             markup = types.InlineKeyboardMarkup()
#             markup.add(types.InlineKeyboardButton("1", url="http://college.mlyniv.rv.ua/index.php?idi=df/rozklad/"))
#             markup.add(types.InlineKeyboardButton("2", url="http://college.mlyniv.rv.ua/index.php?idi=df/rozklad/"))
#             bot.send_message(message.chat.id, 'Оберіть наступний крок', reply_markup=markup)
@bot.message_handler(commands=['help'])
def start(message):
    bot.send_message(message.chat.id,
'''Цей телеграм бот є універсальним довідником 📝, він створений для  і студентів , вчителів і абітурієнтів коледжу.
Основним його завданням є донести швидко і корисну інформацію тому хто її потребує ⏱.
Для початку роботи застосуйте команду /start ✅, в подальшому користуйтесь кнопками на екрані .
Щоб дізнатися хто створив програму використайте команду /owner  👩‍💻.
Приємного користування ✌ )
''')
@bot.message_handler(commands=['owner'])
def start(message):
    bot.send_message(message.chat.id,
'''Засновником даного бота є студент 4 курсу комп’ютерної інженерії 🌐
Мінчук Ігор
inst: igor_minchyk ✅''')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    item1 = types.KeyboardButton('👨‍🎓👩‍🎓 Студенту')
    item2 = types.KeyboardButton('👦🏫 Вступнику')
    item3 = types.KeyboardButton('👨‍🏫👩‍🏫 Викладачу')
    item4 = types.KeyboardButton('🏢🗣️ Про коледж')
    item5 = types.KeyboardButton('📞 Контакти')
    item6 = types.KeyboardButton('📸 Фото-галерея')

    markup.add(item1, item2, item3, item4, item5, item6)
    bot.send_message(message.chat.id, 'Привіт, {0.first_name}! 😊, вас вітає телеграм бот коледжу МТЕФК.     Слава Україні 🇺🇦'.format(message.from_user), reply_markup=markup)

@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == '👨‍🎓👩‍🎓 Студенту': #------------Студенту кнопка
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            item1 = types.KeyboardButton('📆 Розклад')
            item2 = types.KeyboardButton('📈📉 Рейтинг')
            item3 = types.KeyboardButton('📕 ЗНО')
            back = types.KeyboardButton('⬅ Назад')
            markup.add(item1, item2, item3, back)
            bot.send_message(message.chat.id, 'Оберіть наступний крок ⏭',reply_markup= markup )

        elif message.text == '📆 Розклад':
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton("Розклад занять",url="http://college.mlyniv.rv.ua/index.php?idi=df/rozklad/"))
            bot.send_message(message.chat.id, 'Перейдіть за посиланням, щоб повністю ознайомитися з розкладом ', reply_markup=markup)
        elif message.text == '📈📉 Рейтинг':
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton("Стипендіальний рейтинг",url="http://college.mlyniv.rv.ua/df/stud/stip/Reiting.pdf"))
            bot.send_message(message.chat.id, 'Рейтинг II-семестру 2022р. 👇 ',reply_markup=markup)
        if message.text == '📕 ЗНО':
                    markup = types.InlineKeyboardMarkup()
                    markup.add(types.InlineKeyboardButton("Основні питання, щодо ЗНО-2022 ‼", url="http://college.mlyniv.rv.ua/txt/ZNO2022-1.pdf"))
                    markup.add(types.InlineKeyboardButton("Що таке національний мультипредметний тест ? 🤷🏻‍♀️",url="https://osvita.ua/test/advice/86414/"))
                    markup.add(types.InlineKeyboardButton("🖋Підготовка до ЗНО-2022 🖋️", url="http://lv.testportal.gov.ua:8080/"))
                    markup.add(types.InlineKeyboardButton("Інформаційна сторінка учасника ЗНО 👦🏻 ",url="http://college.mlyniv.rv.ua/txt/ZNO2022-1.pdf"))
                    markup.add(types.InlineKeyboardButton("Офіційний сайт МОН 📣", url="https://mon.gov.ua/ua"))
                    bot.send_message(message.chat.id, 'Оберіть наступний крок ⏭', reply_markup=markup)

        #-----------------Кнопка вступнику-------------------------------------------------

        elif message.text == '👦🏫 Вступнику':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            item1 = types.KeyboardButton('💼 Фаховий молодший бакалавр на основі БЗСО (9кл)')
            item2 = types.KeyboardButton('📑 Фаховий молодший бакалавр на основі ПЗСО (11кл)')
            item3 = types.KeyboardButton('📌 Фаховий молодший бакалавр на основі ОКР (кваліфікований робітник)')
            back = types.KeyboardButton('⬅ Назад')
            markup.add(item1, item2, item3, back)
            bot.send_message(message.chat.id, 'Оберіть наступний крок ⏭',reply_markup= markup )

        elif message.text == '💼 Фаховий молодший бакалавр на основі БЗСО (9кл)':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            item1 = types.KeyboardButton('💼 Які документи потрібно для вступу')
            item2 = types.KeyboardButton('📑 Яку спеціальність я можу обрати')
            item3 = types.KeyboardButton('✏ Алгоритм вступу')
            item4 = types.KeyboardButton('📌 QR код для шерингу документів')
            back = types.KeyboardButton('↩ Назад')
            markup.add(item1, item2, item3,item4, back)
            bot.send_message(message.chat.id, 'Оберіть наступний крок ⏭',reply_markup= markup )

        #-------------------------------------9клас-----------------------------------------
        elif message.text == '💼 Які документи потрібно для вступу':
            bot.send_message(message.chat.id, '''
▫ Заява 📄
▫ Мотиваційний лист
▫ Паспорт
▫ Картка платника податків
▫ Свідоцтво про базову освіту та додаток до нього
▫ 4 кольорові фотокартки розміром 3х4
''')
        elif message.text == '📑 Яку спеціальність я можу обрати':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            item1 = types.KeyboardButton('Облік і оподаткування 👩‍💼')
            item2 = types.KeyboardButton('Менеджмент 🧑‍💼')
            item3 = types.KeyboardButton('''Комп'ютерна інженерія 👨‍💻''')
            item4 = types.KeyboardButton('Технологія виробництва та переробки продукції тваринництва 🏭')
            item5 = types.KeyboardButton('Ветеринарна медицина 🩺')
            back = types.KeyboardButton('Назад  ↩')
            markup.add(item1, item2, item3, item4,item5, back)
            bot.send_message(message.chat.id, 'Оберіть наступний крок ⏭', reply_markup=markup)
        elif message.text == 'Облік і оподаткування 👩‍💼':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            item1 = types.KeyboardButton('Про ОПП(спеціальність) 📄')
            item2 = types.KeyboardButton('Відео-представлення 📄🎥')
            item3 = types.KeyboardButton('✏ Алгоритм вступу')
            back = types.KeyboardButton('↩  Назад')
            markup.add(item1, item2,item3, back)
            bot.send_message(message.chat.id, 'Оберіть наступний крок ⏭', reply_markup=markup)
        elif message.text == 'Про ОПП(спеціальність) 📄':
            bot.send_message(message.chat.id,'''
Освітньо – професійна програма:
 	Облік і оподаткування
 	
Спеціальність📕:			   
    071 Облік і оподаткування 👨‍💼
    
Галузь знань 📚:		
	07 Управління та адміністрування
	
Кваліфікація: 
    Фаховий молодший бакалавр з обліку і оподаткування
	
Термін навчання:		 
    2 роки 10 місяців ⏰
    
Бюджетна форма навчання:  
    Індивідуальна усна співбесіда, ⚖
    яка включає питання з української мови та 
    математики + мотиваційний  лист
    
Контрактна форма навчання:
	 Мотиваційний лист
     Вартість навчання одного року	 8000 грн 💸. 

Залишилися питання ☎?
Звертайтеся до секретаря приймальної комісії – Каленюк Оксани Ярославівни
+380502649020,
+380960050864.
''')
        if message.text == 'Відео-представлення 📄🎥':
                    markup = types.InlineKeyboardMarkup()
                    markup.add(types.InlineKeyboardButton("Відео-представлення 📄🎥", url ="https://www.youtube.com/watch?v=-MzKJmPObKE&t=14s"))
                    bot.send_message(message.chat.id, 'Перейдіть за посиланням, щоб переглянути відео ⏭', reply_markup=markup)

        elif message.text == 'Менеджмент 🧑‍💼':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            item1 = types.KeyboardButton('Про ОПП(спеціальність) 📄🎥🗂')
            item2 = types.KeyboardButton('Відео-представлення 🎥🗂📼')
            item3 = types.KeyboardButton('✏ Алгоритм вступу')
            item4 = types.KeyboardButton('↩  Назад')
            markup.add(item1, item2, item3, item4)
            bot.send_message(message.chat.id, 'Оберіть наступний крок ⏭', reply_markup=markup)
        elif message.text == 'Про ОПП(спеціальність) 📄🎥🗂':
            bot.send_message(message.chat.id, '''
Освітньо – професійна програма :		
    Менеджмент 🗃
    
Спеціальність 🛠:					   
    073 Менеджмент
    
Галузь знань 📌:				    
    07 Управління та адміністрування

Кваліфікація: 
    Фаховий молодший бакалавр з менеджемнту
    
Термін навчання:					   
    3 роки  5 місяців  ⏳
    
Бюджетна форма навчання:			    
    Індивідуальна усна співбесіда 👩‍💼 , 
    яка включає питання з української мови та 
    математики + мотиваційний  лист 🖊
    
Контрактна форма навчання			Мотиваційний лист
Вартість навчання одного року		8000 грн. 

Залишилися питання ?
Звертайтеся до секретаря приймальної комісії
 – Каленюк Оксани Ярославівни 📞
+380502649020,
+380960050864.

        ''')
        if message.text == 'Відео-представлення 🎥🗂📼':
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton("Відео-представлення 📄🎥🗂📼",url="https://www.youtube.com/watch?v=R-FIvp5i7j8"))
            bot.send_message(message.chat.id, 'Перейдіть за посиланням, щоб переглянути відео ⏭', reply_markup=markup)

        if message.text == '''Комп'ютерна інженерія 👨‍💻''':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            item1 = types.KeyboardButton('Про ОПП(спеціальність) 💻')
            item2 = types.KeyboardButton('Відео-представлення 📺')
            item3 = types.KeyboardButton('✏ Алгоритм вступу')
            back = types.KeyboardButton('↩  Назад')
            markup.add(item1, item2, item3, back)
            bot.send_message(message.chat.id, 'Оберіть наступний крок ⏭', reply_markup=markup)
        elif message.text == 'Про ОПП(спеціальність) 💻':
            bot.send_message(message.chat.id, '''
Освітньо – професійна програма 		
    Комп’ютерна інженерія ⌨
    
Спеціальність					    
    123 Комп’ютерна інженерія
    
Галузь знань					    
    12 Інформаційні технології 🖥
    
Кваліфікація: 
    Фаховий молодший бакалавр з обліку і комп'ютерної інженерії
    
Термін навчання					    
    3 роки 10 місяців ⏳
    
Бюджетна форма навчання			    
    Індивідуальна усна співбесіда 🖊, 
    яка включає питання з української мови 🖊 
    та математики + мотиваційний  лист
    
Контрактна форма навчання			Мотиваційний лист
Вартість навчання одного року		8000 грн 💸. 

Залишилися питання ⁉
Звертайтеся до секретаря приймальної комісії 📞 – Каленюк Оксани Ярославівни
+380502649020,
+380960050864.
                ''')
        if message.text == 'Відео-представлення 📺':
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton("Відео-представлення 📺",url="https://www.youtube.com/watch?v=o_4C8zOcrkk&t=10s"))
            bot.send_message(message.chat.id, 'Перейдіть за посиланням, щоб переглянути відео ⏭', reply_markup=markup)

        elif message.text == 'Технологія виробництва та переробки продукції тваринництва 🏭':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            item1 = types.KeyboardButton('Про ОПП(спеціальність) 🔬')
            item2 = types.KeyboardButton('Відео-представлення 📸')
            item3 = types.KeyboardButton('✏ Алгоритм вступу')
            back = types.KeyboardButton('↩  Назад')
            markup.add(item1, item2, item3, back)
            bot.send_message(message.chat.id, 'Оберіть наступний крок ⏭', reply_markup=markup)
        elif message.text == 'Про ОПП(спеціальність) 🔬':
            bot.send_message(message.chat.id, '''
Освітньо – професійна програма 		
    Технологія виробництва та переробки продукції тваринництва 🥩
    
Спеціальність					    
    204 Технологія виробництва та переробки продукції тваринництва
    
Галузь знань					    
    20 Аграрні науки та продовольство 👩‍🌾

Кваліфікація: 
    Фаховий молодший бакалавр з технології
    виробництва та переробки продукції тваринництва
    
Термін навчання					    
    3 роки 10 місяців 📣
    
Бюджетна форма навчання			    
    Індивідуальна усна співбесіда, яка включає питання з української мови 
    та біологія + мотиваційний  лист 🖊
    
Контрактна форма навчання			Мотиваційний лист
Вартість навчання одного року		8000 грн. 

Залишилися питання?
Звертайтеся до секретаря приймальної комісії – Каленюк Оксани Ярославівни
+380502649020,
+380960050864.''')
        if message.text == 'Відео-представлення 📸':
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton("Відео-представлення 📺",url="https://www.youtube.com/watch?v=Ib_JuAaudAU"))
            bot.send_message(message.chat.id, 'Перейдіть за посиланням, щоб переглянути відео ⏭', reply_markup=markup)

        elif message.text == 'Ветеринарна медицина 🩺':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            item1 = types.KeyboardButton('Про ОПП(спеціальність) 💉')
            item2 = types.KeyboardButton('Відео-представлення 🎞')
            item3 = types.KeyboardButton('✏ Алгоритм вступу')
            back = types.KeyboardButton('↩  Назад')
            markup.add(item1, item2, item3, back)
            bot.send_message(message.chat.id, 'Оберіть наступний крок ⏭', reply_markup=markup)
        elif message.text == 'Про ОПП(спеціальність) 💉':
            bot.send_message(message.chat.id, '''
Освітньо – професійна програма 		
    Ветеринарна медицина 🐣
    
Спеціальність					    
    211 Ветеринарна медицина 🐮
    
Галузь знань					    
    21 Ветеринарна медицина 🐔
    
Кваліфікація: 
    Фаховий молодший бакалавр з ветеринарної медецини
    
Термін навчання					    
    3 роки 10 місяців ⌛
    
Бюджетна форма навчання			    
    Індивідуальна усна співбесіда,
    яка включає питання з української мови та
    біологія + мотиваційний  лист ✏
     
Контрактна форма навчання			Мотиваційний лист
Вартість навчання одного року		8000 грн. 

Залишилися питання? 📢
Звертайтеся до секретаря приймальної комісії – Каленюк Оксани Ярославівни
+380502649020,
+380960050864.  ''')
        if message.text == 'Відео-представлення 🎞':
            markup = types.InlineKeyboardMarkup()
            markup.add(
                types.InlineKeyboardButton("Відео-представлення 📺", url="https://www.youtube.com/watch?v=Pb6e2h2z3PE"))
            bot.send_message(message.chat.id, 'Перейдіть за посиланням, щоб переглянути відео ⏭', reply_markup=markup)


        elif message.text == '✏ Алгоритм вступу':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            item1 = types.KeyboardButton('Основна сесія прийому 📎')
            item2 = types.KeyboardButton('Додаткова сесія прийому 📎')
            back = types.KeyboardButton('Назад  ↩')
            markup.add(item1, item2, back)
            bot.send_message(message.chat.id, 'Оберіть наступний крок ⏭', reply_markup=markup)

        elif message.text == 'Основна сесія прийому 📎':
            bot.send_message(message.chat.id, '''
✅ <b>Крок1. </b>  Реєстрація електронних кабінетів вступників та завантаження необхідних документів 📜	:
Розпочинається – 23 червня
Завершується – 31 жовтня
✅<b>Крок2. </b>  Початок прийому заяв та документів 📩 - 30 червня 
✅<b>Крок3. </b>  Закінчується прийому заяв та документів о 18:00 годині 
13 липня 
✅<b>Крок4. </b>  Строки проведення індивідуальних усних  співбесід з 14 по 21 липня
✅<b>Крок5. </b>  Рейтинговий список не пізніше 📢: 12:00 год 26 липня
✅<b>Крок6. </b>  Термін виконання вимог вступниками до 12:00 год 28 липня 
✅<b>Крок7. </b>  Термін зарахування 📚:
за регіональним замовленням – не пізніше 18:00 год 30 липня;
за кошти фізичних або юридичних осіб – не пізніше ніж 03 серпня ''',parse_mode= 'html')
        elif message.text == 'Додаткова сесія прийому 📎':
            bot.send_message(message.chat.id, '''
✅ <b>Крок1.</b> Реєстрація електронних кабінетів вступників 💾 та завантаження необхідних документів	:
Розпочинається – 23 червня
Завершується – 31 жовтня
✅ <b>Крок2.</b> Початок прийому заяв та документів 📢 - 8 серпня 
✅ <b>Крок3.</b> Закінчується прийому заяв та документів 📞 о 18:00 годині 21 серпня 
✅ <b>Крок4.</b> Строки проведення індивідуальних усних  співбесід з 22 по 25 серпня
✅ <b>Крок5.</b> Рейтинговий список не пізніше 📃: 12:00 год 26 липня
✅ <b>Крок6.</b> Термін виконання вимог вступниками до 12:00 год 30 серпня
✅ <b>Крок7.</b> Термін зарахування 🖊️:
за кошти фізичних або юридичних осіб – не пізніше ніж 31 серпня''', parse_mode='html')
        elif message.text == '📌 QR код для шерингу документів':
            qr = open('1.png.', 'rb')
            bot.send_photo(message.chat.id, qr,caption='Відскануйте за допомогою сканера, або камери  ☝')

#--------------------------------------11 клас-------------------
        elif message.text == '📑 Фаховий молодший бакалавр на основі ПЗСО (11кл)':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            item1 = types.KeyboardButton('Які документи потрібно для вступу ?🗒️️')
            item2 = types.KeyboardButton('Яку спеціальність я можу обрати 📄')
            item3 = types.KeyboardButton('Алгоритм вступу ⚙')
            item4 = types.KeyboardButton('📌 QR код для шерингу документів')
            back = types.KeyboardButton('↩ Назад')
            markup.add(item1, item2, item3, item4, back)
            bot.send_message(message.chat.id, 'Оберіть наступний крок ⏭', reply_markup=markup)

        if message.text == 'Які документи потрібно для вступу ?🗒️️':
            bot.send_message(message.chat.id, '''
▫ Заява
▫ Мотиваційний лист
▫ Два сертифікати ЗНО (за 2019, 2020, 2021 рік) 
▫ Картка учасника ЗНО
▫ Результат НМТ 2022 
▫ Картка учасника НМТ
▫ Паспорт
▫ Картка платника податків
▫ Свідоцтво про повню середню освіту та додаток до нього
▫ Військовий квиток чи посвідчення про приписку (для парубків)
▫ 4 кольорові фотокартки розміром 3х4''',parse_mode='html')

        elif message.text == 'Яку спеціальність я можу обрати 📄':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
            item1 = types.KeyboardButton('👩‍💼 Облік і оподаткування')
            item2 = types.KeyboardButton('🧑‍💼 Менеджмент')
            item3 = types.KeyboardButton("🧑‍💻 Комп'ютерна інженерія")
            item4 = types.KeyboardButton('🏭 Технологія виробництва та переробки продукції тваринництва')
            item5 = types.KeyboardButton('🩺 Ветеринарна медицина')
            back = types.KeyboardButton('⬅ Назад')
            markup.add(item1, item2, item3, item4, item5, back)
            bot.send_message(message.chat.id, 'Оберіть наступний крок ⏭', reply_markup=markup)

        elif message.text == '👩‍💼 Облік і оподаткування':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            item1 = types.KeyboardButton('📄 Про ОПП(спеціальність)')
            item2 = types.KeyboardButton('Відео-представлення 📄🎥')
            item3 = types.KeyboardButton('Алгоритм вступу ⚙')
            back = types.KeyboardButton('◀ Назад')
            markup.add(item1, item2, item3, back)
            bot.send_message(message.chat.id, 'Оберіть наступний крок ⏭', reply_markup=markup)
        elif message.text == '📄 Про ОПП(спеціальність)':
            bot.send_message(message.chat.id, '''
Освітньо – професійна програма:	📰	
    Облік і оподаткування
     
Спеціальність 👨‍💼:						    
    071 Облік і оподаткування
     
Галузь знань:						    
    07 Управління та адміністрування

Кваліфікація: 
    Фаховий молодший бакалавр з обліку і оподаткування
    
Термін навчання:				    1 роки 10 місяців

Бюджетна форма навчання:			ЗНО за 2019, 2020, 2021 / НМТ або індивідуальна усна співбесіда:
                                    Українська мова, математика або історія або географія
                                    Мотиваційний лист в усіх випадках
                                    
Контрактна форма навчання			Мотиваційний лист
Вартість навчання одного року		8000 грн. 

Залишилися питання ☎?
Звертайтеся до секретаря приймальної комісії – Каленюк Оксани Ярославівни
+380502649020,
+380960050864.
        ''')

        elif message.text == '🧑‍💼 Менеджмент':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            item1 = types.KeyboardButton('📄🗂 Про ОПП(спеціальність)')
            item2 = types.KeyboardButton('Відео-представлення 🎥🗂📼')
            item3 = types.KeyboardButton('Алгоритм вступу ⚙')
            back = types.KeyboardButton('◀ Назад')
            markup.add(item1, item2, item3, back)
            bot.send_message(message.chat.id, 'Оберіть наступний крок ⏭', reply_markup=markup)
        elif message.text == '📄🗂 Про ОПП(спеціальність)':
            bot.send_message(message.chat.id, '''
Освітньо – професійна програма 📋:
 		Менеджмент
 		
Спеціальність 🧰
		073 Менеджмент
		
Галузь знань					    
        07 Управління та адміністрування
        
Кваліфікація: 
    Фаховий молодший бакалавр з менеджменту
        
Термін навчання	🕰		
		2 роки 5 місяців
		
Бюджетна форма навчання:	
		ЗНО за 2019, 2020, 2021 / НМТ або індивідуальна усна співбесіда 👩‍💼:  
        Українська мова, математика або історія або географія
        Мотиваційний лист в усіх випадках 🖊
        
Контрактна форма навчання			Мотиваційний лист
Вартість навчання одного року		8000 грн. 

Залишилися питання ?
Звертайтеся до секретаря приймальної комісії 📞 – Каленюк Оксани Ярославівни
+380502649020,
+380960050864.''')

        if message.text == "🧑‍💻 Комп'ютерна інженерія":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            item1 = types.KeyboardButton('💻 Про ОПП(спеціальність) ')
            item2 = types.KeyboardButton('Відео-представлення 📺')
            item3 = types.KeyboardButton('Алгоритм вступу ⚙')
            back = types.KeyboardButton('◀ Назад')
            markup.add(item1, item2, item3, back)
            bot.send_message(message.chat.id, 'Оберіть наступний крок ⏭', reply_markup=markup)
        elif message.text == '💻 Про ОПП(спеціальність) ':
            bot.send_message(message.chat.id, '''
Освітньо – професійна програма
 	    Комп’ютерна інженерія ⌨
 	    
Спеціальність			
		123 Комп’ютерна інженерія
		
Галузь знань		
    	12 Інформаційні технології 🖥
    	
Кваліфікація: 
    Фаховий молодший бакалавр з комп’ютерної інженерії
    	
Термін навчання				
	    2 роки 10 місяців ⏳
	    
Бюджетна форма навчання:		
        ЗНО за 2019, 2020, 2021 / НМТ або індивідуальна усна співбесіда 🖊:
        Українська мова, математика або історія або географія
        Мотиваційний лист в усіх випадках 🖊
        
Контрактна форма навчання			Мотиваційний лист

Вартість навчання одного року		8000 грн. 💸

Залишилися питання ⁉📞   
Звертайтеся до секретаря приймальної комісії – Каленюк Оксани Ярославівни
+380502649020,
+380960050864.''')

        elif message.text == '🏭 Технологія виробництва та переробки продукції тваринництва':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            item1 = types.KeyboardButton('🔬 Про ОПП(спеціальність) ')
            item2 = types.KeyboardButton('Відео-представлення 📸')
            item3 = types.KeyboardButton('Алгоритм вступу ⚙')
            back = types.KeyboardButton('◀ Назад')
            markup.add(item1, item2, item3, back)
            bot.send_message(message.chat.id, 'Оберіть наступний крок ⏭', reply_markup=markup)
        elif message.text == '🔬 Про ОПП(спеціальність) ':
            bot.send_message(message.chat.id, '''
Освітньо – професійна програма 	
	    Технологія виробництва та переробки продукції тваринництва
	    
Спеціальність			
		204 Технологія виробництва та переробки продукції тваринництва
		
Галузь знань			
		20 Аграрні науки та продовольство 👩‍🌾
		
Кваліфікація: 
    Фаховий молодший бакалавр з технології виробництва 
    та переробки продукції твариництва
		
Термін навчання			
		2 роки 10 місяців 📣
		
Бюджетна форма навчання:	
		ЗНО за 2019, 2020, 2021 / НМТ або індивідуальна усна співбесіда:
        Українська мова, біологія або математика або історія 
        Мотиваційний лист в усіх випадках 🖊
        
Контрактна форма навчання			Мотиваційний лист

Вартість навчання одного року		8000 грн. 

Залишилися питання?
Звертайтеся до секретаря приймальної комісії 📞 – Каленюк Оксани Ярославівни
+380502649020,
+380960050864.''')


        elif message.text == '🩺 Ветеринарна медицина':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            item1 = types.KeyboardButton('💉 Про ОПП(спеціальність) ')
            item2 = types.KeyboardButton('Відео-представлення 🎞')
            item3 = types.KeyboardButton('Алгоритм вступу ⚙')
            back = types.KeyboardButton('◀ Назад')
            markup.add(item1, item2, item3, back)
            bot.send_message(message.chat.id, 'Оберіть наступний крок ⏭', reply_markup=markup)
        elif message.text == '💉 Про ОПП(спеціальність) ':
            bot.send_message(message.chat.id, '''
Освітньо – професійна програма 	
	    Ветеринарна медицина 🐣
	     
Спеціальність			
		211 Ветеринарна медицина 🐮
		
Галузь знань			
		21 Ветеринарна медицина 🐔
		
Кваліфікація: 
    Фаховий молодший бакалавр з ветеринарної медицини		
		
Термін навчання				
	    2 роки 10 місяців ⌛
	    
Бюджетна форма навчання:	
		ЗНО за 2019, 2020, 2021 / НМТ або індивідуальна усна співбесіда:
        Українська мова, біологія або математика або історія 
        Мотиваційний лист в усіх випадках ✏
        
Контрактна форма навчання		    Мотиваційний лист
Вартість навчання одного року		8000 грн. 

Залишилися питання? 📢
Звертайтеся до секретаря приймальної комісії 📞 – Каленюк Оксани Ярославівни
+380502649020,
+380960050864.''')


        elif message.text == 'Алгоритм вступу ⚙':
            bot.send_message(message.chat.id, '''
<b>Крок1.</b> Реєстрація електронних кабінетів вступників та завантаження необхідних документів	:
    Розпочинається – 1 липня
    Завершується – 31 жовтня
<b>Крок2.</b> Початок прийому заяв та документів - 14 липня 
<b>Крок3.</b> Закінчується прийому заяв та документів:
•	Для осіб, які вступають на основі індивідуальної усної співбесіди о 18:00 годині 5 серпня 
•	Для осіб, які вступають на основі сертифікатів ЗНО, або НМТ о 18:00 годині 31 серпня 
<b>Крок4.</b> Строки проведення індивідуальних усних  співбесід з 8 по 16 серпня
<b>Крок5.</b> Рейтинговий список не пізніше: не пізніше 12:00 год 1 вересня
<b>Крок6.</b> Термін виконання вимог вступниками до 12:00 год 6 вересня
<b>Крок7.</b> Термін зарахування:
    за регіональним замовленням – не пізніше 12:00 год 8 вересня 
    за кошти фізичних або юридичних осіб – не пізніше 12:00 год 16 вересня 
''',parse_mode='html')

#----------------------Фаховий молодший бакалавр---------------------------
        elif message.text == '📌 Фаховий молодший бакалавр на основі ОКР (кваліфікований робітник)':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            item1 = types.KeyboardButton('Які документи потрібно для вступу 📑')
            item2 = types.KeyboardButton('Яку спеціальність я можу обрати 🔎')
            item3 = types.KeyboardButton('Алгоритм вступу 📝')
            item4 = types.KeyboardButton('📌 QR код для шерингу документів ')
            back = types.KeyboardButton('↩ Назад')
            markup.add(item1, item2, item3, item4, back)
            bot.send_message(message.chat.id, 'Оберіть наступний крок ⏭', reply_markup=markup)

        elif message.text == 'Які документи потрібно для вступу 📑':
            bot.send_message(message.chat.id, '''
▫ Заява
▫ Мотиваційний лист
▫ Паспорт
▫ Картка платника податків
▫ Диплом кваліфікованого робітника та додаток до нього
▫ 4 кольорові фотокартки розміром 3х4
  ''')

        elif message.text == 'Яку спеціальність я можу обрати 🔎':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
            item1 = types.KeyboardButton('Облік і оподаткування 📋')
            item2 = types.KeyboardButton('Менеджмент 💼')
            item3 = types.KeyboardButton('Комп’ютерна інженерія 💻')
            item4 = types.KeyboardButton('Технологія виробництва та переробки продукції тваринництва 🐣')
            item5 = types.KeyboardButton('Ветеринарна медицина 🐮')
            back = types.KeyboardButton('⬅ Назад')
            markup.add(item1, item2, item3, item4, item5, back)
            bot.send_message(message.chat.id, 'Оберіть наступний крок ⏭', reply_markup=markup)

        elif message.text == 'Облік і оподаткування 📋':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            item1 = types.KeyboardButton('🏢 Про ОПП(спеціальність)')
            item2 = types.KeyboardButton('Відео-представлення 📄🎥')
            item3 = types.KeyboardButton('Алгоритм вступу 📝')
            back = types.KeyboardButton('Назад ◀')
            markup.add(item1, item2, item3, back)
            bot.send_message(message.chat.id, 'Оберіть наступний крок ⏭', reply_markup=markup)
        elif message.text == '🏢 Про ОПП(спеціальність) ':
            bot.send_message(message.chat.id, '''
Освітньо – професійна програма 	
	    Облік і оподаткування
	    
Спеціальність 📕		
		071 Облік і оподаткування 👨‍💼
		
Галузь знань 📚				
	    07 Управління та адміністрування
	    
Кваліфікація: 
    Фаховий молодший бакалавр з обліку і оподаткування
	    
Термін навчання				
	    1 рік 10 місяців ⏰
	    
Бюджетна форма навчання		
	    Індивідуальна усна співбесіда ⚖, яка включає питання
	     з фахових дисциплін + мотиваційний  лист
	     
Контрактна форма навчання			Мотиваційний лист
Вартість навчання одного року		8000 грн. 💸 

Залишилися питання?☎
Звертайтеся до секретаря приймальної комісії – Каленюк Оксани Ярославівни
+380502649020,
+380960050864.
                ''')

        elif message.text == 'Менеджмент 💼':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            item1 = types.KeyboardButton('📌 Про ОПП(спеціальність) ')
            item2 = types.KeyboardButton('Відео-представлення 🎥🗂📼')
            item3 = types.KeyboardButton('Алгоритм вступу 📝')
            back = types.KeyboardButton('Назад ◀')
            markup.add(item1, item2, item3, back)
            bot.send_message(message.chat.id, 'Оберіть наступний крок ⏭', reply_markup=markup)
        elif message.text == '📌Про ОПП(спеціальність) ':
            bot.send_message(message.chat.id, '''
Освітньо – професійна програма 📋  	
	    Менеджмент
	    
Спеціальність 🧰			
		073 Менеджмент
		
Галузь знань			
		07 Управління та адміністрування
		
Кваліфікація: 
    Фаховий молодший бакалавр з менеджменту
		
Термін навчання	🕰			
	    1 рік 5 місяців
	    
Бюджетна форма навчання		
	    Індивідуальна усна співбесіда, яка включає питання
	    з фахових дисциплін + мотиваційний  лист 🖊
	    
Контрактна форма навчання		    Мотиваційний лист
Вартість навчання одного року		8000 грн. 

Залишилися питання?
Звертайтеся до секретаря приймальної комісії 📞 – Каленюк Оксани Ярославівни
+380502649020,
+380960050864.
''')

        elif message.text == 'Комп’ютерна інженерія 💻':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            item1 = types.KeyboardButton('🖥⌨🖱 Про ОПП(спеціальність) ')
            item2 = types.KeyboardButton('Відео-представлення 📺')
            item3 = types.KeyboardButton('Алгоритм вступу 📝')
            back = types.KeyboardButton('Назад ◀')
            markup.add(item1, item2, item3, back)
            bot.send_message(message.chat.id, 'Оберіть наступний крок ⏭', reply_markup=markup)
        elif message.text == '🖥⌨🖱 Про ОПП(спеціальність) ':
            bot.send_message(message.chat.id, '''
Освітньо – професійна програма 	
	    Комп’ютерна інженерія ⌨
	    
Спеціальність			
		123 Комп’ютерна інженерія 🖥 
		
Галузь знань			
		12 Інформаційні технології ⏳
		
Кваліфікація: 
    Фаховий молодший бакалавр з ком'ютерної інженерії
		
Термін навчання				
	    1 рік 10 місяців
	    
Бюджетна форма навчання		
	    Індивідуальна усна співбесіда, яка включає питання
	     з фахових дисциплін +  мотиваційний  лист 🖊
	     
Контрактна форма навчання			Мотиваційний лист
Вартість навчання одного року		8000 грн.  💸

Залишилися питання ⁉📞
Звертайтеся до секретаря приймальної комісії – Каленюк Оксани Ярославівни
+380502649020,
+380960050864.
''')

        elif message.text == 'Технологія виробництва та переробки продукції тваринництва 🐣':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            item1 = types.KeyboardButton('👨‍🌾 Про ОПП(спеціальність) ')
            item2 = types.KeyboardButton('Відео-представлення 📸')
            item3 = types.KeyboardButton('Алгоритм вступу 📝')
            back = types.KeyboardButton('Назад ◀')
            markup.add(item1, item2, item3, back)
            bot.send_message(message.chat.id, 'Оберіть наступний крок ⏭', reply_markup=markup)
        elif message.text == '👨‍🌾 Про ОПП(спеціальність) ':
            bot.send_message(message.chat.id, '''
Освітньо – професійна програма 	
	    Технологія виробництва та переробки продукції тваринництва 🏭 
	    
Спеціальність			
		204 Технологія виробництва та переробки продукції тваринництва👩‍🌾
		
Галузь знань				
	    20 Аграрні науки та продовольство
	    
Кваліфікація: 
    Фаховий молодший бакалавр з технології виробництва та переробки продукції тваринництва
	    
Термін навчання				
	    1 рік 10 місяців 📣
	    
Бюджетна форма навчання		
	    Індивідуальна усна співбесіда, яка включає питання 
	    з фахових дисциплін + мотиваційний  лист 🖊
	    
Контрактна форма навчання		    Мотиваційний лист
Вартість навчання одного року		8000 грн. 

Залишилися питання?
Звертайтеся до секретаря приймальної комісії 📞 – Каленюк Оксани Ярославівни
+380502649020,
+380960050864.
''')


        elif message.text == 'Ветеринарна медицина 🐮':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            item1 = types.KeyboardButton('🐶🐱 Про ОПП(спеціальність) ')
            item2 = types.KeyboardButton('Відео-представлення 🎞')
            item3 = types.KeyboardButton('Алгоритм вступу 📝')
            back = types.KeyboardButton('Назад ◀')
            markup.add(item1, item2, item3, back)
            bot.send_message(message.chat.id, 'Оберіть наступний крок ⏭', reply_markup=markup)
        elif message.text == '🐶🐱 Про ОПП(спеціальність) ':
            bot.send_message(message.chat.id, '''
Освітньо – професійна програма 	
	    Ветеринарна медицина 🐣
	    
Спеціальність				
	    211 Ветеринарна медицина 🐮
	    
Галузь знань			
		21 Ветеринарна медицина 🐔
		
Кваліфікація: 
    Фаховий молодший бакалавр з ветеринарної медецини

Термін навчання				
	    2 роки 10 місяців ⌛
	    
Бюджетна форма навчання		
	    Індивідуальна усна співбесіда, яка включає питання
	     з фахових дисциплін + мотиваційний  лист ✏
	     
Контрактна форма навчання			Мотиваційний лист
Вартість навчання одного року		8000 грн. 

Залишилися питання? 📢
Звертайтеся до секретаря приймальної комісії 📞 – Каленюк Оксани Ярославівни
+380502649020,
+380960050864.
''')


        elif message.text == 'Алгоритм вступу 📝':

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            item1 = types.KeyboardButton('Основна сесія прийому 📱')
            item2 = types.KeyboardButton('Додаткова сесія прийому 📱')
            back = types.KeyboardButton('⬅ Назад')
            markup.add(item1, item2, back)

            bot.send_message(message.chat.id, 'Оберіть наступний крок ⏭',reply_markup=markup )


        elif message.text == 'Основна сесія прийому 📱':

            bot.send_message(message.chat.id, '''

<b>Крок1.</b> Реєстрація електронних кабінетів вступників та завантаження необхідних документів	:
    Розпочинається – 23 червня
    Завершується – 31 жовтня
<b>Крок2.</b> Початок прийому заяв та документів - 30 червня 
<b>Крок3.</b> Закінчується прийому заяв та документів о 18:00 годині 
    13 липня 
<b>Крок4.</b> Строки проведення індивідуальних усних  співбесід з 14 по 21 липня
<b>Крок5.</b> Рейтинговий список не пізніше: 12:00 год 26 липня
<b>Крок6.</b> Термін виконання вимог вступниками до 12:00 год 28 липня 
<b>Крок7.</b> Термін зарахування:
    за регіональним замовленням – не пізніше 18:00 год 30 липня;
    за кошти фізичних або юридичних осіб – не пізніше ніж 03 серпня ''', parse_mode='html')

        elif message.text == 'Додаткова сесія прийому 📱':
            bot.send_message(message.chat.id, '''
<b>Крок1.</b> Реєстрація електронних кабінетів вступників та завантаження необхідних документів	:
    Розпочинається – 23 червня
    Завершується – 31 жовтня
<b>Крок2.</b> Початок прийому заяв та документів - 8 серпня 
<b>Крок3.</b> Закінчується прийому заяв та документів о 18:00 годині 
    21 серпня 
<b>Крок4.</b> Строки проведення індивідуальних усних  співбесід з 22 по 25 серпня
<b>Крок5.</b> Рейтинговий список не пізніше: 12:00 год 26 липня
<b>Крок6.</b> Термін виконання вимог вступниками до 12:00 год 30 серпня
<b>Крок7.</b> Термін зарахування:
    за кошти фізичних або юридичних осіб – не пізніше ніж 31 серпня''', parse_mode= 'html')




        #----------------Кнопка Викладачу
        elif message.text == '👨‍🏫👩‍🏫 Викладачу':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            item1 = types.KeyboardButton('Сайти цикловох комісій 🎓')
            item2 = types.KeyboardButton('Підвищення кваліфікації 👩🏻‍🏫💹')
            item3 = types.KeyboardButton('Наша бібліотека 📔')
            back = types.KeyboardButton('⬅ Назад')
            markup.add(item1, item2, item3, back)
            bot.send_message(message.chat.id, 'Оберіть наступний крок ⏭',reply_markup= markup )

        elif message.text == 'Сайти цикловох комісій 🎓':
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton("Сайт циклової комісії комп'ютерної інженерії 🖥", url="https://lpmmliniv.wixsite.com/mdtek-oksm"))
            markup.add(types.InlineKeyboardButton("Сайт циклової комісії ветеринарної медецини 💉🩺",url="https://chornv83.wixsite.com/website"))
            markup.add(types.InlineKeyboardButton("Сайт циклової комісії управління та адміністрування 📂📈",url="https://mdtek7.wixsite.com/komisia"))
            bot.send_message(message.chat.id, 'Перейдіть за одним із посилань 👇🏻', reply_markup=markup)
        elif message.text == 'Підвищення кваліфікації 👩🏻‍🏫💹':
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton("План підвищення кваліфікації 📄", url="http://college.mlyniv.rv.ua/index.php?idi=df/viklad/#"))
            markup.add(types.InlineKeyboardButton("Презентація підвищення кваліфікації 🎦", url="http://college.mlyniv.rv.ua/df/viklad/PPK.pdf"))
            bot.send_message(message.chat.id, 'Перейдіть за потрібним вам посиланням ↖', reply_markup=markup)
        if message.text == 'Наша бібліотека 📔':
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton(" Наша бібліотека 📔",url="https://kohanuklarisa1.wixsite.com/library"))
            bot.send_message(message.chat.id, 'Бібліотека коледжу 🔎', reply_markup=markup)


        if message.text == '📞 Контакти':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            item1 = types.KeyboardButton('Адреса та контактні дані 📱')
            item2 = types.KeyboardButton('Соціальні мережі 💻⌨')
            item3 = types.KeyboardButton('Чат для спілкування 📢')
            item4 = types.KeyboardButton('Місце розташування 🏫')
            back = types.KeyboardButton('⬅ Назад')
            markup.add(item1, item2, item3,item4, back)
            bot.send_message(message.chat.id, 'Оберіть наступний крок ⏭', reply_markup=markup)
        if message.text == 'Соціальні мережі 💻⌨':
                    markup = types.InlineKeyboardMarkup()
                    markup.add(types.InlineKeyboardButton("🏛 Офіціальний сайт", url="http://college.mlyniv.rv.ua/"))
                    markup.add(types.InlineKeyboardButton("📣 Facebook", url="https://www.facebook.com/groups/mdtek/"))
                    markup.add(types.InlineKeyboardButton("📱 Instagram", url="https://www.instagram.com/mlyniv_mtefk/"))
                    markup.add(types.InlineKeyboardButton("📽 YouTube", url="https://www.youtube.com/channel/UCkMHHGSKwPR8UlGS_8gkBwA"))
                    bot.send_message(message.chat.id, 'Виберіть потрібну вам кнопку  😉', reply_markup=markup)
        elif message.text == 'Адреса та контактні дані 📱':
            bot.send_message(message.chat.id,
'''☎ Тел:
(03659)65495
(03659)64694 - факс 📠
(03659)65566
📧 Email : MDTEK@ukr.net 
Рівенська обл., смт.Млинів , вул. Івана Франка 1 , 35100 🚍''')
        elif message.text == 'Чат для спілкування 📢':
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton("Чат коледжу 🔊", url="https://t.me/+0jrUTT4Eqlc3ZWE6"))
            bot.send_message(message.chat.id, 'Перейдіть за посиланням, щоб долучитися до чату ✅', reply_markup=markup)
        elif message.text == 'Місце розташування 🏫':
            bot.send_message(message.chat.id,'https://www.google.com.ua/maps/place/Mlynivs%CA%B9kyy+Derzhavnyy+Tekhnoloho-Ekonomichnyy+Koledzh/@50.5081089,25.599495,15.71z/data=!4m5!3m4!1s0x472f803b0e263497:0x1727512a71856981!8m2!3d50.5058579!4d25.5985944?hl=ru')

#         elif message.text == '🏢🗣️ Про коледж':
#             bot.send_message(message.chat.id,
# '''Фаховий коледж розпочав свою діяльність як Млинівський зоотехнічний технікум 12.05.1958 📄
# Коледж має 2 навчальних корпуси 🏘, 2 гуртожитки, спортзал, тренажерний зал, їдальню 👩‍🍳, кафе.
# Підготовка фахівців здійснюється у 32 лабораторіях та кабінетах, обладнаних сучасними стендами 📮, технічними засобами навчання.
# У навчальному закладі є 4 комп’ютерні класи, які під’єднані до мережі Інтернет 🎮, створено електронну бібліотеку.
# Для відпрацювання професійних навичок є ветеринарна клініка 🧸, аптека, науково-дослідне господарство.
# Після закінчення навчального закладу студенти отримують диплом молодшого спеціаліста,
# атестат про повну середню освіту, набувають робочі професії
# за спеціальностями 🧑‍🎓: оператор комп’ютерного набору, оператор із штучного осіменіння сільськогосподарських тварин і птиці,
# обліковець з реєстрації бухгалтерських даних, менеджент, технолог.''')

        if message.text == '📸 Фото-галерея':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            item1 = types.KeyboardButton('Краєвид коледжу 🏞☀')
            item2 = types.KeyboardButton('Виховні заходи 💃🏼🏃🏻🎤')
            item3 = types.KeyboardButton('Студенські будні 📖🖊')
            item4 = types.KeyboardButton('Віртуальний тур коледжом 🚶🏻')
            back = types.KeyboardButton('⬅ Назад')
            markup.add(item1, item2, item3, item4, back)
            bot.send_message(message.chat.id, 'Оберіть наступний крок ⏭', reply_markup=markup)


        elif message.text == 'Краєвид коледжу 🏞☀':
            photo11 = open('1.1.JPG.', 'rb')
            photo12 = open('1.2.JPG', 'rb')
            photo13 = open('1.3.jpg', 'rb')
            photo14 = open('1.4.JPG', 'rb')
            photo15 = open('1.5.jpg', 'rb')
            media = [InputMediaPhoto(photo11), InputMediaPhoto(photo12), InputMediaPhoto(photo13), InputMediaPhoto(photo14), InputMediaPhoto(photo15) ]
            bot.send_media_group(message.chat.id, media, timeout= 120 )
        elif message.text == 'Виховні заходи 💃🏼🏃🏻🎤':
            photo21 = open('2.1.jpg.', 'rb')
            photo22 = open('2.2.jpg', 'rb')
            photo23 = open('2.3.jpg', 'rb')
            photo24 = open('2.4.jpg', 'rb')
            media2 = [InputMediaPhoto(photo21), InputMediaPhoto(photo22), InputMediaPhoto(photo23), InputMediaPhoto(photo24) ]
            bot.send_media_group(message.chat.id, media2, timeout=120)
        elif message.text == 'Студенські будні 📖🖊':
            photo31 = open('3.1.jpg', 'rb')
            photo32 = open('3.2.jpg', 'rb')
            photo33 = open('3.3.jpg', 'rb')
            photo34 = open('3.4.jpg', 'rb')
            media3 = [InputMediaPhoto(photo31), InputMediaPhoto(photo32), InputMediaPhoto(photo33),InputMediaPhoto(photo34) ]
            bot.send_media_group(message.chat.id, media3, timeout=120)
        elif message.text == 'Віртуальний тур коледжом 🚶🏻':
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton("Віртуальний тур 🚶🏻", url="https://www.google.com.ua/maps/@50.5058279,25.5986761,3a,75y,171.77h,93.17t/data=!3m8!1e1!3m6!1sAF1QipNNzUHyjlJhLz_RpQgAvoREasPVbwRh_Z_yeMHe!2e10!3e11!6shttps:%2F%2Flh5.googleusercontent.com%2Fp%2FAF1QipNNzUHyjlJhLz_RpQgAvoREasPVbwRh_Z_yeMHe%3Dw203-h100-k-no-pi-10-ya180-ro0-fo100!7i12000!8i6000"))
            bot.send_message(message.chat.id, 'Крокуй по коледжу онлайн 👍🏼', reply_markup=markup)


            bot.send_message(message.chat.id, 'Оберіть наступний крок ⏭')


        elif message.text == '⬅ Назад':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
            item1 = types.KeyboardButton('👨‍🎓👩‍🎓 Студенту')
            item2 = types.KeyboardButton('👦🏫 Вступнику')
            item3 = types.KeyboardButton('👨‍🏫👩‍🏫 Викладачу')
            item4 = types.KeyboardButton('🏢🗣️ Про коледж')
            item5 = types.KeyboardButton('📞 Контакти')
            item6 = types.KeyboardButton('📸 Фото-галерея')
            markup.add(item1, item2, item3, item4, item5, item6)
            bot.send_message(message.chat.id, 'Ви перейшли до головного меню 🇺🇦', reply_markup= markup)

        elif message.text == '↩ Назад':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            item1 = types.KeyboardButton('💼 Фаховий молодший бакалавр на основі БЗСО (9кл)')
            item2 = types.KeyboardButton('📑 Фаховий молодший бакалавр на основі ПЗСО (11кл)')
            item3 = types.KeyboardButton('📌 Фаховий молодший бакалавр на основі ОКР (кваліфікований робітник)')
            item4 = types.KeyboardButton('⬅ Назад')
            markup.add(item1, item2, item3,item4)
            bot.send_message(message.chat.id, 'Ви перейшли до попереднього меню 🇺🇦', reply_markup= markup)

        elif message.text == 'Назад  ↩':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            item1 = types.KeyboardButton('💼 Які документи потрібно для вступу')
            item2 = types.KeyboardButton('📑 Яку спеціальність я можу обрати')
            item3 = types.KeyboardButton('✏ Алгоритм вступу')
            item4 = types.KeyboardButton('📌 QR код для шерингу документів')
            item5 = types.KeyboardButton('↩ Назад')
            markup.add(item1, item2, item3,item4,item5)
            bot.send_message(message.chat.id, 'Ви перейшли до попереднього меню 🇺🇦', reply_markup= markup)
#--------------9 клас
        elif message.text == '↩  Назад':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            item1 = types.KeyboardButton('Облік і оподаткування 👩‍💼')
            item2 = types.KeyboardButton('Менеджмент 🧑‍💼')
            item3 = types.KeyboardButton('''Комп'ютерна інженерія 👨‍💻''')
            item4 = types.KeyboardButton('Технологія виробництва та переробки продукції тваринництва 🏭')
            item5 = types.KeyboardButton('Ветеринарна медицина 🩺')
            item6 = types.KeyboardButton('Назад  ↩')
            markup.add(item1,item2,item3,item4,item5,item6)
            bot.send_message(message.chat.id, 'Ви перейшли до попереднього меню 🇺🇦', reply_markup= markup)
#---------------11 клас
        elif message.text == '◀ Назад':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            item1 = types.KeyboardButton('👩‍💼 Облік і оподаткування')
            item2 = types.KeyboardButton('🧑‍💼 Менеджмент')
            item3 = types.KeyboardButton('''🧑‍💻 Комп'ютерна інженерія''')
            item4 = types.KeyboardButton('🏭 Технологія виробництва та переробки продукції тваринництва')
            item5 = types.KeyboardButton('🩺 Ветеринарна медицина')
            item6 = types.KeyboardButton('Назад  ↩')
            markup.add(item1,item2,item3,item4,item5,item6)
            bot.send_message(message.chat.id, 'Ви перейшли до попереднього меню 🇺🇦', reply_markup= markup)
#--------------Фах мол спец ---------
        elif message.text == 'Назад ◀':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            item1 = types.KeyboardButton('Облік і оподаткування 📋')
            item2 = types.KeyboardButton('Менеджмент 💼')
            item3 = types.KeyboardButton('''Комп’ютерна інженерія 💻''')
            item4 = types.KeyboardButton('Технологія виробництва та переробки продукції тваринництва 🐣')
            item5 = types.KeyboardButton('Ветеринарна медицина 🐮')
            item6 = types.KeyboardButton('Назад  ↩')
            markup.add(item1,item2,item3,item4,item5,item6)
            bot.send_message(message.chat.id, 'Ви перейшли до попереднього меню 🇺🇦', reply_markup= markup)


bot.polling(none_stop=True, interval=0)
