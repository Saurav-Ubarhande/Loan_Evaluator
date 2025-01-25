import pdfplumber
import pandas as pd

def extract_data_from_pdf(pdf_path_or_file):
    data = []
    with pdfplumber.open(pdf_path_or_file) as pdf:
        for page in pdf.pages:
            table = page.extract_table()
            if table:
                for row in table:
                    if any(row):
                        data.append(row)

    if data:
        max_columns = max(len(row) for row in data)
        normalized_data = [row + [None] * (max_columns - len(row)) for row in data] 
        return pd.DataFrame(normalized_data)
    else:
        return pd.DataFrame() 
