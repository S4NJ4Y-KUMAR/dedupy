import argparse
import sys
import time

def print_banner():
    banner = "\033[94m" + """
    ____                              
  (|   \        |                    
   |    | _   __|           _        
  _|    ||/  /  |  |   |  |/ \_|   | 
 (/\___/ |__/\_/|_/ \_/|_/|__/  \_/|/
                         /|       /| 
                         \|       \|
                    --Basic tool to remove duplicates
    """ + "\033[0m"  # Reset color
    print(banner)
    h = [
        "Options:",
        "  -list --input         Path to the input file",
        "  -o,   --output        Output file for processed results",
        "\n",
    ]
    print("\n".join(h))

def remove_duplicates(input_file, output_file):
    lines = set()
    with open(input_file, 'r') as f:
        l = f.read().splitlines()
        for line in l:
            removed_line = '/'.join(line.split('/')[:-1]) + '/'
            if removed_line not in lines:
                lines.add(removed_line)
    
    sys.stdout.write("\033[94m"+"\n\nRemoving Duplicate sub links"+"\033[0m")
    sys.stdout.flush()

    # Simulate loading animation
    for _ in range(5):
        sys.stdout.write("\033[94m"+'.'+"\033[0m")
        sys.stdout.flush()
        time.sleep(0.2)

    sys.stdout.write("\n\n")
    with open(output_file, 'w') as r:
        for processed_line in lines:
            r.write(processed_line + '\n')

    
    print("\033[97m"+"The output file is generated in the current directory.\nThank you for using this tool!"+"\033[0m")
    

def main():
    print_banner()
    parser = argparse.ArgumentParser(description='Basic tool to remove duplicates', epilog="Usage: tool.py -list input.txt -o output.txt")
    parser.add_argument('-list', required=True, help='Path to the input file')
    parser.add_argument('-o', '--output', required=True, help='Output file for processed results')

    args = parser.parse_args()

    print("Usage: tool.py -list input.txt -o output.txt")
    remove_duplicates(args.list, args.output)

if __name__ == "__main__":
    main()
