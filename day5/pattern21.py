def palindromic(n):
    for i in range(n):
        spaces = n-i-1
        print(" "*spaces, end="")

        for j in range(1, i+2):
            print(j, end="")

        for j in range(i, 0, -1):
            print(j, end="")

        print()

def main():
    n = int(input())
    palindromic(n)

if __name__ == "__main__":
    main()