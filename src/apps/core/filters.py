from telegram.ext.filters import Filters


class StringFilter:
    """Фильтр по полному совпадению строки.
    Используйте StringHandler(string='youstring') если отсутсвуют другие фильтры.
    Используйте в комбинации с другими фильтрами:
     filters = StringFilter.button(string) and AnotherFilter
    """
    class button(Filters.regex):
        def __init__(self, button_text):
            pattern = f'^({button_text})$'
            super().__init__(pattern)
