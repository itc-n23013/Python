import openpyxl
import sys

def insert_empty_rows(filename, n, m):
    try:
        wb = openpyxl.load_workbook(filename)
        sheet = wb.active

        sheet.insert_rows(n, amount=m)

        wb.save(filename)
        print(f"{filename} に {n}行目から{m}行の空行を挿入しました。")
    except FileNotFoundError:
        print(f"エラー: ファイル '{filename}' が見つかりませんでした。")
    except IndexError:
        print(f"エラー: シート '{sheet.title}' でインデックスが範囲外です。")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("実行: python blankRowInserter.py <N> <M> <ファイル名>")
    else:
        try:
            N = int(sys.argv[1])
            M = int(sys.argv[2])
            filename = sys.argv[3]
            insert_empty_rows(filename, N, M)
        except ValueError:
            print("エラー: N と M は整数でなければなりません。")

