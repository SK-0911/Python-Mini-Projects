import PyPDF2

new_pdf = open('2.6.pdf', 'rb')
reading_pdf = PyPDF2.PdfReader(new_pdf)

print("No. pages in PDF is: " + str(len(reading_pdf.pages)))

read_page = int(input("Enter the Page you want to extract text from: "))
first_page = reading_pdf.pages[read_page]

print("\n\n----- xxxx -----")
print(first_page.extract_text())
print("----- xxxx -----")

# Close PDF file
new_pdf.close()