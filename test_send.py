from telegram import Bot

bot = Bot(token="7667772165:AAHFiO_YipJ8cwmhvFHt4hGtVM3f1b6q_2Y")
updates = bot.get_updates()

if not updates:
    print("Нет новых сообщений. Отправь боту сообщение в Telegram и попробуй снова.")
else:
    for update in updates:
        if update.message:
            print("Найдено сообщение от чата:", update.message.chat.id)
        else:
            print("Найдено обновление без сообщения:", update)
