# Yuh skibidibop pop
import argparse

from pdf_to_mxl import pdf_to_mxl
from mxl_last_notes import mxl_last_notes

def main(args):
    pdf_to_mxl(args.input_file.name, args.output_dir)
    mxl_last_notes(args.output_dir, last_N=args.notes, file_pattern=args.regex)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A CLI to simplify inputs for the Python-imparied")
    
    parser.add_argument('input_file', type=argparse.FileType('r'), help='input PDF to read')
    parser.add_argument('--output_dir', '-o', type=str, default='output', help='output dir to save mxl files to')
    parser.add_argument('--notes', '-n', type=int, default=10, help='number of notes to extract from end of each page')
    parser.add_argument('--verbose', '-v', action='store_true', help='enable verbose logging')
    parser.add_argument('--regex', '-r', type=str, default=r"_page_(\d+)\.mxl$", help="R-string that matches pattern for output files")
    
    args = parser.parse_args()
    main(args)