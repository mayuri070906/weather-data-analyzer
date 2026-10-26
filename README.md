# Weather Data Analyzer

## Project Overview
Weather Data Analyzer is a beginner-friendly Python project that analyzes daily weather data using NumPy and visualizes patterns using Matplotlib.

The project calculates temperature statistics, analyzes rainfall, identifies hot and heavy-rainfall days, and generates charts to help understand weather patterns.

**Note:** The included weather dataset is sample data created for learning and demonstration. It is not actual recorded weather.

## Features
- Load weather data from a CSV file using NumPy.
- Check data quality and identify invalid values.
- Calculate average, minimum, maximum, and median temperature.
- Calculate temperature standard deviation and 90th percentile.
- Identify hot days and heavy-rainfall days.
- Calculate total, average, and maximum rainfall.
- Visualize daily temperature and rainfall using charts.
- Run automated tests using pytest.

## Technologies Used
- Python
- NumPy
- Matplotlib
- CSV
- Pytest

## Project Structure

```text
weather-data-analyzer/
├── data/
│   └── weather.csv
├── notebooks/
│   └── weather_analysis.ipynb
├── src/
│   ├── data_loader.py
│   ├── data_cleaning.py
│   ├── analysis.py
│   └── visualization.py
├── tests/
│   └── test_analysis.py
├── main.py
├── requirements.txt
└── README.md
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd weather-data-analyzer
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with your actual GitHub repository URL.

### 2. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 3. Run the project

```bash
python main.py
```

The program displays weather analysis results and generates temperature and rainfall charts.

### 4. Run automated tests

```bash
python -m pytest -v
```

## Concepts Demonstrated
- NumPy arrays and array indexing
- Statistical calculations
- Boolean filtering and conditional selection
- Data cleaning basics
- Data visualization
- Python modules and functions
- Automated testing

## Future Improvements
- Add real weather data from a weather API.
- Display actual dates instead of record numbers.
- Add humidity and wind-speed analysis.
- Create an interactive dashboard.
- Export analysis results to CSV.

## Learning Outcome
This project demonstrates foundational skills in Python programming, numerical data analysis, visualization, and testing.
