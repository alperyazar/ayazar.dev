import os
import sys
import re

def find_markdown_files(root_dir):
    """
    Recursively search for markdown files (.md) in the specified directory.
    """
    markdown_files = []
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith(".md"):
                markdown_files.append(os.path.join(root, file))
    return markdown_files

def modify_markdown(file_path, identifier):
    """
    Modify the markdown file by updating the front matter or adding a new one,
    and removing the Disqus block.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.readlines()

    front_matter_exists = False
    in_front_matter = False
    start_index = -1
    end_index = -1
    new_content = []

    # Check for existing front matter
    for index, line in enumerate(content):
        if line.strip() == '---':
            if not front_matter_exists:
                front_matter_exists = True
                in_front_matter = True
                start_index = index
            elif in_front_matter:
                end_index = index
                break

    # Modify or create front matter
    if front_matter_exists:
        print(f"Appending to existing front matter in {file_path}")
        content.insert(end_index, f'giscus: {identifier}\n')
    else:
        print(f"Creating new front matter in {file_path}")
        new_front_matter = ['---\n', f'giscus: {identifier}\n', '---\n']
        new_content = new_front_matter + content
        content = new_content

    # Remove the Disqus pattern and one additional line
    content = re.sub(r'^\`\`\`\{disqus\}\n:disqus_identifier: .*\n\`\`\`$\n?', '', ''.join(content), flags=re.MULTILINE)


    # Write the changes back to the file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(''.join(content))

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <path_to_directory>")
        sys.exit(1)

    root_dir = sys.argv[1]
    markdown_files = find_markdown_files(root_dir)
    disqus_pattern = r"^\`\`\`\{disqus\}\n:disqus_identifier: ([^\n]+)\n\`\`\`$"

    for file_path in markdown_files:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            matches = re.findall(disqus_pattern, content, re.MULTILINE)
            if matches:
                for identifier in matches:
                    print(f"Found Disqus identifier '{identifier}' in {file_path}. Modifying file...")
                    modify_markdown(file_path, identifier)

if __name__ == "__main__":
    main()
