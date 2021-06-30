# Дан словарь, содержащий данные о товаре из магазина
# "price" - цена товара в валюте "currency"
# "count" - количествотовара в магазине
# Считая,что курс доллара равен dollar_rate
# Вычислите цену всех товаров с названием "name" в долларах

item = {"name": "Кроссовки", "price": "7540.5", "currency": "rub", "count": "10"}
dollar_rate = 74.12

# TODO: your code here
products = {
    "name": "кроссовки",
   "price": "7540.5",
    "currency": "rub",
    "count": "10",
    "exchange_rate": dollar_rate
    #dollar_rate*"price"
}

print(int(products["exchange_rate"])*int(products["count"]))
