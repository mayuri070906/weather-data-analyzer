
import numpy as np
import matplotlib.pyplot as plt


def plot_weather(data):
    days = np.arange(1, len(data) + 1)

    temperature = data[:, 0]
    rainfall = data[:, 2]

    # Temperature line chart
    plt.figure(figsize=(10, 5))
    plt.plot(days, temperature, marker="o")
    plt.title("Daily Temperature Analysis")
    plt.xlabel("Day")
    plt.ylabel("Temperature (°C)")
    plt.xticks(days)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # Rainfall bar chart
    plt.figure(figsize=(10, 5))
    plt.bar(days, rainfall)
    plt.title("Daily Rainfall Analysis")
    plt.xlabel("Day")
    plt.ylabel("Rainfall (mm)")
    plt.xticks(days)
    plt.tight_layout()
    plt.show()
