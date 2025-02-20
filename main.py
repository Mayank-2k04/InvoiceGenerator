import glob
import pandas as pd
from fpdf import FPDF
from pathlib import Path

files = glob.glob("invoices/*.xlsx")

for i in files:
    i_no, date = Path(i).stem.split("-")

    f = pd.read_excel(i,sheet_name="Sheet 1")
    pdf = FPDF(orientation="p",unit="mm",format="a4")
    pdf.set_font('Times', style='B',size=16)

    pdf.add_page()
    pdf.cell(w=0, h=8,align='',txt=f"Invoice Number : {i_no}",ln=1)
    pdf.cell(w=0, h=8,txt=f"Date : {date}",ln=1)






    pdf.output(f"{i_no}.pdf")


