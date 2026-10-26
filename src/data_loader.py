
import numpy as np
from pathlib import Path


def load_weather_data():
    project_root = Path(__file__).resolve().parent.parent
    file_path = project_root / "data" / "weather.csv"

    data = np.genfromtxt(
        file_path,
        delimiter=",",
        skip_header=1,
        dtype=float,
        usecols=(1, 2, 3, 4),
        encoding="utf-8"
    )

    # Ensure data is always a 2D array
    if data.ndim == 1:
        data = data.reshape(1, -1)

    # Remove rows containing NaN or infinity
    data = data[np.isfinite(data).all(axis=1)]

    if data.size == 0:
        raise ValueError("No valid weather records found in CSV.")


    return data
