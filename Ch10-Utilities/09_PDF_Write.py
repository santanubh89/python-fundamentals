import PyPDF2

f = open('data/story_book.pdf', 'rb')
pdf_reader = PyPDF2.PdfReader(f)
first_page = pdf_reader.pages[0]
print(type(first_page))
pdf_writer = PyPDF2.PdfWriter()
pdf_writer.add_page(first_page)
pdf_output = open('data/new_file.pdf', 'wb')
pdf_writer.write(pdf_output)