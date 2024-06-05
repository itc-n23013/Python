import re

input_filename = 'input.txt'
output_filename = 'output.txt'

with open(input_filename, 'r') as file:
    text = file.read()

keywords = ['形容詞', '名詞', '副詞', '動詞']

for keyword in keywords:
    matches = re.findall(rf'\b{keyword}\b', text)
    for match in matches:
        replacement = input(f'Enter a {keyword.lower()}: ')
        text = text.replace(match, replacement, 1)

print("\nModified Text:\n")
print(text)

with open(output_filename, 'w') as file:
    file.write(text)

print(f'\nModified text has been saved to {output_filename}')

