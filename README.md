# Topsis-Package

**Topsis-Package** is a Python library for implementing the **TOPSIS (Technique for Order Preference by Similarity to Ideal Solution)** method for multi-criteria decision analysis. It simplifies ranking and decision-making based on criteria weights and performance data.

---

## Installation

Install the package directly from PyPI:

```bash
pip install topsis-teena-102217049
```

---

## Usage

### Input

Prepare a CSV file with the following structure:

- The first row contains column headers (criteria names).
- The first column contains the names of alternatives (e.g., products or options).
- The remaining columns are numeric values representing the performance scores for each criterion.

### Example Input CSV (data.csv):

```csv
Alternative, Criterion 1, Criterion 2, Criterion 3, Criterion 4
Option A, 250, 16, 12, 5
Option B, 200, 22, 8, 6
Option C, 300, 18, 15, 4
Option D, 275, 20, 14, 7
```

### Running the Package

To execute, you will need:

- Path to the input CSV file.
- A comma-separated string of weights (e.g., `"0.4,0.3,0.2,0.1"`).
- A comma-separated string of impacts (e.g., `"+,+,-,-"`).

### Example Code:

```bash
topsis input.csv "0.4,0.3,0.2,0.1" "+,+,-,-" result.csv
```

### Input parameters

- input_file = "data.csv"
- weights = "0.4,0.3,0.2,0.1"
- impacts = "+,+,-,-"

### Output

The package will create a new CSV file with an additional column, **"Topsis Score"**, and the final **"Rank"** for each alternative.

**Example Output:**

```csv
Alternative, Criterion 1, Criterion 2, Criterion 3, Criterion 4, Topsis Score, Rank
Option A, 250, 16, 12, 5, 0.78, 2
Option B, 200, 22, 8, 6, 0.56, 4
Option C, 300, 18, 15, 4, 0.84, 1
Option D, 275, 20, 14, 7, 0.64, 3
```

---

## Features

- **Simple Input Format**: Provide your data in CSV format.
- **Customizable Weights and Impacts**: Define criteria importance and type (beneficial or non-beneficial).
- **Automated Output**: Generates scores and ranks for all alternatives.

---

## Requirements

This package requires Python 3.7 or higher. Install any missing dependencies using `pip`.

---

## Author

Developed by **Neha**.

---
