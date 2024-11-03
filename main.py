from fpdf import FPDF
import os
import pandas as pd


pdf = FPDF(orientation="P", unit="mm",format="A4")
pdf.set_auto_page_break(auto=False,margin=0)

filepath = r"D:\Python\PDF TEMPLETE GENERATION\topics.csv"

if os.path.exists(filepath):
    if os.access(filepath, os.R_OK):
        # The directory exists and you have read permission, proceed to read the CSV file
        df = pd.read_csv(filepath)
        

for index,row in df.iterrows():

    pdf.add_page()
    pdf.set_font(family="Times",style="B",size=24)
    pdf.set_text_color(100,100,100)
    pdf.cell(w=0,txt=row['Topic'],align='L',h=12,ln=1,border=0)
    for X in range(20,298,10):
        pdf.line(10,X,200,X)
    
    pdf.ln(265)
    pdf.set_font(family="Times",style="I",size=8)
    pdf.set_text_color(180,180,180)
    pdf.cell(w = 0,txt=row["Topic"],h=8,align="R",border=0)
    
    for i in range(row["Pages"]-1):
        pdf.add_page()
        pdf.ln(277)
        pdf.set_font(family="Times",style="I",size=8)
        pdf.set_text_color(180,180,180)
        pdf.cell(w = 0,txt=row["Topic"],h=8,align="R",border=0)
        
        for X in range(20,298,10):
            pdf.line(10,X,200,X)
        

    
    
pdf.output("output.pdf")


        
