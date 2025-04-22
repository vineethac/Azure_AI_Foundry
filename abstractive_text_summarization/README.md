# Overview
This script can be used for abstractive text summarization from a given PDF using Azure AI Services.

# Pre-requisites
```
pip install azure-ai-textanalytics==5.3.0
pip install PyMuPDF
```

# How to run
```
> python3 .\summarize_pdf.py --help
usage: summarize_pdf.py [-h] [--path PATH] [--endpoint ENDPOINT] [--key KEY]

options:
  -h, --help           show this help message and exit
  --path PATH          Path to the pdf file.
  --endpoint ENDPOINT  Azure AI service endpoint.
  --key KEY            Key to access Azure AI service API.

> python3 .\summarize_pdf.py --path "path_to_pdf" --endpoint "your_endpoint" --key "your_key"
```

