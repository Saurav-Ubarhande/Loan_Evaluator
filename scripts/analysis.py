def calculate_monthly_totals(df):

    if "Date" not in df.columns:
        raise KeyError("The DataFrame does not contain a 'Date' column.")

    df["Month"] = df["Date"].dt.to_period("M")
    monthly_totals = df.groupby("Month").agg({"Debit": "sum", "Credit": "sum"})
    return monthly_totals

def detect_recurring_transactions(df):
    recurring = df.groupby('Description').agg({'Debit': 'sum', 'Credit': 'sum', 'Description': 'count'})
    recurring = recurring.rename(columns={'Description': 'Frequency'})
    recurring = recurring[recurring['Frequency'] > 1].sort_values(by='Frequency', ascending=False)
    return recurring

def detect_loans(df):
    loan_keywords = ['loan', 'mortgage', 'credit', 'debt']
    df['Is_Loan'] = df['Description'].str.contains('|'.join(loan_keywords), case=False, na=False)
    return df[df['Is_Loan']]

def loan_recommendation(df):
    total_credit = df["Credit"].sum()
    total_debit = df["Debit"].sum()
    net_change = total_credit - total_debit


    has_negative_balance = (df["Balance"] < 0).any()

    if net_change > 0 and not has_negative_balance:
        return f"Eligible for a loan. Total Credit: {total_credit:.2f}, Total Debit: {total_debit:.2f}, Net Change: {net_change:.2f}."
    else:
        return f"Not eligible for a loan. Total Credit: {total_credit:.2f}, Total Debit: {total_debit:.2f}, Net Change: {net_change:.2f}."
