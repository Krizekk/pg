import sys

def convert_ammount(ammount, currency):
    return 0.0

if __name__ == "__main__":

    if len(sys.argv) < 3:
        print(f"Usage: {sys.argv[0]} ammount currency")
        sys.exit()

    ammount = int(sys.argv[1])
    currency = sys.argv[2]