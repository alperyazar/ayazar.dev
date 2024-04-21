import os
import sys
import argparse

def find_md_files(directory):
    """Yield paths to all markdown files in the given directory and its subdirectories."""
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".md"):
                yield os.path.join(root, file)

def extract_giscus_values(file_path):
    """Extract giscus values from the specified markdown file."""
    with open(file_path, 'r') as file:
        return [line.strip().split(': ')[1] for line in file if line.strip().startswith('giscus:') and len(line.strip().split(': ')) == 2]

def main():
    parser = argparse.ArgumentParser(description="Search .md files for 'giscus: <ID>' pattern.")
    parser.add_argument("path", type=str, help="Directory path to search for .md files")
    args = parser.parse_args()

    all_giscus_values = {}
    unique_giscus_values = {}
    error_messages = []
    file_count = 0

    # Process each markdown file found in the directory
    for md_file in find_md_files(args.path):
        print(f"Checking file: {md_file}")
        file_count += 1
        values = extract_giscus_values(md_file)

        if len(values) > 1:
            error_messages.append(f"Error: More than one 'giscus: <ID>' value found in {md_file}")

        for value in values:
            if value in unique_giscus_values:
                # Append current file to list of files that already include this value
                unique_giscus_values[value].append(md_file)
            else:
                unique_giscus_values[value] = [md_file]

    # Check for duplicate values across different files
    for value, files in unique_giscus_values.items():
        if len(files) > 1:
            error_messages.append(f"Error: Duplicate 'giscus: <ID>' value '{value}' found across files: {', '.join(files)}")

    # Print all error messages, if any
    if error_messages:
        for message in error_messages:
            print(message, file=sys.stderr)

    # Print summary to stdout
    print(f"Total files checked: {file_count}")
    print(f"Total unique 'giscus: <ID>' matches found: {len(unique_giscus_values)}")

    if error_messages:
        return 1
    return 0

if __name__ == "__main__":
    sys.exit(main())
