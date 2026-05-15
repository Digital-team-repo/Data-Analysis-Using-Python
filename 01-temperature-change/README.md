# Lesson 1: Temperature Change in Canada

This folder contains the technical resources for the Temperature Change in Canada analysis lesson.

## Dataset Information
* **Source:** Environment and Climate Change Canada (2025)
* **Dataset Name:** Temperature change in Canada
* **Original URL:** [Open Government Portal](https://open.canada.ca/data/en/dataset/8b01db78-b825-4d38-a66c-1a1712c382ee)
* **Indicator Page:** [Temperature Change - ECCC](https://www.canada.ca/en/environment-climate-change/services/environmental-indicators/temperature-change.html)
* **Reference Period:** 1948 to 2024
* **Baseline:** 1961-1990 average

## Files
* `notebook.ipynb`: The student-facing Jupyter notebook.
* `data.csv`: A cleaned version of the official Environment Canada annual temperature departure CSV.

## Data Cleaning Notes
The `data.csv` file in this folder has been modified for classroom use:
1. **Header Cleanup:** Descriptive title headers and blank rows at the top of the file were removed to allow direct loading in Pandas.
2. **Column Renaming:** Columns were simplified to `Year`, `Departure (Celsius)`, and `Ranking`.
3. **Footnote Relocation:** Footnotes and source citations were moved from the CSV file into this README to prevent data processing errors.

## Original Footnotes & Methodology
* **Temperature Departure:** The temperature departure is the difference between the average temperature for a given year and the average temperature for the reference period (1961 to 1990).
* **Ranking:** "1" indicates the warmest year on record since 1948. 2024 and 2010 are currently tied for the warmest year.
* **Coverage:** This indicator uses the Adjusted and Homogenized Canadian Climate Data (AHCCD) for temperature.
* **Citation:** Environment and Climate Change Canada (2025) Canadian Environmental Sustainability Indicators: Temperature change in Canada.
