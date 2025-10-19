import pymupdf

doc = pymupdf.open("paper.pdf")

with open("out.txt","wb") as out:
    for page in doc:
        tp = page.get_textpage_ocr()
        text = page.get_text(textpage=tp).encode("utf8")
        out.write(text)
        out.write(bytes((12,)))
    out.close()

