from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext
import requests

BOT_TOKEN = '7661745790:AAFvaGBVs-QZK7mtkJ9IkTtCmGM57gEPhK4'

def generate_phantom_link(user_id):
    redirect = "https://yourrenderapp.onrender.com/connect_callback"  # Replace after deploy
    return f"https://phantom.app/ul/v1/connect?app_url=ZombieBundler&redirect_link={redirect}&state={user_id}"

def start(update: Update, context: CallbackContext):
    user = update.effective_user
    user_id = str(user.id)
    
    keyboard = [
        [InlineKeyboardButton("🔗 Connect Wallet", url=generate_phantom_link(user_id))],
        [InlineKeyboardButton("🚀 Launch Coin", callback_data='launch')],
        [InlineKeyboardButton("📈 Buy Coin", callback_data='buy')],
        [InlineKeyboardButton("💣 Sell All", callback_data='sell')],
        [InlineKeyboardButton("🧨 Rugpull Now (Free x2)", callback_data='rugpull')],
        [InlineKeyboardButton("💎 Upgrade Plan", callback_data='upgrade')],
        [InlineKeyboardButton("👛 Show Wallet", callback_data='show_wallet')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(f"👋 Welcome {user.first_name}!", reply_markup=reply_markup)

def button(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    user_id = str(query.from_user.id)

    if query.data == "show_wallet":
        response = requests.get(f"https://yourrenderapp.onrender.com/get_wallet/{user_id}")
        wallet = response.json().get("wallet", "Not connected")
        query.edit_message_text(text=f"💼 Connected Wallet:\n{wallet}")
        return

    actions = {
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


def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CallbackQueryHandler(button))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
