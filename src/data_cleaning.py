
import numpy as np


def check_data_quality(data):
    print("\n===== DATA QUALITY REPORT =====")

    # Count missing or invalid values in each column
    column_names = [
        "Temperature",
        "Humidity",
        "Rainfall",
        "Wind Speed"
    ]

    for i, name in enumerate(column_names):
        invalid_count = np.sum(~np.isfinite(data[:, i]))
        print(f"{name}: {invalid_count} invalid values")

    print("Total records:", len(data))
