from PyPDF2 import PdfWriter, PdfFileMerger

merger = PdfWriter()

for pdf in ['data/pdf_file_1.pdf', 'data/pdf_file_2.pdf']:
    merger.append(pdf)

merger.write('data/merged-file.pdf')
merger.close()