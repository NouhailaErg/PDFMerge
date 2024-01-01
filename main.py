from PyPDF2 import PdfMerger
import os

# Get the path from the user
user_path = input("Enter the path of the directory containing PDF files: ")

# Validate the path
if not os.path.exists(user_path):
    print("Invalid path. Please provide a valid path.")
    exit()

# Change the working directory to the specified path
os.chdir(user_path)

# Create a PdfMerger object
merger = PdfMerger()

# Iterate over PDF files in the specified directory
for file in os.listdir(os.curdir):
    if file.endswith(".pdf"):
        merger.append(file)

# Write the merged PDF to a new file
output_file = input("Enter the name of the merged PDF file (e.g., combinedDoc.pdf): ")
merger.write(output_file)

# Close the PdfMerger object
merger.close()

print(f"Merged PDF saved as {output_file} in {user_path}")
