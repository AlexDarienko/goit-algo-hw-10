import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi

# Визначення функції та межі інтегрування
def f(x):
    return x ** 2

a = 0  # Нижня межа
b = 2  # Верхня межа

# Метод Монте-Карло для обчислення визначеного інтеграла
def monte_carlo_integration(f, a, b, num_samples=100000):
    samples = np.random.uniform(a, b, num_samples)
    sample_values = f(samples)
    integral_estimate = (b - a) * np.mean(sample_values)
    return integral_estimate

# Виконання інтегрування методом Монте-Карло
mc_result = monte_carlo_integration(f, a, b)
print("Інтеграл за методом Монте-Карло:", mc_result)

# Перевірка за допомогою функції quad з SciPy
result, error = spi.quad(f, a, b)
print("Аналітичний інтеграл (quad):", result)
print("Абсолютна помилка:", abs(mc_result - result))

# Візуалізація графіка функції та області інтегрування
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

fig, ax = plt.subplots()
ax.plot(x, y, 'r', linewidth=2)

# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title(f'Графік інтегрування f(x) = x^2 від {a} до {b}')
plt.grid()
plt.show()
