import pytest
from string_utils import StringUtils

# Инициализация экземпляра класса для тестирования
utils = StringUtils()

# Тесты для функции capitilize
class TestCapitalize:
    
    @pytest.mark.parametrize("input_string, expected", [
        ("skypro", "Skypro"),           # Позитивный тест
        ("Skypro", "Skypro"),           # Первая буква уже заглавная
        ("123abc", "123abc"),           # Числа в начале
        ("", ""),                       # Пустая строка
        (" ", " "),                     # Строка с пробелом
        ("hello world", "Hello world"), # Строка с пробелами
    ])
    def test_capitalize(self, input_string, expected):
        assert utils.capitilize(input_string) == expected

# Тесты для функции trim
class TestTrim:
    
    @pytest.mark.parametrize("input_string, expected", [
        ("   skypro", "skypro"),        # Позитивный тест
        ("skypro", "skypro"),           # Без пробелов в начале
        ("   ", ""),                    # Только пробелы
        ("  hello  ", "hello  "),       # Пробелы в начале и конце
        ("", ""),                       # Пустая строка
    ])
    def test_trim(self, input_string, expected):
        assert utils.trim(input_string) == expected

# Тесты для функции to_list
class TestToList:
    
    @pytest.mark.parametrize("input_string, delimiter, expected", [
        ("a,b,c,d", ",", ["a", "b", "c", "d"]),     # Позитивный тест с дефолтным разделителем
        ("1:2:3", ":", ["1", "2", "3"]),            # Позитивный тест с кастомным разделителем
        ("", ",", []),                              # Пустая строка
        ("a", ",", ["a"]),                          # Один элемент
        ("a,b,,d", ",", ["a", "b", "", "d"]),       # Пустые элементы
        ("word1 word2 word3", " ", ["word1", "word2", "word3"]), # Пробел как разделитель
    ])
    def test_to_list(self, input_string, delimiter, expected):
        assert utils.to_list(input_string, delimiter) == expected
    
    def test_to_list_default_delimiter(self):
        # Тест с разделителем по умолчанию
        assert utils.to_list("a,b,c") == ["a", "b", "c"]

# Тесты для функции contains
class TestContains:
    
    @pytest.mark.parametrize("string, symbol, expected", [
        ("SkyPro", "S", True),          # Позитивный тест - символ есть
        ("SkyPro", "U", False),         # Позитивный тест - символа нет
        ("", "a", False),               # Пустая строка
        (" ", " ", True),               # Строка с пробелом
        ("Hello", "h", False),          # Регистрозависимость
        ("123", "2", True),             # Числа в строке
        ("multiple words", " ", True),  # Пробел как символ
    ])
    def test_contains(self, string, symbol, expected):
        assert utils.contains(string, symbol) == expected

# Тесты для функции delete_symbol
class TestDeleteSymbol:
    
    @pytest.mark.parametrize("string, symbol, expected", [
        ("SkyPro", "k", "SyPro"),               # Позитивный тест - удаление одного символа
        ("SkyPro", "Pro", "Sky"),               # Позитивный тест - удаление подстроки
        ("Hello", "x", "Hello"),                # Символ отсутствует
        ("", "a", ""),                          # Пустая строка
        ("aaa", "a", ""),                       # Удаление всех вхождений
        ("a b c", " ", "abc"),                  # Удаление пробелов
        ("Mississippi", "iss", "Mippi"),        # Удаление повторяющейся подстроки
    ])
    def test_delete_symbol(self, string, symbol, expected):
        assert utils.delete_symbol(string, symbol) == expected

# Тесты для функции starts_with
class TestStartsWith:
    
    @pytest.mark.parametrize("string, symbol, expected", [
        ("SkyPro", "S", True),          # Позитивный тест - начинается с символа
        ("SkyPro", "P", False),         # Позитивный тест - не начинается с символа
        ("", "a", False),               # Пустая строка
        (" ", " ", True),               # Строка с пробелом
        ("Hello", "h", False),          # Регистрозависимость
        ("123", "1", True),             # Числа в строке
        (" multiple", " ", True),       # Начинается с пробела
    ])
    def test_starts_with(self, string, symbol, expected):
        assert utils.starts_with(string, symbol) == expected

# Тесты для функции end_with
class TestEndWith:
    
    @pytest.mark.parametrize("string, symbol, expected", [
        ("SkyPro", "o", True),          # Позитивный тест - заканчивается символом
        ("SkyPro", "y", False),         # Позитивный тест - не заканчивается символом
        ("", "a", False),               # Пустая строка
        (" ", " ", True),               # Строка с пробелом
        ("Hello", "O", False),          # Регистрозависимость
        ("123", "3", True),             # Числа в строке
        ("multiple ", " ", True),       # Заканчивается пробелом
    ])
    def test_end_with(self, string, symbol, expected):
        assert utils.end_with(string, symbol) == expected

# Тесты для функции is_empty
class TestIsEmpty:
    
    @pytest.mark.parametrize("string, expected", [
        ("", True),                     # Пустая строка
        (" ", True),                    # Строка с пробелом
        ("   ", True),                  # Строка с несколькими пробелами
        ("SkyPro", False),              # Не пустая строка
        ("  hello  ", False),           # Строка с пробелами вокруг текста
        ("123", False),                 # Числа как строка
    ])
    def test_is_empty(self, string, expected):
        assert utils.is_empty(string) == expected

# Тесты для функции list_to_string
class TestListToString:
    
    @pytest.mark.parametrize("lst, joiner, expected", [
        ([1, 2, 3, 4], ", ", "1, 2, 3, 4"),            # Позитивный тест с числами
        (["Sky", "Pro"], ", ", "Sky, Pro"),             # Позитивный тест со строками
        (["Sky", "Pro"], "-", "Sky-Pro"),               # Кастомный разделитель
        ([], ", ", ""),                                 # Пустой список
        (["single"], ", ", "single"),                   # Один элемент
        ([1, "two", 3.0], ", ", "1, two, 3.0"),        # Разные типы данных
        (["a", "b", "c"], " | ", "a | b | c"),         # Разделитель с пробелами
    ])
    def test_list_to_string(self, lst, joiner, expected):
        assert utils.list_to_string(lst, joiner) == expected
    
    def test_list_to_string_default_joiner(self):
        # Тест с разделителем по умолчанию
        assert utils.list_to_string(["a", "b", "c"]) == "a, b, c"