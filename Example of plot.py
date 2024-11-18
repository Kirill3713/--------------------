# Импортируем модули
import matplotlib.pyplot as plt

# Создаем график
# Задаем координаты
plt.plot([0, 0.1, 1, 1.5, 2, 2.5, 3], [1, 2, 3, 4, 5, 6, 7])
# Подписываем оси
plt.xlabel("см")
plt.ylabel("недели")
# Название графика
plt.title("Примерный график роста плодов моей прошлогодней редиски.")
# Показываем график
plt.show()