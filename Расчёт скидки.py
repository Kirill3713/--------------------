order_cost = 250 # стоимость заказа
discount_cost = 1 # множитель скидки. Если 1, то платят полную стоимость, если 0, то не платят ничего.
# Запрашиваем возраст покупателя
try:
    age = int(input("Введите свой возраст: "))
except ValueError:
    print("Введено некорректное значение!")
    quit()
# Расчет скидки
if age < 18:
    # скидка 5%
    discount_cost = 0.95
elif age < 30:
    discount_cost = 0.85
elif age < 60:
    discount_cost = 0.75
elif age < 100:
    discount_cost = 0.50
else:
    discount_cost = 0
    print("Пожалуйста, не рассказывайте про нас Вашим подругам, иначе мы обанкротимся. Или если они уже лежат и не смогут прийти быстро (днем), то пусть, пожалуйста, не приходят, а то они других посетителей распугают.")
# Выводим стоимость
print("Стоимость заказа со скидкой:", order_cost * discount_cost)
# если клиенту меньше 18, то скидка 5%;
# иначе если клиенту меньше 30, то скидка 15%;
# иначе если клиенту меньше 60, то скидка 25%;
# иначе если клиенту меньше 100, то скидка 50%;
# иначе бесплатно.