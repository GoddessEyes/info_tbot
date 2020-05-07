from telegram import ReplyKeyboardMarkup


def build_menu(
        buttons,
        n_cols: int,
        header_button=None,
        footer_button=None,
):
    menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
    if header_button:
        menu.insert(0, [header_button])
    if footer_button:
        menu.append([footer_button])
    return menu


def build_three_column_menu(buttons: list) -> ReplyKeyboardMarkup:
    """Построение обычного меню в три колонки."""
    menu = build_menu(
        buttons,
        n_cols=3,
    )

    return ReplyKeyboardMarkup(menu, resize_keyboard=True)
