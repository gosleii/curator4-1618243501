import telebot

bot = telebot.TeleBot("7109592655:AAF3NZAWDBpRmzqwgY0SvOHxhMmAHcrF7yw")


@bot.message_handler(commands=["start"])
def he(message):
    bot.send_message(message.chat.id,
                     "_Привет, сегодня я расскажу тебе о неизвестном никому парне. Его зовут Маффаэль Клауд. Ему 25 лет и он работает в пекарне._",
                     parse_mode="Markdown")


@bot.message_handler(commands=["appearance"])
def view(message):
    bot.send_message(message.chat.id,
                     "*Его внешность: кудрявые пшенично-золотые волосы, курносый нос, темно-синие глаза, пухлые губы. И самое интересное в нем это то, что он пухлый парень. Осанку держит всегда прямо, но при этом все равно складывается ощущение неуклюжести и некой тяжести.*",
                     parse_mode="Markdown")


@bot.message_handler(commands=["character"])
def nature(message):
    bot.send_message(message.chat.id,
                     "*Характер же нежен, ласков и немного робок. Он очень добр к другим людям и очень эмпатичен. Но несмотря на все это, он целеустремленный, уверенный и даже слегка наглый парень(хоть использует эти качества не всегда).*",
                     parse_mode="Markdown")


@bot.message_handler(commands=["fact"])
def thing(message):
    bot.send_message(message.chat.id,
                     "*Маффаэль очень сильно любит свою работу, а так же всех клиентов, которых он обслужил. Его любимый цвет - лиловый. А любимое животное - козленок. Из еды Мафф предпочтет брауни с апельсиновым соком. И он кстати скорее жаворонок, чем сова.)*",
                     parse_mode="Markdown")


@bot.message_handler(commands=["style"])
def tone(message):
    bot.send_message(message.chat.id,
                     "*Old money (стиль одежды), который он обожает использовать, хотя этот стиль контрастирует с его характером. Используя этот стиль он часто не попадает в нужный дресс-код. Из-за чего у других людей сложилось мнение, что у Маффи нет вкуса стиля.*",
                     parse_mode="Markdown")


bot.infinity_polling()