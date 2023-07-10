import tkinter as tk

# Function to highlight a cell in a specified color
def highlight_cell(row, col, color):
    x1 = 50 + (col - 1) * 300 / 9
    y1 = 50 + (row - 1) * 300 / 9
    x2 = x1 + 300 / 9
    y2 = y1 + 300 / 9
    canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="")

# Create a new window
window = tk.Tk()

# Create a canvas to draw the board
canvas = tk.Canvas(window, width=400, height=400)
canvas.pack()

# Highlight specific cells in red
highlight_cell(1, 5, "red")  # A5
highlight_cell(2, 1, "red")  # B1
highlight_cell(2, 9, "red")  # B9
highlight_cell(6, 1, "red")  # F1
highlight_cell(6, 9, "red")  # F9
highlight_cell(5, 4, "red")  # E4
highlight_cell(5, 8, "red")  # E8
highlight_cell(9, 3, "red")  # I3
highlight_cell(9, 7, "red")  # I7
highlight_cell(7, 5, "red")  # G5

# Highlight specific cells in green
highlight_cell(1, 4, "green")  # A4
highlight_cell(1, 8, "green")  # A8
highlight_cell(3, 1, "green")  # C1
highlight_cell(4, 5, "green")  # D5
highlight_cell(5, 3, "green")  # E3
highlight_cell(5, 9, "green")  # E9
highlight_cell(7, 1, "green")  # G1
highlight_cell(8, 5, "green")  # H5
highlight_cell(9, 4, "green")  # I4
highlight_cell(9, 8, "green")  # I8

# Highlight specific cells in yellow
highlight_cell(1, 2, "yellow")  # A2
highlight_cell(1, 6, "yellow")  # A6
highlight_cell(2, 5, "yellow")  # B5
highlight_cell(3, 9, "yellow")  # C9
highlight_cell(5, 1, "yellow")  # E1
highlight_cell(5, 7, "yellow")  # E7
highlight_cell(6, 5, "yellow")  # F5
highlight_cell(7, 9, "yellow")  # G9
highlight_cell(9, 2, "yellow")  # I2
highlight_cell(9, 6, "yellow")  # I6

# Highlight specific cells in very light grey (almost white)
highlight_cell(1, 1, "#f7f7f7")  # A1
highlight_cell(1, 9, "#f7f7f7")  # A9
highlight_cell(5, 5, "#f7f7f7")  # E5
highlight_cell(9, 1, "#f7f7f7")  # I1
highlight_cell(9, 9, "#f7f7f7")  # I9

# Highlight specific cells in blue
highlight_cell(1, 3, "blue")  # A3
highlight_cell(1, 7, "blue")  # A7
highlight_cell(3, 5, "blue")  # C5
highlight_cell(4, 1, "blue")  # D1
highlight_cell(4, 9, "blue")  # D9
highlight_cell(5, 2, "blue")  # E2
highlight_cell(5, 6, "blue")  # E6
highlight_cell(8, 1, "blue")  # H1
highlight_cell(8, 9, "blue")  # H9
highlight_cell(9, 5, "blue")  # I5

# Remove specific cells
remove_cells = [(2, 2), (2, 3), (2, 4), (2, 6), (2, 7), (2, 8),
                (3, 2), (3, 3), (3, 4), (3, 6), (3, 7), (3, 8),
                (4, 2), (4, 3), (4, 4), (4, 6), (4, 7), (4, 8),
                (6, 2), (6, 3), (6, 4), (6, 6), (6, 7), (6, 8),
                (7, 2), (7, 3), (7, 4), (7, 6), (7, 7), (7, 8),
                (8, 2), (8, 3), (8, 4), (8, 6), (8, 7), (8, 8)]

for cell in remove_cells:
    row, col = cell
    x1 = 50 + (col - 1) * 300 / 9
    y1 = 50 + (row - 1) * 300 / 9
    x2 = x1 + 300 / 9
    y2 = y1 + 300 / 9
    canvas.create_rectangle(x1, y1, x2, y2, fill="white", outline="")

# Start the main event loop
window.mainloop()
