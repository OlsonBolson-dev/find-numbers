import re
import tkinter as tk
from tkinter import filedialog

# Create a Tkinter root window
root = tk.Tk()
root.withdraw()

# Open a file dialog box to select the input file
input_file = filedialog.askopenfilename(title="Select input file", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])

# Open the input file and read its contents
with open(input_file, 'r', errors='ignore') as file:
    text = file.read()

# Define the regular expression pattern and find matches
pattern = r'\[(\d+)\]'
matches = re.findall(pattern, text)

# Count the number of matches found
num_matches = len(matches)

# Print the number of matches to the terminal
print(f"Found {num_matches} matches in the input file.")

# Join the matches into a single string separated by commas
variable_names = ', '.join(matches)

# Open a file dialog box to select the output file
output_file = filedialog.asksaveasfilename(title="Select output file", filetypes=[("Text files", "*.txt"), ("All files", "*.*")], defaultextension=".txt")

# Write the variable names and number of matches to the selected output file
with open(output_file, 'w') as outfile:
    outfile.write(variable_names)

# Convert the matched strings to integers
numbers = [int(match) for match in matches]

# Sort the list of numbers in ascending order
numbers.sort()

# Open the file for appending
with open(output_file, 'w') as outfile:
    # Write the sorted list of numbers to the file
    outfile.write(','.join(map(str, numbers)))
