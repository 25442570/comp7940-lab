
# Write a function that prints all factors of the given parameter x
def print_factor(x):
        print(f"Factors of {x}:")
        for i in range(1, x):
            if x % i == 0:
                print(i, end=' ')


def main():
    x = 52633
    print_factor(x)

if __name__ == '__main__':
    main()