import subprocess
import sys


def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

try:
	from PyPDF2 import PdfFileMerger
except ImportError as e:
	install("pypdf2")

from PyPDF2 import PdfFileMerger

merger = PdfFileMerger()

pdfs = sys.argv
pdfs.pop(0)

for pdf in pdfs:
    merger.append(pdf)

merger.write("merged_result.pdf")
merger.close()

print("Pdf files merged successfully!")