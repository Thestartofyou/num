def main():
    # Prompt the user to enter a number
    num = float(input("Enter a number: "))

    # Check if the number is positive, negative, or zero
    if num > 0:
        print("The number is positive.")
    elif num < 0:
        print("The number is negative.")
    else:
        print("The number is zero.")
    
    # Check if the number is even or odd
    if num % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")

if __name__ == "__main__":
    main()

