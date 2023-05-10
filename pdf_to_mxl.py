import os
import subprocess
import shutil

# Put your Audiveris executable path here. This is the default location for Windows installations.
audiveris_path = "C:\Program Files\Audiveris\\bin\Audiveris.bat"

pdf_path = "touhou.pdf"

output_dir = "output"
output_filename = "output.mxl"

os.makedirs(output_dir, exist_ok=True)

temp_dir = "temp"
os.makedirs(temp_dir, exist_ok=True)

subprocess.call([audiveris_path, "-batch", "-export", "-output", temp_dir, pdf_path])

output_midi_path = os.path.join(output_dir, output_filename)

for subdir, dirs, files in os.walk(temp_dir):
    for filename in files:
        if filename.endswith(".mxl"):
            mxl_path = os.path.join(subdir, filename)
            shutil.copy(mxl_path, output_midi_path)
            break

shutil.rmtree(temp_dir)