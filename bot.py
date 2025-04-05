from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

BOT_TOKEN = '7884424893:AAG2sVbxs4uRzEqEvotYr8jnXudiebq69dw'

def start(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    keyboard = [
        [InlineKeyboardButton("🪙 Connect Wallet", callback_data='connect')],
        [InlineKeyboardButton("🚀 Launch Coin", callback_data='launch')],
        [InlineKeyboardButton("📈 Buy Coin", callback_data='buy')],
        [InlineKeyboardButton("💣 Sell All", callback_data='sell')],
        [InlineKeyboardButton("🧨 Rugpull Now (Free x2)", callback_data='rugpull')],
        [InlineKeyboardButton("💎 Upgrade Plan", callback_data='upgrade')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # ✅ Yeh dono line andar rakho
    update.message.reply_text(f"👋 Welcome {user.first_name}!")
    update.message.reply_text("I am your Zombie Bundler bot. What would you like to do?", reply_markup=reply_markup)

def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()
    
    actions = {
        'connect': "🔗 Please connect your Phantom Wallet...",
        'launch': "🚀 Coin launch feature coming soon...",
        'buy': "📈 Auto-buy system initializing...",
        'sell': "💣 Selling all your coins...",
        'rugpull': "🧨 Executing Rugpull (Free remaining: 2)...",
        'upgrade': "💎 Upgrade to premium to unlock unlimited rugpulls."
    }

    response = actions.get(query.data, "Unknown action.")
    query.edit_message_text(text=response)

def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CallbackQueryHandler(button))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
