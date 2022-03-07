import telebot
import random
from telebot import types

bot = telebot.TeleBot("5096378730:AAHAbMn9ZAfOwNaIsaOxGxLQjYpF9pTBo00")
jokes = ["Истина одна. В споре выигрывает тот, кто первый понял и заткнулся.",
         "Будет очень симметрично, если Зеленский станет мэром Батуми.",
         "Мы рождены, чтобы рубль сделать пылью!",
         "Странности - это неочевидные закономерности",
         "В полночь карета превратится в тыкву и можно будет хоть что-то сожрать.",
         "Правило бильярда - шарик нужно бить легко, как женщину.",
         "Люди делятся на тех, кто понуро идет в концлагерь, и тех кто идет в ополчение",
         "Мочевой пузырь - он как сердце: ему не прикажешь",
         "На Украину завезли вакцины Спутник V и Спутник Z. Вакцинация принудительная",
         "НАТО подало заявку для вступление в ВСУ.",
         "После приостановки работы Visa и Mastercard, в России воцарил МИР.",
         "Честность - неумение быстро придумать другие варианты..."]


@bot.message_handler(commands=['start'])
def start(message):
    hello = f"<b>Привет {message.from_user.first_name} это бот с плохими шутками</b>"
    bot.send_message(message.chat.id, hello, parse_mode='html')
    bot.send_message(message.chat.id, "Напиши комманду /get_joke чтобы бот рассказал шутку")


@bot.message_handler(commands=['get_joke'])
def get_joke(message, res=False):
    markup = types.ReplyKeyboardMarkup()
    button = types.KeyboardButton("Получить шутку")
    markup.add(button)
    fun_jokes = random.choice(jokes)
    bot.send_message(message.chat.id, fun_jokes, reply_markup=markup)




bot.polling(none_stop=True)