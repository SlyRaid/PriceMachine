# Задача:
Написать анализатор прайс-листов.

## Описание и требования: 
В папке находятся несколько файлов, содержащих прайс-листы от разных поставщиков.  
Количество и название файлов заранее неизвестно, однако точно известно, что в названии файлов прайс-листов есть слово "price".  
Файлы, не содержащие слово "price" следует игнорировать.  
Формат файлов: данные, разделенные точкой с запятой.  
Порядок колонок в файле заранее неизвестен, но известно, что столбец с названием товара называется одним из вариантов: "название", "продукт", "товар", "наименование".  
Столбец с ценой может называться "цена" или "розница".  
Столбец с весом имеет название "фасовка", "масса" или "вес" и всегда указывается в килограммах.  
Остальные столбцы игнорировать.  

## Особенности реализации:
Программа должна загрузить данные из всех прайс-листов и предоставить интерфейс для поиска товара по фрагменту названия с сорторовкой по цене за килогорамм.  
Интерфейс для поиска реализовать через консоль, циклически получая информацию от пользователя.  
Если введено слово "exit", то цикл обмена с пользователем завершается, программа выводит сообщение о том, что работа закончена и завершает свою работу. В противном случае введенный текст считается текстом для поиска. Программа должна вывести список найденных позиций в виде таблицы.

Список должен быть отсортирован по возрастанию стоимости за килограмм.
