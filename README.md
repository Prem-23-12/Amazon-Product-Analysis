# Amazon Product Analysis

## Overview

This project performs Exploratory Data Analysis (EDA) on Amazon product data using Python. The goal is to analyze product categories, ratings, reviews, prices, and discounts to extract meaningful business insights.

The project uses Pandas, NumPy, and Matplotlib for data cleaning, analysis, and visualization.

---

## Features

* Data Cleaning and Preprocessing
* Missing Value Handling
* Duplicate Removal
* Product Category Analysis
* Rating Analysis
* Review Count Analysis
* Price Analysis
* Discount Analysis
* Data Visualization
* Insight Generation

---

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib

---

## Dataset Information

The dataset contains Amazon product information, including:

* Product Name
* Product Category
* Actual Price
* Discounted Price
* Discount Percentage
* Product Rating
* Rating Count
* Product Reviews

---

## Analysis Performed

### Product Category Analysis

* Identified the top product categories.
* Analyzed category distribution.

### Rating Analysis

* Calculated average product rating.
* Identified highest-rated products.

### Review Analysis

* Found the most reviewed products.
* Compared popularity using review counts.

### Price Analysis

* Identified the most expensive products.
* Compared actual and discounted prices.

### Discount Analysis

* Calculated and analyzed discount percentages.
* Found products offering the highest discounts.

---

## Visualizations

The project generates the following visualizations:

* Top Product Categories
* Ratings Distribution
* Top Rated Products
* Top Discounted Products

All generated charts are stored in the `output/` folder.

---

## Project Structure
"""
Amazon-Product-Analysis/

├── data/
│   └── amazon.csv

├── analysis/
│   └── analysis.py

├── output/
│   ├── top_categories.png
│   ├── ratings_distribution.png
│   ├── top_rated_products.png
│   ├── top_discounted_products.png
│   └── insights.txt

├── requirements.txt

├── .gitignore

└── README.md
"""
---

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/Amazon-Product-Analysis.git
```

Navigate to the project folder:

```bash
cd Amazon-Product-Analysis
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

Run the analysis script:

```bash
python analysis/analysis.py
```

The generated charts and insights will be saved in the `output/` directory.

---

## Key Insights

* Identified the most popular product categories.
* Determined the highest-rated products.
* Analyzed customer review trends.
* Compared actual and discounted prices.
* Discovered products with the highest discounts.

---

## Future Improvements

* Interactive Dashboard using Streamlit
* Advanced Visualizations using Seaborn
* Sentiment Analysis on Customer Reviews
* Machine Learning-based Product Recommendation System

---
