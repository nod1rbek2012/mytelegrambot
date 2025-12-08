import telebot
from telebot import types

bot = telebot.TeleBot("8591382657:AAGSQEX0oJDkQo_hTDruSqvV-BbDey8aqOw")

# === START ===
@bot.message_handler(commands=['start'])
def start(message):
    menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
    menu.add("📚 Dars jadvali")
    menu.add("🧠 Mantiqiy savollar")
    menu.add("Test yaratish ")

    bot.send_message(
        message.chat.id,
        "Asosiy menyu 👇",
        reply_markup=menu
    )

# === ASOSIY HANDLER ===
@bot.message_handler(func=lambda m: True)
def handler(message):

    if message.text == "📚 Dars jadvali":
        classes = types.ReplyKeyboardMarkup(resize_keyboard=True)
        classes.add("5-sinf")
        classes.add("6-sinf")
        classes.add("7-sinf")
        classes.add("8-sinf")
        classes.add("9-sinf")
        classes.add("10-sinf")
        classes.add("11-sinf")
        classes.add("⬅️ Orqaga")

        bot.send_message(
            message.chat.id,
            "Sinfni tanlang 👇",
            reply_markup=classes
        )
    elif message.text == "5-sinf":
        s5 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        s5.add("5-01", "5-02")
        s5.add("⬅️ Orqaga")
        bot.send_message(message.chat.id, "5-sinf guruhini tanlang 👇", reply_markup=s5)
    elif message.text == "5-01":
        with open("5-01.jpg", "rb") as photo:
            bot.send_photo(
                message.chat.id,
                photo,
                caption="📚 5 sinf dars jadvali")
    elif message.text == "5-02":
        with open("5-02.jpg", "rb") as photo:
            bot.send_photo(
                message.chat.id,
                photo,
                caption="📚 5-02 sinf dars jadvali"
            )
    elif message.text == "6-sinf":
        s5 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        s5.add("6-01", "6-02")
        s5.add("⬅️ Orqaga")
        bot.send_message(message.chat.id, "6-sinf guruhini tanlang 👇", reply_markup=s5)
    elif message.text == "6-01":
        with open("6-01.jpg", "rb") as photo:
            bot.send_photo(
                message.chat.id,
                photo,
                caption="📚 6-01 sinf dars jadvali"
            )
    elif message.text == "6-02":
        with open("6-02.jpg", "rb") as photo:
            bot.send_photo(
                message.chat.id,
                photo,
                caption="📚 6-02 sinf dars jadvali"
            )
    elif message.text == "7-sinf":
        s5 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        s5.add("7-01", "7-02","7-03")
        s5.add("⬅️ Orqaga")
        bot.send_message(message.chat.id, "6-sinf guruhini tanlang 👇", reply_markup=s5)
    elif message.text == "7-01":
        with open("7-01.jpg", "rb") as photo:
            bot.send_photo(
                message.chat.id,
                photo,
                caption="📚 7-01 sinf dars jadvali"
            )
    elif message.text == "7-02":
        with open("7-02.jpg", "rb") as photo:
            bot.send_photo(
                message.chat.id,
                photo,
                caption="📚 7-02 sinf dars jadvali"
            )
    elif message.text == "7-03":
        with open("7-03.jpg", "rb") as photo:
            bot.send_photo(
                message.chat.id,
                photo,
                caption="📚 7-03 sinf dars jadvali"
            )
    elif message.text == "8-sinf":
        s5 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        s5.add("8-01", "8-02","8-03")
        s5.add("⬅️ Orqaga")
        bot.send_message(message.chat.id, "6-sinf guruhini tanlang 👇", reply_markup=s5)
    elif message.text == "8-01":
        with open("8-01.jpg", "rb") as photo:
            bot.send_photo(
                message.chat.id,
                photo,
                caption="📚 8-01 sinf dars jadvali"
            )
    elif message.text == "8-02":
        with open("8-02.jpg", "rb") as photo:
            bot.send_photo(
                message.chat.id,
                photo,
                caption="📚 8-02 sinf dars jadvali"
            )
    elif message.text == "8-03":
        with open("8-03.jpg", "rb") as photo:
            bot.send_photo(
                message.chat.id,
                photo,
                caption="📚 8-03 sinf dars jadvali"
            )
    elif message.text == "9-sinf":
        s5 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        s5.add("9-01", "9-02","9-03")
        s5.add("⬅️ Orqaga")
        bot.send_message(message.chat.id, "6-sinf guruhini tanlang 👇", reply_markup=s5)
    elif message.text == "9-01":
        with open("9-01.jpg", "rb") as photo:
            bot.send_photo(
                message.chat.id,
                photo,
                caption="📚 9-01 sinf dars jadvali"
            )
    elif message.text == "9-02":
        with open("9-02.jpg", "rb") as photo:
            bot.send_photo(
                message.chat.id,
                photo,
                caption="📚 9-02 sinf dars jadvali"
            )
    elif message.text == "9-03":
        with open("9-03.jpg", "rb") as photo:
            bot.send_photo(
                message.chat.id,
                photo,
                caption="📚 9-03 sinf dars jadvali"
            )
    elif message.text == "10-sinf":
        s5 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        s5.add("10-01", "10-02","10-03")
        s5.add("⬅️ Orqaga")
        bot.send_message(message.chat.id, "6-sinf guruhini tanlang 👇", reply_markup=s5)
    elif message.text == "10-01":
        with open("10-01.jpg", "rb") as photo:
            bot.send_photo(
                message.chat.id,
                photo,
                caption="📚 10-01 sinf dars jadvali"
            )
    elif message.text == "10-02":
        with open("10-02.jpg", "rb") as photo:
            bot.send_photo(
                message.chat.id,
                photo,
                caption="📚 10-02 sinf dars jadvali"
            )
    elif message.text == "10-03":
        with open("10-03.jpg", "rb") as photo:
            bot.send_photo(
                message.chat.id,
                photo,
                caption="📚 10-03 sinf dars jadvali"
            )
    elif message.text == "11-sinf":
        s5 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        s5.add("11-01", "11-02","11-03")
        s5.add("⬅️ Orqaga")
        bot.send_message(message.chat.id, "6-sinf guruhini tanlang 👇", reply_markup=s5)
    elif message.text == "11-01":
        with open("11-01.jpg", "rb") as photo:
            bot.send_photo(
                message.chat.id,
                photo,
                caption="📚 11-01 sinf dars jadvali"
            )
    elif message.text == "11-02":
        with open("11-02.jpg", "rb") as photo:
            bot.send_photo(
                message.chat.id,
                photo,
                caption="📚 11-02 sinf dars jadvali"
            )
    elif message.text == "11-03":
        with open("11-03.jpg", "rb") as photo:
            bot.send_photo(
                message.chat.id,
                photo,
                caption="📚 11-03 sinf dars jadvali"
            )
    elif message.text == "⬅️ Orqaga":
        start(message)

    elif message.text == "🧠 Mantiqiy savollar":
        bot.send_message(message.chat.id, "Tez orada 🤔")

    else:
        bot.send_message(message.chat.id, "Menyudan tanlang 👆")

bot.polling(none_stop=True)
