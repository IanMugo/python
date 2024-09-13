try:
    with open("my_file.txt", 'w') as file:
        file.write("My name is Ian.\n")
        file.write("This is a number: 1\n")
        file.write("First generated line .\n")
    print("File created and initial content written.")

# File Reading and Display: Reading the contents of the file
    with open("my_file.txt", 'r') as file:
        print("\nReading file contents:")
        content = file.read()
        print(content)

# File Appending: Appending additional content to the file
    with open("my_file.txt", 'a') as file:
        file.write("My name is Mugo.\n")
        file.write("This is a number: 2\n")
        file.write("Second generated line.\n")
    print("Additional content appended.")

# Re-reading the file to show updated content
    with open("my_file.txt", 'r') as file:
        print("\nUpdated file contents after appending:")
        content = file.read()
        print(content)

except FileNotFoundError as fnf_error:
    print(f"Error: {fnf_error}")
except PermissionError as perm_error:
    print(f"Error: {perm_error}")
finally:
    print("File handling operations complete.")
