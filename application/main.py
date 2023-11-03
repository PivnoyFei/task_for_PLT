import asyncio

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from pydantic import ValidationError

from aggregate import Aggregate
from logger import logger_config
from schemas import AggregateOut, MessageIn
from settings import settings

logger = logger_config(__name__)
dp: Dispatcher = Dispatcher()


@dp.message(CommandStart())
async def start_message(message: Message) -> None:
    await message.answer(f"Добро пожаловать, {message.from_user.full_name}!")


@dp.message()
async def listen_all_messages(message: Message) -> None:
    try:
        data = MessageIn.model_validate_json(message.text)
    except ValidationError as e:
        await message.answer(e.json())
    else:
        result: AggregateOut = await Aggregate().aggregate_result(**data.model_dump())
        await message.answer(f"{result.model_dump_json()}")


async def main() -> None:
    bot = Bot(settings.TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot, skip_updates=True)


if __name__ == "__main__":
    if all([settings.TOKEN, settings.MONGO_DATABASE_URI]):
        logger.info("Бот запущен")
        asyncio.run(main())
    else:
        logger.info("Нет переменной TOKEN")
