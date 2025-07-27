import PyPDF2

f = open('data/story_book.pdf', 'rb')
pdf_reader = PyPDF2.PdfReader(f)
print(f'Number of pages = {len(pdf_reader.pages)}')
page_0 = pdf_reader.pages[0]
page_0_text = page_0.extract_text()
print(f'Page 0 Text: \n{page_0_text}')
f.close()