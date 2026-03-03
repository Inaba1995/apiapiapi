from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import CommandStart, Command
from api_services import get_weather, get_currency

router = Router()

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Погода 🌤️"), KeyboardButton(text="Курсы валют 💰")]

    ],
    resize_keyboard=True
)

@router.message(CommandStart())
async def start(message: Message):
    await message.answer(
        f"Привет, {message.from_user.first_name}! Я Мульти помощник.\n"
        "Выбери действие:",
        reply_markup=main_menu
    )

@router.message(F.text == "Погода 🌤️")
async def weather_handler(message: Message):
    weather = await get_weather()
    await message.answer(weather, reply_markup=main_menu)

@router.message(F.text == "Курсы валют 💰")
async def currency_handler(message: Message):
    currency = get_currency()
    await message.answer(currency, reply_markup=main_menu)







