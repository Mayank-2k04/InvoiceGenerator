# Invoice PDF Generator

## Overview
This Python script automates the process of generating invoice PDFs from Excel files stored in the `invoices/` directory. It extracts relevant details from each file, formats them, and outputs a structured invoice PDF.

## Features
- Reads invoice data from Excel files (`.xlsx`).
- Extracts invoice number and date from the filename.
- Formats data into a structured table with product details.
- Computes and displays the total due amount.
- Adds a personalized signature with an image.
- Outputs invoices as PDF files named after the invoice number.

## Prerequisites
Ensure the following dependencies are installed:

```bash
pip install pandas fpdf
```

## Usage
1. Place the invoice Excel files in the `invoices/` directory.
2. Ensure each filename follows the format: `invoiceNumber-date.xlsx`.
3. Run the script:
   
   ```bash
   python main.py
   ```

4. Generated PDF invoices will be saved in the current directory.

## File Format
The input Excel file should contain the following columns:
- `product_id`
- `product_name`
- `amount_purchased`
- `price_per_unit`
- `total_price`

## Example Invoice Structure
Each invoice PDF includes:
- Invoice Number & Date
- Product details in tabular format
- Total due amount
- Signature with an image

## Author
Made by: **Mayank Kapoor**
