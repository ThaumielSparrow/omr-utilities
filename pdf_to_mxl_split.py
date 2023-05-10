import os
import subprocess
import shutil
import PyPDF2 as PyPDF

# Put your Audiveris executable path here. This is the default location for Windows installations.
audiveris_path = "C:\Program Files\Audiveris\\bin\Audiveris.bat"

pdf_path = "shadowofthegods.pdf"

output_dir = "output"
os.makedirs(output_dir, exist_ok=True)

temp_dir = "temp"
os.makedirs(temp_dir, exist_ok=True)

with open(pdf_path, "rb") as pdf_file:
    pdf_reader = PyPDF.PdfReader(pdf_file)
    num_pages = len(pdf_reader.pages)

    for page in range(num_pages):
        pdf_writer = PyPDF.PdfWriter()
        pdf_writer.add_page(pdf_reader.pages[page])
        single_page_pdf_path = os.path.join(temp_dir, f"page_{page + 1}.pdf")

        with open(single_page_pdf_path, "wb") as single_page_pdf_file:
            pdf_writer.write(single_page_pdf_file)

        subprocess.call([audiveris_path, "-batch", "-export", "-output", temp_dir, single_page_pdf_path])

        output_mxl_path = os.path.join(output_dir, f"output_page_{page + 1}.mxl")

        for subdir, dirs, files in os.walk(temp_dir):
            for filename in files:
                if filename.endswith(".mxl"):
                    mxl_path = os.path.join(subdir, filename)
                    shutil.copy(mxl_path, output_mxl_path)
                    break

        os.remove(single_page_pdf_path)
        for filename in files:
            if filename.endswith(".mxl"):
                os.remove(os.path.join(subdir, filename))

shutil.rmtree(temp_dir)