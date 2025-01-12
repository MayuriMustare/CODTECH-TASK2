# CODTECH-TASK2

Name: MAYURI MUSTARE

Company: CODTECH IT SOLUTION

ID: CT08EYS

Domain: Python Programming Intern

Duration: December 2024 to January 2025

Mentor: SRAVANI GOUNI
# Overview of the Project:
# Project: AUTOMATED REPORT GENERATION
# A] Objective:
To automate the process of reading, analyzing, and summarizing data from a CSV file and generating a formatted PDF report that includes data statistics, missing value counts, and column details.

# B] Key Activities:
1. Reading Data: Load data from a CSV file using pandas, Handle errors such as missing files or incorrect formats gracefully.
2. Data Analysis: Compute the total number of rows and columns in the dataset, Identify columns with missing values and calculate their counts, Generate summary statistics (e.g., mean, median, min, max, etc.) for numerical and categorical columns.
3. PDF Report Generation: Use FPDF to create a well-structured PDF report, Include: A header and footer for the report, Sections for data summary and detailed statistics, Proper formatting for readability, including line breaks and indentation.
4. Error Handling: Ensure robust error handling for file reading and data processing to prevent runtime crashes.
5. User Interaction: Allow users to specify the input CSV file and output PDF file paths.

# C] Technologies Used:
1. Programming Language: Python-Chosen for its rich ecosystem of libraries for data analysis and report generation.
2. Libraries: pandas-For efficient data reading, cleaning, and analysis, Handles large datasets and provides functions like isnull(), describe(), and column operations. FPDF-For creating PDF reports with a customizable layout, including headers, footers, and formatted content.
3. File Formats: CSV (Comma-Separated Values)-Used as the input data file format, PDF (Portable Document Format)-Generated as the output report format for easy sharing and printing.
4. Data Analysis Techniques: Handling missing values and providing a detailed count, Generating descriptive statistics for both numerical and categorical data.
5. Output Customization: Headers and Footers-Add consistent branding or context to the report, Multi-line Content-Use multi_cell to ensure proper text wrapping and formatting in the PDF.


