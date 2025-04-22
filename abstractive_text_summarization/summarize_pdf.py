'''
This script can be used for abstractive text summarization from a given PDF 
using Azure AI Services. 

Requirements: 
pip install azure-ai-textanalytics==5.3.0
pip install PyMuPDF

'''

import argparse
import fitz
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

def authenticate_client(key, endpoint):
    """
    Authenticate the client using your key and endpoint.
    """
    ta_credential = AzureKeyCredential(key)
    text_analytics_client = TextAnalyticsClient(
            endpoint=endpoint, 
            credential=ta_credential)
    return text_analytics_client

def read_pdf_line_by_line(pdf_path):
    """
    To read the pdf file.
    """
    full_text = ""
    full_text_list = []

    pdf_document = fitz.open(pdf_path)
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        text = page.get_text("text")

        for line in text.split('\n'):
            try:
                line.encode('charmap')
                full_text += line + "\n"
            except UnicodeEncodeError:
                # Skip characters that cannot be encoded using 'charmap' codec
                continue

    full_text_list.append(full_text)
    return full_text_list

def sample_abstractive_summarization(client, pdf_path):
    """
    Function for summarizing text.
    """
    document = read_pdf_line_by_line(pdf_path)
    poller = client.begin_abstract_summary(document)

    document_results = poller.result()
    for result in document_results:
        if result.kind == "AbstractiveSummarization":
            print("Abstractive summary:")
            for summary in result.summaries:
                print(f"{summary.text}\n")
        elif result.is_error is True:
            print(f"Is an error with code {result.error.code} and message {result.error.message}")

def main():
    """
    Main function.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', type=str, help="Path to the pdf file.")
    parser.add_argument('--endpoint', type=str, help="Azure AI service endpoint.")
    parser.add_argument('--key', type=str, help="Key to access Azure AI service API.")

    args = parser.parse_args()
    key = args.key
    endpoint = args.endpoint
    pdf_path = args.path

    client = authenticate_client(key, endpoint)
    sample_abstractive_summarization(client, pdf_path)


if __name__ == "__main__":
    main()
