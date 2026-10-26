
import numpy as np
from src.analysis import analyze_temperature, analyze_rainfall


def test_temperature_analysis():
    # Columns: temperature, humidity, rainfall, wind speed
    data = np.array([
        [20.0, 60, 0.0, 10.0],
        [30.0, 50, 5.0, 15.0],
        [40.0, 70, 10.0, 20.0]
    ])

    result = analyze_temperature(data)

    assert result["average"] == 30.0
    assert result["maximum"] == 40.0
    assert result["minimum"] == 20.0
    assert result["hottest_day"] == 3
    assert result["coldest_day"] == 1


def test_rainfall_analysis():
    data = np.array([
        [20.0, 60, 0.0, 10.0],
        [30.0, 50, 5.0, 15.0],
        [40.0, 70, 10.0, 20.0]
    ])

    result = analyze_rainfall(data)

    assert result["total"] == 15.0
    assert result["max"] == 10.0
    assert np.array_equal(
        result["heavy_rain_days"],
        np.array([3])
    )
