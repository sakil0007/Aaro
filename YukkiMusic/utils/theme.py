import random
from YukkkMusic.utils.database import get_theme

themes = [
    "arch1",
    "arch2",
    "arch3",
    "arch4",
    "arch5",
    "arch6",
    "arch7",
    "arch8",
]


async def check_theme(chat_id: int):
    _theme = await get_theme(chat_id, "theme")
    if not _theme:
        theme = random.choice(themes)
    else:
        theme = _theme["theme"]
        if theme == "Random":
            theme = random.choice(themes)
    return theme
