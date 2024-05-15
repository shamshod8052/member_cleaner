import traceback

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from environs import Env

from isgroup import IsGroup
from isprivate import IsPrivate

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

# .env fayl ichidan quyidagilarni o'qiymiz
BOT_TOKEN = env.str("BOT_TOKEN")  # Bot token

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())


@dp.message_handler(IsGroup(), content_types=types.ContentType.NEW_CHAT_MEMBERS)
@dp.message_handler(IsGroup(), content_types=types.ContentType.LEFT_CHAT_MEMBER)
async def delete_message(message: types.Message):
    try:
        await message.delete()
    except Exception:
        ...


@dp.message_handler(IsPrivate())
async def start(message: types.Message):
    await message.answer("🖐 Assalomu alaykum!\n\nBotni guruhingizga qo'shing va admin qiling!\n\n"
                         "Bot guruhingizdagi kirdi-chiqdini tozalab turadi.")


# Botni ishga tushirish
if __name__ == '__main__':
    from aiogram import executor

    executor.start_polling(dp, skip_updates=True)
