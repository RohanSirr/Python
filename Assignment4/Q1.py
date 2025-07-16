try:

    with open("demo.txt", "r") as file:
        print("Reading file content:")
        line_number = 1
        # File ki har line ko iterate kar rahe hain.
        for line in file:
            # Har line ko format karke print kar rahe hain, '.strip()' se extra newline characters hat jayenge.
            print(f"Line {line_number}: {line.strip()}")
            line_number += 1 

except FileNotFoundError:
    print("Error: The file 'demo.txt' was not found.")