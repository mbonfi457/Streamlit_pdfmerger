import os
import PyPDF2
import streamlit as st

def merge_pdfs(pdf_files, output_filename):
    pdf_merger = PyPDF2.PdfMerger()

    for pdf_file in pdf_files:
        try:
            pdf_merger.append(pdf_file)
        except:
            st.warning(f"Invalid PDF file: {pdf_file.name} - Skipping.")

    # Automatically attach '.pdf' to the output file name if not already provided
    if not output_filename.endswith('.pdf'):
        output_filename += '.pdf'

    # Write the merged PDF to the output file
    with open(output_filename, 'wb') as output:
        pdf_merger.write(output)

    return output_filename

def main():
    st.title("PDF Merger with Streamlit")
    st.write("Upload your PDF files below and enter the desired output file name.")

    pdf_files = st.file_uploader("Upload PDF files", type=["pdf"], accept_multiple_files=True)

    if pdf_files:
        output_filename = st.text_input("Output File Name", value="output_combined.pdf")

        if st.button("Merge PDFs"):
            merged_file = merge_pdfs(pdf_files, output_filename)
            st.success(f"PDF files merged successfully!")
            st.download_button(label="Download Merged PDF", data=open(merged_file, 'rb').read(), file_name=merged_file)

if __name__ == "__main__":
    main()
