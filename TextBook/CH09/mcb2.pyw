import shelve
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python clipboard.py [save|load|delete|deleteall|list] <keyword> [content]")
        return

    command = sys.argv[1]
    keyword = sys.argv[2] if len(sys.argv) > 2 else None

    with shelve.open('clipboard_shelf') as shelf:
        if command == 'save' and keyword and len(sys.argv) == 4:
            shelf[keyword] = sys.argv[3]
            print(f"Saved '{sys.argv[3]}' to clipboard with keyword '{keyword}'.")
        elif command == 'load' and keyword:
            print(shelf.get(keyword, "Keyword not found"))
        elif command == 'delete' and keyword:
            if keyword in shelf:
                del shelf[keyword]
                print(f"Deleted '{keyword}' from clipboard.")
            else:
                print(f"Keyword '{keyword}' not found in clipboard.")
        elif command == 'deleteall':
            shelf.clear()
            print("All keywords have been deleted from the clipboard.")
        elif command == 'list':
            print("Keywords in clipboard:", list(shelf.keys()))
        else:
            print("Unknown command or missing arguments. Usage: python clipboard.py [save|load|delete|deleteall|list] <keyword> [content]")

main()

