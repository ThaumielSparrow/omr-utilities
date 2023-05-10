import os
import re
import music21

folder_path = "output"
save_to_file = False
last_N = 10

# This regular expression matches [ARBITRARYSTRING]_page_[INTEGER].mxl, if you are changing how these are saved you need to change the regex.
page_number_pattern = r"_page_(\d+)\.mxl$"

file_list = sorted(os.listdir(folder_path), key=lambda x: int(re.search(page_number_pattern, x).group(1)))
for filename in file_list:
    if filename.endswith(".mxl"):
        file_path = os.path.join(folder_path, filename)
        score = music21.converter.parse(file_path)
        
        last_elements = score.flat.getElementsByClass(['Note', 'Chord'])[-last_N:]
        last_notes = [str(n) for n in last_elements]
        
        print(filename)
        print(' '.join(last_notes))
        print("\n")

        if save_to_file:
            with open('last_notes.txt', 'a') as f:
                f.write(f"{filename}\n{' '.join(last_notes)}\n")
            