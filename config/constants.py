from dataclasses import dataclass

# Настройки общей пагинации
COMMON_PAGE = 30
# Настройки вложенной в объект пагинации (история цен)
NESTED_PAGE = 10
# Кол-во выводимых предложений аналогов
MATCH_NUMBER = 10


# Статусы ключей дилеров
@dataclass
class KeyStatus:
    CHECK = "На проверку"
    DECLINED = "Не подходит"
    FOUND = "Подтверждено"
