# Appendix: Importing from a Google Sheet

Importing data from a Google Sheet is similar to importing an online CSV file. The main difference is that the Google Sheets URL must be changed so that the selected worksheet is delivered as CSV data.

## CSV versus Google Sheets

For a CSV file, the data is already in CSV format and the file URL can be used directly.

For a Google Sheet, change the end of the sharing URL:

```text
/edit#gid=0
```

to:

```text
/export?format=csv
```

The complete Google Sheets URL follows this pattern:

```text
https://docs.google.com/spreadsheets/d/SHEET_ID/export?format=csv
```

`SHEET_ID` identifies the spreadsheet. This exports the default first worksheet tab. Only add `&gid=TAB_ID` when importing a different tab. The `TAB_ID` is the number shown after `gid=` in the Google Sheets URL.

The important change is `format=csv`. It tells Google Sheets to send the worksheet as CSV data. Once the URL has been changed, the data can be loaded with the same `pd.read_csv(data_url)` process used for an online CSV file.

## Important Conditions

The worksheet’s viewing permission must be public so the notebook can retrieve the CSV export. Do not publish private or identifying student information.

For the smoothest beginner workflow, place the column names in the first row of the worksheet. After importing, check that the expected column names and rows appear before beginning analysis.

## Workflow Summary

**Google Sheet → change URL to include `format=csv` → import as CSV → inspect the data**
