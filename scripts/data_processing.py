import pandas as pd

def preprocess_data(df):
    df = df.dropna(how="all")

    column_mapping = {
        0: "Transaction Date",
        1: "Value Date",
        2: "Particulars",
        3: "Cheque No.",
        4: "Debit",
        5: "Credit",
        6: "Balance"
    }
    df = df.rename(columns=column_mapping)

    required_columns = ["Transaction Date", "Particulars", "Debit", "Credit", "Balance"]
    df = df[[col for col in required_columns if col in df.columns]]

    df = df.rename(columns={"Transaction Date": "Date"})

    df["Debit"] = df["Debit"].str.replace(",", "").astype(str).str.strip()
    df["Credit"] = df["Credit"].str.replace(",", "").astype(str).str.strip()
    df["Balance"] = df["Balance"].str.replace(",", "").astype(str).str.strip()

    df["Debit"] = pd.to_numeric(df["Debit"], errors="coerce").fillna(0)
    df["Credit"] = pd.to_numeric(df["Credit"], errors="coerce").fillna(0)
    df["Balance"] = pd.to_numeric(df["Balance"], errors="coerce")

    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

    df = df.drop_duplicates()

    invalid_dates = df["Date"].isnull().sum()
    if invalid_dates > 0:
        print(f"Dropping {invalid_dates} rows with invalid dates.")
    df = df.dropna(subset=["Date"])

    return df
