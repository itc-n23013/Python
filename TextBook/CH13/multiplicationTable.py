import sys
from openpyxl import Workbook

def create_multiplication_table(n):
    wb = Workbook()
    ws = wb.active
    ws.title = f"{n}x{n} Multiplication Table"

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            ws.cell(row=i, column=j, value=i * j)

    wb.save(f"multiplication_table_{n}x{n}.xlsx")
    print(f"{n}x{n}の掛け算表が作成されました。 multiplication_table_{n}x{n}.xlsx")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("実行: python script.py N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("Nは整数でなければなりません")
        sys.exit(1)

    if N <= 0:
        print("Nは正の整数でなければなりません")
        sys.exit(1)

    create_multiplication_table(N)

