initial_input = input("Enter text to write to the file: ")
with open("output.txt", "w") as file:
    file.write(initial_input + "\n")
print("Data successfulluy written to the output.txt\n")


additional_input = input("Enter additional text to append: ")
with open("output.txt", "a") as file:
    file.write(additional_input + "\n")
print("Data successfully append. ")

print("\nFinal content of the output.txt: ")
with open("output.txt", "r") as file:
    print(file.read())