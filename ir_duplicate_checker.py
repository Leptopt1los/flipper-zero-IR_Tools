import argparse
import os
import sys
from IR_Tools import IR_Signal, parse_ir_file

def main():
    parser = argparse.ArgumentParser(description='Compare IR signals from two files')
    parser.add_argument('file1', type=str, help='Path to the first IR file')
    parser.add_argument('file2', type=str, help='Path to the second IR file')
    args = parser.parse_args()

    if not os.path.isfile(args.file1):
        print(f"Error: File '{args.file1}' does not exist.")
        return
    if not os.path.isfile(args.file2):
        print(f"Error: File '{args.file2}' does not exist.")
        return

    signals_1 = parse_ir_file(args.file1)
    signals_2 = parse_ir_file(args.file2)

    for signal_1 in signals_1:
        for signal_2 in signals_2:
            if signal_1.compare_data(signal_2.get_data()):
                print(f"{'='*50}\nPOTENTIAL MATCH FOUND:\nIN {args.file1} SIGNAL\n\n{str(signal_1)}\nSEEMS LIKE\n\n{str(signal_2)}\nIN {args.file2}\n{'='*50}\n\n{'*'*80}\n")

if __name__ == "__main__":
    main()


