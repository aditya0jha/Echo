import PyPDF2




pdfs = ['1.pdf', '2.pdf']

merger = PdfMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("result.pdf")
merger.close()

