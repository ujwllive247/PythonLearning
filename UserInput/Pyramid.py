def print_pyramid(rows):
    """
    This function prints a pyramid pattern with the given number of rows.

    :param rows: The number of rows for the pyramid
    """
    for i in range(rows):
        # Print leading spaces
        for j in range(rows - i - 1):
            print(" ", end="")

        # Print stars
        for k in range(2 * i + 1):
            print("*", end="")

        # Move to the next line after printing each row
        print()


# Example usage
num_rows = int(input("Enter the number of rows for the pyramid: "))
print_pyramid(num_rows)
