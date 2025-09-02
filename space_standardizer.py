#!/usr/bin/env python3
import re
import sys
import os

def standardize_spaces(file_path):
    """Replace all Unicode space characters with standard space (U+0020)"""
    
    # Read the file content
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Define regex pattern for all Unicode space characters
    # This includes regular space, non-breaking space, en space, em space, 
    # thin space, hair space, zero-width space, and others
    space_pattern = r'[\u0020\u00A0\u2000-\u200A\u202F\u205F\u3000\uFEFF]'
    
    # Replace all space characters with a standard space
    standardized_content = re.sub(space_pattern, ' ', content)
    
    # Write the standardized content back to the file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(standardized_content)
    
    print(f"Standardized spaces in: {file_path}")

def process_directory(directory_path):
    """Process all files in a directory"""
    for root, _, files in os.walk(directory_path):
        for file_name in files:
            if file_name.endswith(('.md', '.txt')):
                file_path = os.path.join(root, file_name)
                standardize_spaces(file_path)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        path = sys.argv[1]
        if os.path.isfile(path):
            standardize_spaces(path)
        elif os.path.isdir(path):
            process_directory(path)
        else:
            print(f"Error: {path} is not a valid file or directory")
    else:
        print("Usage: python space_standardizer.py <file_or_directory_path>")
