import glob
import pandas as pd
from fpdf import FPDF
from pathlib import Path

files = glob.glob("invoices/*.xlsx")

for i in files:
    i_no, date = Path(i).stem.split("-")

    pdf = FPDF(orientation="p",unit="mm",format="a4")
    pdf.set_font('Times', style='B',size=20)

    pdf.add_page()
    pdf.cell(w=0, h=8,align='',txt=f"Invoice Number : {i_no}",ln=1)
    pdf.cell(w=0, h=8,txt=f"Date : {date}",ln=1)

    f = pd.read_excel(i, sheet_name="Sheet 1")

    c_name = list(f.columns)
    pdf.set_font('Times', style='B', size=13)
    pdf.cell(w=30, h=8, txt=c_name[0], border=1)
    pdf.cell(w=50, h=8, txt=c_name[1], border=1)
    pdf.cell(w=40, h=8, txt=c_name[2], border=1)
    pdf.cell(w=40, h=8, txt=c_name[3], border=1)
    pdf.cell(w=30, h=8, txt=c_name[4], border=1,ln=1)

    for index, row in f.iterrows():

        pdf.set_font('Times',"",12)
        pdf.set_text_color(80,80,80)

        pdf.cell(w=30,h=8,txt=str(row['product_id']),border=1)
        pdf.cell(w=50,h=8,txt=str(row['product_name']),border=1)
        pdf.cell(w=40,h=8,txt=str(row['amount_purchased']),border=1)
        pdf.cell(w=40,h=8,txt=str(row['price_per_unit']),border=1)
        pdf.cell(w=30,h=8,txt=str(row['total_price']),border=1,ln=1)










    pdf.output(f"{i_no}.pdf")


