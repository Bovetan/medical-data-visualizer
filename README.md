# Medical Data Visualizer

This project is part of the FreeCodeCamp Data Analysis with Python certification.

## Description

This project analyzes and visualizes medical examination data using Python, Pandas, Matplotlib, and Seaborn.

The dataset contains patient information such as body measurements, blood test results, and lifestyle habits. The goal is to explore how these variables relate to cardiovascular disease.

## Dataset

The dataset used is `medical_examination.csv`, which includes:

* Age
* Height
* Weight
* Blood pressure (ap_hi, ap_lo)
* Cholesterol
* Glucose
* Smoking status
* Alcohol intake
* Physical activity
* Cardiovascular disease (cardio)

## Tasks Completed

* Loaded and processed the dataset using Pandas
* Created an `overweight` column using BMI calculation
* Normalized cholesterol and glucose values (0 = good, 1 = bad)
* Built a categorical plot comparing health indicators by cardiovascular condition
* Cleaned the dataset by removing invalid and extreme values
* Generated a correlation heatmap to analyze relationships between variables

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn

## Project Files

* `medical_data_visualizer.py` → main implementation
* `main.py` → execution script
* `medical_examination.csv` → dataset
* `catplot.png` → categorical plot
* `heatmap.png` → heatmap

## Output

The project generates two visualizations:

* Categorical plot showing counts of health indicators grouped by cardiovascular disease
* Heatmap displaying correlations between medical variables

## Author

Bovetan
