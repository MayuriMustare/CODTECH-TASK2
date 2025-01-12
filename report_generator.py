import pandas as pd
from fpdf import FPDF

# Step 1: Read Data from a File
def read_data(file_path):
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print(f"Error reading file: {e}")
        return None

# Step 2: Analyze Data
def analyze_data(data):
    analysis = {
        "Total Rows": len(data),
        "Columns": list(data.columns),
        "Missing Values": data.isnull().sum().to_dict(),
        "Summary Statistics": data.describe(include='all').to_dict()
    }
    return analysis

# Step 3: Generate PDF Report
class PDFReport(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 16)
        self.cell(0, 10, 'Automated Data Analysis Report', 0, 1, 'C')
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

    def add_section(self, title, content):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(5)
        self.set_font('Arial', '', 10)
        for line in content:
            self.multi_cell(0, 10, line)
        self.ln(10)

def generate_pdf_report(analysis, output_file):
    pdf = PDFReport()
    pdf.add_page()

    # Add summary section
    pdf.add_section("Data Summary", [
        f"Total Rows: {analysis['Total Rows']}",
        f"Columns: {', '.join(analysis['Columns'])}",
        "Missing Values:",
        "\n".join([f"  - {col}: {count}" for col, count in analysis['Missing Values'].items()]),
    ])

    # Add statistics section
    pdf.add_section("Summary Statistics", [
        f"{col}: {stats}" for col, stats in analysis['Summary Statistics'].items()
    ])

    pdf.output(output_file)
    print(f"PDF report generated: {output_file}")

# Main Program
if __name__ == "__main__":
    file_path = "data.csv"  # Replace with your CSV file path
    output_file = "report.pdf"

    print("Reading data...")
    data = read_data(file_path)

    if data is not None:
        print("Analyzing data...")
        analysis = analyze_data(data)

        print("Generating PDF report...")
        generate_pdf_report(analysis, output_file)
