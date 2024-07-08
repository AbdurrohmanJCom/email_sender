# pip install matplotlib

import numpy as np
import matplotlib.pyplot as plt

# Создание диапазона x-значений
x = np.linspace(-2, 2, 400)

# Определение экспоненциальных функций
y_growth = np.exp(x)  # Экспоненциальный рост
y_decay = np.exp(-x)  # Экспоненциальное затухание

# Построение графиков
plt.figure(figsize=(10, 5))

# График экспоненциального роста
plt.plot(x, y_growth, label='Экспоненциальный рост: $e^x$', color='blue')

# График экспоненциального затухания
plt.plot(x, y_decay, label='Экспоненциальное затухание: $e^{-x}$', color='red')

# Добавление подписей и легенды
plt.title('Графики экспоненциальных функций')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.legend()

# Отображение графика
plt.show()