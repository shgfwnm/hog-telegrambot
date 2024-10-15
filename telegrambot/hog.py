from telegram import Updater, CommandHandler, MessageHandler, Filters, ReplyKeyboardMarkup
from telegram.ext import CallbackContext, CommandHandler, MessageHandler, Filters
import random


houses = ["گریفندور", "اسلیترین", "هافلپاف", "ریونکلا"]

def start(update, context):
    keyboard = [["ادامه"], ["ارتباط با ما"], ["گروهبندی مجدد"]]
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)
    update.message.reply_text('سلام! خوش آمدید به ربات گروهبندی هاگوارتز. برای شروع، دکمه ادامه را فشار دهید.', reply_markup=reply_markup)

def continue_grouping(update, context):
    update.message.reply_text("لطفاً نام خود را وارد کنید:")
    return "NAME"

def receive_name(update, context):
    context.user_data['name'] = update.message.text
    update.message.reply_text("سن خود را وارد کنید:")
    return "AGE"

def receive_age(update, context):
    context.user_data['age'] = update.message.text
    update.message.reply_text("شخصیت مورد علاقه خود را وارد کنید:")
    return "FAVORITE_CHARACTER"

def receive_favorite_character(update, context):
    context.user_data['favorite'] = update.message.text
    result = random.choice(houses)
    update.message.reply_text(f"گروه شما: *{result}* 🏰", parse_mode='Markdown')

   
    keyboard = [["ارتباط با ما"], ["گروهبندی مجدد"]]
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)
    update.message.reply_text("برای ارتباط با ما دکمه مربوطه را فشار دهید یا می‌توانید دوباره گروهبندی کنید.", reply_markup=reply_markup)

def contact_us(update, context):
    update.message.reply_text("@NmmNmmNmmNn")

def restart_grouping(update, context):
    start(update, context)
    return ConversationHandler.END

from telegram.ext import ConversationHandler


conv_handler = ConversationHandler(
    entry_points=[CommandHandler('start', start)],
    states={
        "NAME": [MessageHandler(Filters.text & ~Filters.command, receive_name)],
        "AGE": [MessageHandler(Filters.text & ~Filters.command, receive_age)],
        "FAVORITE_CHARACTER": [MessageHandler(Filters.text & ~Filters.command, receive_favorite_character)],
    },
    fallbacks=[
        CommandHandler('start', start),
        MessageHandler(Filters.regex('^ارتباط با ما$'), contact_us),
        MessageHandler(Filters.regex('^گروهبندی مجدد$'), restart_grouping)
    ],
)

def main():
    updater = Updater("7894863381:AAG7xOnUAoh2sc9GhMv2j0b4rpn4aie4Uk0", use_context=True)
    dp = updater.dispatcher

   
    dp.add_handler(conv_handler)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
