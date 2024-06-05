import os
import re

def search_files(directory, pattern):
    regex = re.compile(pattern)
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.txt'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    lines = f.readlines()
                    
                    for line_num, line in enumerate(lines, 1):
                        if regex.search(line):
                            print(f"File: {file_path}, Line {line_num}: {line.strip()}")

directory = input("ディレクトリのパスを入力してください: ")
pattern = input("検索する正規表現パターンを入力してください: ")
search_files(directory, pattern)

