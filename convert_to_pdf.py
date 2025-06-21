import pdfkit
import os

# Convert markdown report to PDF
try:
    pdfkit.from_file('EDA_Report_Cars_Analysis.md', 'EDA_Report_Cars_Analysis.pdf')
    print("Markdown report converted to PDF successfully!")
except Exception as e:
    print(f"Error converting markdown to PDF: {str(e)}")

# Convert notebook to PDF
try:
    # First convert to HTML
    os.system('jupyter nbconvert --to html EDA_Assignment_Day_14_Completed.ipynb')
    # Then convert HTML to PDF
    os.system('jupyter nbconvert --to pdf EDA_Assignment_Day_14_Completed.ipynb')
    print("Notebook converted to PDF successfully!")
except Exception as e:
    print(f"Error converting notebook to PDF: {str(e)}")
