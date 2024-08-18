import sys

while True:
    str = sys.stdin.readline().strip()
    n, m = str.split("R")[1].split("C")
    
    if n == "0" and m == "0":
        break

    excel_col = ""

    while int(m) > 0:
        if int(m) % 26 == 0:
            excel_col = "Z" + excel_col
            m = int(m) // 26 - 1
        else:
            excel_col = chr(64 + int(m) % 26) + excel_col
            m = int(m) // 26


    print(excel_col + n)