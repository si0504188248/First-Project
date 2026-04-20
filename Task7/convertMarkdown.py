
from markdown_it import MarkdownIt
from xhtml2pdf import pisa


def open_file(file,mode):
    try:
        with open(file, mode,encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        print(f"Reading error occurred: {e}")
        return None

def md_to_pdf(content):
    md = MarkdownIt()
    html_content = md.render(content)
    try:
        with open("output.pdf", "wb") as f:
            status = pisa.CreatePDF(html_content, dest=f, encoding="utf-8")
            if status.err == 0:
                print("PDF created successfully")
            else:
                print(f"PDF creation failed with error code: {status.err}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == '__main__':
    while True:
        path = input("enter path of your file: ").strip()
        file_content = open_file(path, "r")
        if file_content is not None:
            break
        print("invalid path, please try again.\n")
    md_to_pdf(file_content)












