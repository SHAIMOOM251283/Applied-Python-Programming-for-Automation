import sys
import openpyxl
from openpyxl.styles import Alignment, Font

def create_multiplication_table(N):
    wb = openpyxl.Workbook()
    sheet = wb.active

    # Apply styles to center text in cells
    align_center = Alignment(horizontal='center', vertical='center')
    font_bold = Font(bold=True)

    # Fill in multiplication table
    for i in range(1, N+1):
        for j in range(1, N+1):
            result = i * j
            cell = sheet.cell(row=i, column=j, value=result)
            cell.alignment = align_center
            if i == 1:
                cell.font = font_bold  # Bold font for header row
            if j == 1:
                cell.font = font_bold  # Bold font for first column

    return wb

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python multiplicationTable.py <N>")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        if N <= 0:
            raise ValueError("N must be a positive integer.")
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

    workbook = create_multiplication_table(N)
    workbook.save(f'multiplication_table_{N}x{N}.xlsx')
    print(f"Multiplication table saved to multiplication_table_{N}x{N}.xlsx")
