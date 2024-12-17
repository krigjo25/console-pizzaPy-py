#   Importing Python responsories
import sys, csv

from tabulate import tabulate

def main():

    """
        #   Description :   
                Implements a command-line program to read a csv file
        #   O(1000) : Log n = 0.200s
    """

    try:
        
        #   Ensure the file is a CSV
        for i in range(1, len(sys.argv)):
            if not sys.argv[i].endswith('csv') and len(sys.argv) == 2:
                raise Exception("Please make sure the file is a CSV")

    except Exception as e:
        sys.exit(e)
    
    print(CSVReader(sys.argv[1]))


def CSVReader(arg):

    #   Open and print the file
    with open(f"{arg}", 'r') as f:
        return tabulate([i for i in csv.DictReader(f)], headers ='keys', tablefmt = 'grid')
        
if __name__ == '__main__':
    main()