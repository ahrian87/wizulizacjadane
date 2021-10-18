import matplotlib.pyplot as plt

x_values = range(1, 6)
y_values = [x**3 for x in x_values]

plt.style.use('Solarize_Light2')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c="blue", s=50)

# Zdefiniowanie tytułu wykresu i etykiet osi
ax.set_title("Sześciany liczb", fontsize=24)
ax.set_xlabel("Wartość", fontsize=14)
ax.set_ylabel("Sześciany wartości", fontsize=14)

# Zdefiniowanie wielkości etykiet.
ax.tick_params(axis="both", labelsize=14)

# Zdefiniowanie zakresu dla każdej osi.
ax.axis([0, 6, 0, 150])

plt.show()