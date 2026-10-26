
from src.data_loader import load_weather_data
from src.analysis import analyze_temperature,analyze_rainfall
from src.data_cleaning import check_data_quality
from src.visualization import plot_weather



def main():
    data = load_weather_data()

    check_data_quality(data)

    results = analyze_temperature(data)
    rain = analyze_rainfall(data)

    print("\n===== TEMPERATURE ANALYSIS =====")
    print(f"Average: {results['average']:.2f} °C")
    print(f"Maximum: {results['maximum']:.2f} °C")
    print(f"Minimum: {results['minimum']:.2f} °C")
    print(f"Median: {results['median']:.2f} °C")
    print(f"Standard deviation: {results['std_deviation']:.2f} °C")
    print(f"Hottest day: Day {results['hottest_day']}")
    print(f"Coldest day: Day {results['coldest_day']}")
    print(f"Hot days above 32°C: {results['hot_days']}")
    print(
        f"90th percentile: "
        f"{results['temperature_90th_percentile']:.2f} °C"
    )

    print("\n===== RAINFALL ANALYSIS =====")
    print(f"Total rainfall: {rain['total']:.2f} mm")
    print(f"Average rainfall: {rain['average']:.2f} mm")
    print(f"Maximum rainfall: {rain['max']:.2f} mm")
    print(f"Heavy rainfall days (>5 mm): {rain['heavy_rain_days']}")
    plot_weather(data)


if __name__ == "__main__":
    main()
