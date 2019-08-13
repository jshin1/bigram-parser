import sys

def parse_file():
    f = open(sys.argv[1], "r")
    contents = f.read()
    print(contents)

if __name__ == "__main__":
    parse_file()
