import os
import csv
from tabulate import tabulate


class PriceMachine():

    def __init__(self):
        self.data = []
        self.result = ''

    def load_prices(self, file_path):
        files = os.listdir(file_path)
        prices = []
        for file in files:
            if 'price' in file.lower(): # учитывает название файлов в которых есть 'price'
                prices.append(file)
                with open(file=file, mode='r', encoding='utf-8') as file:
                    reader = csv.DictReader(file, delimiter=',')
                    headers = reader.fieldnames
                    for row in reader:
                        name_column, price_column, weight_column = None, None, None
                        for header in headers:
                            if header.lower() in ['название', 'продукт', 'товар', 'наименование']:
                                name_column = header
                            elif header.lower() in ['цена', 'розница']:
                                price_column = header
                            elif header.lower() in ['фасовка', 'масса', 'вес']:
                                weight_column = header
                        columns = [name_column, price_column, weight_column]
                        product_name = row.get(columns[0])
                        price = row.get(columns[1])
                        weight = row.get(columns[2])
                        price_per_kg = float(price) / float(weight)
                        self.data.append([product_name, price, weight, file.name, round(price_per_kg, 2)])

    def export_to_html(self, file_name='output.html'):
        with open(file_name, mode='w', encoding='utf-8') as file:
            file.write("<html><body>")
            self.data = sorted(self.data, key=lambda x: x[0]) # сортировка названий по алфавиту
            table = tabulate(self.data, headers=['Название', 'Цена', 'Вес', 'Файл', 'Цена за кг.'], tablefmt='html')
            file.write(table)
            file.write("</body></html>")

    def find_text(self, text):
        filtered_data = []
        for row in self.data:
            if text.lower() in row[0].lower():
                filtered_data.append(row)
        sorted_data = sorted(filtered_data, key=lambda x: x[4]) # сортировка по цене
        table = []
        for idx, row in enumerate(sorted_data):
            temp = [idx + 1]
            for item in row:
                temp.append(item)
            table.append(temp)
        self.result = tabulate(table, headers=["№", "Название", "Цена", "Вес", "Файл", "Цена за кг."], tablefmt="grid")
        print(self.result)


PM = PriceMachine()
PM.load_prices('D:\PyCharm\PriceListAnalyzer')

while True:
    search_text = input('Введите название товара для поиска (или "exit" для завершения): ')
    if search_text.lower() in ['exit']:
        print('the end')
        break
    PM.find_text(search_text)
    PM.export_to_html()