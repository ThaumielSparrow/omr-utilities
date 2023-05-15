import os
import re
import music21


# Default regular expression matches [ARBITRARYSTRING]_page_[INTEGER].mxl, if you are changing how these are saved you need to change the regex.

def mxl_last_notes(folder_path, save=True, last_N = 10, file_pattern=r"_page_(\d+)\.mxl$"):
    file_list = sorted(os.listdir(folder_path), key=lambda x: int(re.search(file_pattern, x).group(1)))
    for filename in file_list:
        if filename.endswith(".mxl"):
            file_path = os.path.join(folder_path, filename)
            score = music21.converter.parse(file_path)
            
            last_elements = score.flat.getElementsByClass(['Note', 'Chord'])[-last_N:]
            last_notes = []
            for element in last_elements:
                if isinstance(element, music21.note.Note):
                    last_notes.append(str(element.name))
                elif isinstance(element, music21.chord.Chord):
                    chord_notes = [str(n.name) for n in element.notes]
                    last_notes.append(chord_notes)
            
            print(filename)
            output_list = [f"[{', '.join(element)}]" if isinstance(element, list) else element for element in last_notes]
            print(' '.join(output_list))
            print("\n")

            if save:
                with open(f'{folder_path}/last_notes.txt', 'a') as f:
                    f.write(f"{filename}\n{' '.join(output_list)}\n")

if __name__ == "__main__":
    mxl_last_notes("output/")