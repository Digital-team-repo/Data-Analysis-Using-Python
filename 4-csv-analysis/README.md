# Lesson 3: CSV Analysis (Temperature Change Dataset)

This folder contains the technical resources for Lesson 3, which focuses on CSV analysis using a Temperature Change in Canada dataset.

## Dataset Information
* **Source:** Environment and Climate Change Canada (2025)
* **Dataset Name:** Temperature change in Canada
* **Indicator Page:** [Temperature Change - ECCC](https://www.canada.ca/en/environment-climate-change/services/environmental-indicators/temperature-change.html)
* **Reference Period:** 1948 to 2024
* **Baseline:** 1961-1990 average

## Files
* `notebook.ipynb`: The student-facing Jupyter notebook.
* `data_en.csv`: Cleaned English CSV for classroom use.
* `data_fr.csv`: Cleaned French CSV for classroom use.

## Data Cleaning Notes
The CSV files in this folder have been modified for classroom use:
1. **Header Cleanup:** Descriptive title headers and blank rows at the top of the file were removed to allow direct loading in Pandas.
2. **Column Standardization:** Column names were standardized for instructional readability:
   * English: `Year`, `Temperature departure (degree Celsius)`, `Warmest year ranking`
   * French: `Année`, `Écart de températures (degrés Celsius)`, `Classement des années les plus chaudes`
3. **Footnote Relocation:** Footnotes and source citations were moved from the CSV file into this README to prevent data processing errors.

## Original Footnotes & Methodology
* **Temperature Departure:** The temperature departure is the difference between the average temperature for a given year and the average temperature for the reference period (1961 to 1990).
* **Ranking:** "1" indicates the warmest year on record since 1948. 2024 and 2010 are currently tied for the warmest year.
* **Coverage:** This indicator uses the Adjusted and Homogenized Canadian Climate Data (AHCCD) for temperature.
* **Citation:** Environment and Climate Change Canada (2025) Canadian Environmental Sustainability Indicators: Temperature change in Canada.

## Licence Reference
This folder's dataset context uses Government of Canada open data terms:
- Open Government Licence - Canada: https://open.canada.ca/en/open-government-licence-canada
