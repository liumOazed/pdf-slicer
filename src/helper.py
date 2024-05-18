import PyPDF2

# input_pdf = "data\Gary Vaynerchuk - Jab, Jab, Jab, Right Hook_ How to Tell Your Story in a Noisy Social World (2013, HarperBusiness) - libgen.li.pdf"
def extract_pages(input_pdf, start_round, end_round, output_pdf):
    # Open the pdf file
    with open(input_pdf, 'rb') as file:
        reader = PyPDF2.PdfFileReader(file)

        # Create a pdf writer object
        writer = PyPDF2.PdfFileWriter()

        # Add pages from start_round to end_round to the writer
        for i in range(start_round-1, end_round+1):
            page = reader.getPage(i)
            writer.addPage(page)

        # Write the pages to a new pdf file
        with open(output_pdf, 'wb') as output_file:
            writer.write(output_file)

