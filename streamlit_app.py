import streamlit as st
from scripts.data_extraction import extract_data_from_pdf
from scripts.data_processing import preprocess_data
from scripts.analysis import calculate_monthly_totals, loan_recommendation

st.title("Saurav's Loan Evaluator")

uploaded_file = st.file_uploader("Upload a Bank Statement (PDF)", type=["pdf"])

if uploaded_file:
    st.info("Processing the uploaded file...")

    # Extract data
    raw_data = extract_data_from_pdf(uploaded_file)
    if raw_data.empty:
        st.error("No data could be extracted from the uploaded file. Please upload a valid bank statement.")
    else:
        st.write("### Raw Extracted Data", raw_data)

        # Preprocess data
        processed_data = preprocess_data(raw_data)
        st.success("Data successfully processed!")
        st.write("### Cleaned Data", processed_data)

        # Perform analysis
        monthly_totals = calculate_monthly_totals(processed_data)
        recommendation = loan_recommendation(processed_data)

        # Display results
        st.subheader("Monthly Totals")
        if not monthly_totals.empty:
            st.bar_chart(monthly_totals)
            st.write(monthly_totals)
        else:
            st.warning("No valid data for monthly totals.")

        # Loan recommendation
        st.subheader("Loan Recommendation")
        st.write(recommendation)
