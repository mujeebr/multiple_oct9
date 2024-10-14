import streamlit as st
import openai
from fpdf import FPDF

# Set up OpenAI API key
openai.api_key = "your_openai_api_key_here"

# Function to generate a report using GPT-4
def generate_report(company_name, month, revenue, expenses, summary):
    prompt = f"""
    You are an expert financial report generator. Create a monthly report for the following company.
    
    Company Name: {company_name}
    Month: {month}
    Revenue: ${revenue}
    Expenses: ${expenses}
    
    Write a detailed summary based on the given information:
    {summary}
    """
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response['choices'][0]['message']['content']

# Function to save report as PDF
def save_report_as_pdf(company_name, month, generated_report):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    for line in generated_report.split('\n'):
        pdf.cell(200, 10, txt=line, ln=True, align='L')
    pdf_filename = f"{company_name}_report_{month}.pdf"
    pdf.output(pdf_filename)
    return pdf_filename

# Streamlit app interface
st.title("Financial Report Generator")

# Input form
company_name = st.text_input("Company Name")
month = st.text_input("Month")
revenue = st.number_input("Revenue", min_value=0)
expenses = st.number_input("Expenses", min_value=0)
summary = st.text_area("Summary")

# Button to generate report
if st.button("Generate Report"):
    if company_name and month and revenue and expenses and summary:
        # Generate report
        report = generate_report(company_name, month, revenue, expenses, summary)
        
        # Display report
        st.subheader("Generated Report")
        st.write(report)
        
        # Save report as PDF
        pdf_filename = save_report_as_pdf(company_name, month, report)
        st.success(f"Report saved as {pdf_filename}")
        st.download_button(label="Download PDF", data=open(pdf_filename, "rb"), file_name=pdf_filename)
    else:
        st.error("Please fill in all fields.")

