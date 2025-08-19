def count_lines_in_file():
    file_path = input("Enter the path to the text file: ")
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            return len(lines)
    except FileNotFoundError:
        print("File not found.")
        return None

# Example usage:
if __name__ == "__main__":
    num_lines = count_lines_in_file()
    if num_lines is not None:
        print(f"Number of lines: {num_lines}")