from markdown_it import MarkdownIt
from xhtml2pdf import pisa
from io import BytesIO
import os

md = MarkdownIt()
path = input("enter the path of your file: ").strip()
if not os.path.isfile(path):
    print("File not found")
    exit()
with open(path, "r", encoding="utf-8") as f:
    content = f.read()
html_content = md.render(content)
with open("output.pdf", "wb") as f:
    pisa.CreatePDF(html_content, dest=f)
print("PDF created successfully")


