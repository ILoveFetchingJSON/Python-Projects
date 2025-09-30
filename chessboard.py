import tkinter as tk

BOARD_SIZE = 8
SQUARE_SIZE = 60

class ChessGUI:
    def __init__(self, root, title):
        self.root = root
        self.title = root.title(title)
        self.canvas = tk.Canvas(root, width=BOARD_SIZE * SQUARE_SIZE, height=BOARD_SIZE * SQUARE_SIZE)
        self.canvas.pack()
        self.CENTER_SQUARE_MAP = {}  # Maps "e4" → (x, y)
        self.draw_starting_position()

    def on_click(self, event):
        self.dragged_piece = self.canvas.find_closest(event.x, event.y)[0]
    def on_drag(self, event):
        self.canvas.coords(self.dragged_piece, event.x, event.y)
    def on_drop(self, event):
        drop_x = event.x
        drop_y = event.y
        distance_x = drop_x - event.x
        distance_y = drop_y - event.y
        minimum_val = float('inf')
        for coords, (x, y) in self.CENTER_SQUARE_MAP.items():
            distance_x = drop_x - x
            distance_y = drop_y - y
            distance = (distance_x ** 2) + (distance_y ** 2)
            if distance < minimum_val:
                minimum_val = distance
                closest_coords = (x, y)
        self.canvas.coords(self.dragged_piece, *closest_coords)
            
    def draw_starting_position(self):
        colors = ["#6CB16C", "#FFF6A0"]

        # Draw squares and map centers
        for row_index in range(BOARD_SIZE):
            for col_index in range(BOARD_SIZE):
                x1 = col_index * SQUARE_SIZE
                y1 = row_index * SQUARE_SIZE
                x2 = x1 + SQUARE_SIZE
                y2 = y1 + SQUARE_SIZE

                center = (x1 + SQUARE_SIZE // 2, y1 + SQUARE_SIZE // 2)
                name = f"{chr(97 + col_index)}{8 - row_index}"  # e.g. "a1", "e4"
                self.CENTER_SQUARE_MAP[name] = center

                color = colors[(row_index + col_index) % 2]
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color)

        # Place pieces using Unicode
        pieces = {
            "a1": "\u2656", "b1": "\u2658", "c1": "\u2657", "d1": "\u2655", "e1": "\u2654", "f1": "\u2657", "g1": "\u2658", "h1": "\u2656",
            "a2": "\u2659", "b2": "\u2659", "c2": "\u2659", "d2": "\u2659", "e2": "\u2659", "f2": "\u2659", "g2": "\u2659", "h2": "\u2659",
            "a7": "\u265F", "b7": "\u265F", "c7": "\u265F", "d7": "\u265F", "e7": "\u265F", "f7": "\u265F", "g7": "\u265F", "h7": "\u265F",
            "a8": "\u265C", "b8": "\u265E", "c8": "\u265D", "d8": "\u265B", "e8": "\u265A", "f8": "\u265D", "g8": "\u265E", "h8": "\u265C"
        }

        for square, piece in pieces.items():
            x, y = self.CENTER_SQUARE_MAP[square]
            fill = "black" if piece in "\u265A\u265B\u265C\u265D\u265E\u265F" else "white"
            text = self.canvas.create_text(x, y, text=piece, font=("Arial", 32), fill=fill)
            self.canvas.tag_bind(text, "<Button-1>", self.on_click)
            self.canvas.tag_bind(text, "<B1-Motion>", self.on_drag)
            self.canvas.tag_bind(text, "<ButtonRelease-1>", self.on_drop)
  # Placeholder for drop logic
            


if __name__ == "__main__":
    root = tk.Tk()
    gui = ChessGUI(root, "Tkinter is awesome!")
    root.mainloop()