from fpdf import FPDF

pdf = FPDF(orientation="portrait", format="A4")
pdf.add_page()
pdf.set_margin(0)
pdf.set_font("Helvetica")
pdf.cell(text="CS50 Shirtificate")
name = input("Name: ")
pdf.image("shirtificate.png", h= pdf.eph, w=pdf.epw, alt_text= f"{name} took CS50")
pdf.output("shirtificate.pdf")
