
import numpy as np


def analyze_temperature(data):
    temperature = data[:, 0]

    return {
        "average": np.mean(temperature),
        "maximum": np.max(temperature),
        "minimum": np.min(temperature),
        "median": np.median(temperature),
        "std_deviation": np.std(temperature),
        "hottest_day": np.argmax(temperature) + 1,
        "coldest_day": np.argmin(temperature) + 1,
        "hot_days": np.where(temperature > 32)[0] + 1,
        "temperature_90th_percentile": np.percentile(
            temperature, 90
        ),
    }


def analyze_rainfall(data):
    rainfall = data[:, 2]

    return {
        "total": np.sum(rainfall),
        "average": np.mean(rainfall),
        "max": np.max(rainfall),
        "heavy_rain_days": np.where(rainfall > 5)[0] + 1,
    }
