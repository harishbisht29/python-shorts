import PyPDF2 as pdf

pdf_object = open('sample.pdf', 'rb')
pdf_reader = pdf.PdfFileReader(pdf_object)
  
total_pages= pdf_reader.numPages
  
for p in range(total_pages):
	# creating a page object
	page_obj = pdf_reader.getPage(p)

	print("Displaying text of page: ",p+1)
	# extracting text from page
	print(page_obj.extractText())

# closing the pdf file object
pdf_object.close()
