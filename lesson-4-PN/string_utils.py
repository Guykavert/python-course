class StringUtils:
    """
    Класс с полезными утилитами для обработки и анализа строк
    """
    
    def capitilize(self, string: str) -> str:
        """
        Принимает на вход текст, делает первую букву заглавной и возвращает этот же текст
        Пример: `capitilize("skypro") -> "Skypro"`
        """
        return string.capitalize()
    
    def trim(self, string: str) -> str:
        """
        Принимает на вход текст и удаляет пробелы в начале, если они есть
        Пример: `trim("   skypro") -> "skypro"`
        """
        whitespace = " "
        while string.startswith(whitespace):
            string = string.removeprefix(whitespace)
        return string
    
    def to_list(self, string: str, delimiter: str = ",") -> list:
        """
        Принимает на вход текст с разделителем и возвращает список строк. \n
        Параметры: \n 
            string: строка для обработки \n
            delimiter: разделитель. По умолчанию запятая (",") \n
        Пример 1: `to_list("a,b,c,d") -> ["a", "b", "c", "d"]`
        Пример 2: `to_list("1:2:3", ":") -> ["1", "2", "3"]`
        """
        if len(string) == 0:
            return []
        
        return string.split(delimiter)

    def contains(self, string: str, symbol: str) -> bool:
        """
        Возвращает `True`, если строка содержит искомый символ и `False` - если нет \n 
        Параметры: \n
            string: строка для обработки \n
            symbol: искомый символ \n
        Пример 1: `contains("SkyPro", "S") -> True`
        Пример 2: `contains("SkyPro", "U") -> False`
        """
        return symbol in string

    def delete_symbol(self, string: str, symbol: str) -> str:
        """
        Удаляет все подстроки из переданной строки \n 
        Параметры: \n
            string: строка для обработки \n
            symbol: искомый символ для удаления \n
        Пример 1: `delete_symbol("SkyPro", "k") -> "SyPro"`
        Пример 2: `delete_symbol("SkyPro", "Pro") -> "Sky"`
        """
        if symbol not in string:
            return string
        
        return string.replace(symbol, "")

    def starts_with(self, string: str, symbol: str) -> bool:
        """
        Возвращает `True`, если строка начинается с заданного символа и `False` - если нет \n 
        Параметры: \n
            string: строка для обработки \n
            symbol: искомый символ \n
        Пример 1: `starts_with("SkyPro", "S") -> True`
        Пример 2: `starts_with("SkyPro", "P") -> False`
        """
        return string.startswith(symbol)

    def end_with(self, string: str, symbol: str) -> bool:
        """
        Возвращает `True`, если строка заканчивается заданным символом и `False` - если нет \n 
        Параметры: \n
            string: строка для обработки \n
            symbol: искомый символ \n
        Пример 1: `end_with("SkyPro", "o") -> True`
        Пример 2: `end_with("SkyPro", "y") -> False`
        """
        return string.endswith(symbol)

    def is_empty(self, string: str) -> bool:
        """
        Возвращает `True`, если строка пустая и `False` - если нет \n 
        Пример 1: `is_empty("") -> True`
        Пример 2: `is_empty(" ") -> True`
        Пример 3: `is_empty("SkyPro") -> False`
        """
        if len(string) == 0:
            return True
        while " " in string:
            string = string.replace(" ", "")
        if len(string) == 0:
            return True
        return False

    def list_to_string(self, lst: list, joiner: str = ", ") -> str:
        """
        Преобразует список элементов в строку с указанным разделителем \n 
        Параметры: \n
            lst: список элементов \n
            joiner: разделитель. По умолчанию запятая (", ") \n
        Пример 1: `list_to_string([1,2,3,4]) -> "1, 2, 3, 4"`
        Пример 2: `list_to_string(["Sky", "Pro"]) -> "Sky, Pro"`
        Пример 3: `list_to_string(["Sky", "Pro"], "-") -> "Sky-Pro"`
        """
        string = ""
        length = len(lst)
        
        if length == 0:
            return string
        
        for i in range(length):
            string += str(lst[i])
            if i != length - 1:
                string += joiner
        
        return string