from fpdf import FPDF

def save_itinerary_to_pdf(itinerary, filename="itinerary.pdf"):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", style='', size=12)
    
    pdf.multi_cell(0, 10, itinerary)
    
    pdf.output(filename)
    return filename
