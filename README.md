# BMW_Messtechnik_Task

# CSV Data Processing Project

## Project Overview

This repository contains a Python project focused on processing and analyzing CSV data originally exported from an Excel file. The primary objective is to identify and correct common data errors and inconsistencies, ensuring a robust dataset for further analysis.

## Technical Requirements

- **Python 3.8+**: Ensure Python 3.8 or higher is installed to avoid compatibility issues.
- **Pandas Library**: Used for data manipulation and cleaning.
- **NumPy Library**: Utilized for various numerical operations.

To install all dependencies, run the following command:

# Errors and Solutions

Error: Expected commas but found semicolons in the CSV file.

Solution: Adjusted the delimiter when reading the file using sep=';'.

Error: Empty cells and cells marked with "X".

Solution: Replaced 'X' with NaN and filled empty cells with the previous value using df.replace('X', np.nan, inplace=True) and df.ffill(inplace=True).

Error: Inconsistencies due to conversion from XLSX to CSV.

Solution: Applied ffill() to restore correct values in incomplete cells.

Error: Unintended value carry-over by ffill().

Solution: Limited the application of ffill() to the ['ID'] column.

Error: Duplicate last names propagated by ffill().

Solution: Applied ffill() to the ['Last Name'] column with a limit (limit=1).

# Extension Opportunities

Tests and Validation:
Implement automated or manual tests to verify data at critical points, ensuring integrity and accuracy of processing.

Exception Handling:
Implement Try-Exception blocks to handle unexpected or erroneous input values efficiently.

Processing Performance:
Explore alternatives to ffill() that may optimize resource utilization, especially with large datasets.
Data Cleaning Beyond the Provided Excel Table:

Consider additional data cleaning steps such as removing duplicates to enhance data quality for subsequent uses.
Contribution
Contributions to this project are welcome! Please ensure you follow the coding standards and submit pull requests for any enhancements.

```bash
pip install pandas numpy

License
This project is licensed under the MIT License - see the LICENSE.md file for details.
