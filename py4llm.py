import pymupdf4llm
import pathlib
md_text = pymupdf4llm.to_markdown("paper.pdf")

pathlib.Path("output.md").write_bytes(md_text.encode())
