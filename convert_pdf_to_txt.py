from PyPDF2 import PdfReader

# paths to the PDF files
pdf_path = "harrypotter.pdf"
txt_path = "harrypotter.txt"

#  Read the PDF file
reader = PdfReader(pdf_path)

# Extract text from each page and write to a text file

with open(txt_path, "w", encoding="utf-8") as txt_file:
    for page_num ,page in enumerate(reader.pages , start=1):
        text = page.extract_text()
        if text:
            txt_file.write(text + "\n")
            print(f"✅ Processed page {page_num}")

print(f"\n🎉 Done! Text saved at: {txt_path}")
        




