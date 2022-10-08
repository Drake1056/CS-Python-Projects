def main():

    X = int(input("What's X? "))
    if is_even(X):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    return True if n % 2 == 0 else False


main()

