import os
import sys
import re

def find_md_files(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.md'):
                yield os.path.join(root, file)

def search_and_extract_uuids(file_path, pattern, uuid_pattern):
    uuids = []
    with open(file_path, 'r') as file:
        for line in file:
            if pattern in line:
                match = re.search(uuid_pattern, line)
                if match:
                    uuids.append(match.group(1))
    return uuids

def main():
    if len(sys.argv) != 2:
        print("Usage: python app.py <path>")
        sys.exit(1)

    path = sys.argv[1]
    pattern = ':disqus_identifier:'
    uuid_pattern = r':disqus_identifier:\s*([0-9a-fA-F-]{36})'
    all_uuids = {}
    collisions = []
    total_files = 0
    files_matched_pattern = 0

    for md_file in find_md_files(path):
        total_files += 1
        uuids = search_and_extract_uuids(md_file, pattern, uuid_pattern)
        if uuids:
            files_matched_pattern += 1
            for uuid in uuids:
                print(f"{md_file}: {uuid}")
                if uuid in all_uuids and all_uuids[uuid] != md_file:
                    collisions.append((uuid, md_file, all_uuids[uuid]))
                else:
                    all_uuids[uuid] = md_file

    collision_count = len(set(file for _, file1, file2 in collisions for file in (file1, file2)))

    if collisions:
        print("\nCollisions Detected:")
        for uuid, file1, file2 in collisions:
            print(f"Collision: UUID {uuid} found in both {file1} and {file2}")

    print(f"\nTotal .md files opened: {total_files}")
    print(f"Total .md files matching pattern: {files_matched_pattern}")
    print(f"Total .md files involved in collisions: {collision_count}")

    if collisions:
        sys.exit(1)
    else:
        print("No UUID collisions found.")
        sys.exit(0)

if __name__ == "__main__":
    main()
