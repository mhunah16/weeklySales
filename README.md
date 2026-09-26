# WeeklySales

A simple Python utility for tracking daily sales over a week, calculating the weekly average, and predicting the following week's sales based on that average.

## Features

- Collects sales figures for each day of the week (Mon–Sun) via console input
- Calculates the average sales for the week
- Predicts next week's sales by projecting the weekly average across 7 days

## Requirements

- Python 3.x (no external dependencies)

## Usage

Run the script directly:

```bash
python sales.py
```

You will be prompted to enter a sales figure for each day:

```
Enter sales for each day:
Mon: 120
Tue: 150
Wed: 100
Thu: 200
Fri: 180
Sat: 220
Sun: 90
```

After all seven values are entered, the script prints a summary:

```
--- Results ---
Your sales: [120.0, 150.0, 100.0, 200.0, 180.0, 220.0, 90.0]
Average sales: 151.43
Predicted next week: [151.43, 151.43, 151.43, 151.43, 151.43, 151.43, 151.43]
```

## API

### `WeeklySales`

A class that collects and analyzes one week of sales data.

- **`__init__()`** — Prompts for and stores sales figures for each of the 7 days in `self.sales`.
- **`average_sales()`** — Returns the average of the week's sales as a float.
- **`predict_next_week()`** — Returns a list of 7 values, each equal to the rounded weekly average, as a simple forecast for the following week.

## Notes

- Sales input must be numeric; non-numeric input will raise a `ValueError`.
- The prediction model is a naive average-based forecast — it assumes next week's sales will be flat and equal to this week's average, with no trend or seasonality factored in.
