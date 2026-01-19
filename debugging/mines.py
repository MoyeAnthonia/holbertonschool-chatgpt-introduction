#!/usr/bin/python3
import random
import os

def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

class Minesweeper:
    def __init__(self, width=10, height=10, mines=10):
        self.width = width
        self.height = height
        self.mines = set(random.sample(range(width * height), mines))
        self.revealed = [[False for _ in range(width)] for _ in range(height)]

    def print_board(self, reveal=False):
        """Print the game board."""
        print('  ' + ' '.join(str(i) for i in range(self.width)))
        for y in range(self.height):
            print(y, end=' ')
            for x in range(self.width):
                if reveal or self.revealed[y][x]:
                    if (y * self.width + x) in self.mines:
                        print('*', end=' ')
                    else:
                        count = self.count_mines_nearby(x, y)
                        print(count if count > 0 else ' ', end=' ')
                else:
                    print('.', end=' ')
            print()

    def count_mines_nearby(self, x, y):
        """Count mines in adjacent cells."""
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    if (ny * self.width + nx) in self.mines:
                        count += 1
        return count

    def reveal(self, x, y):
        """Reveal a cell; recursively reveal neighbors if zero nearby mines."""
        if self.revealed[y][x]:
            return True

        if (y * self.width + x) in self.mines:
            return False

        self.revealed[y][x] = True

        if self.count_mines_nearby(x, y) == 0:
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < self.width and 0 <= ny < self.height:
                        if not self.revealed[ny][nx]:
                            self.reveal(nx, ny)
        return True

    def check_win(self):
        """Check if all non-mine cells have been revealed."""
        revealed_cells = sum(
            self.revealed[y][x]
            for y in range(self.height)
            for x in range(self.width)
        )
        return revealed_cells == (self.width * self.height - len(self.mines))

    def play(self):
        """Main game loop with input validation and graceful exit."""
        try:
            while True:
                self.print_board()
                
                # Wrap input parsing in a try/except for ValueError
                try:
                    x = int(input("Enter x coordinate: "))
                    y = int(input("Enter y coordinate: "))
                except ValueError:
                    print("Invalid input. Please enter numbers only.")
                    continue

                if not (0 <= x < self.width and 0 <= y < self.height):
                    print("Coordinates out of bounds. Try again.")
                    continue

                if not self.reveal(x, y):
                    self.print_board(reveal=True)
                    print("💥 Game Over! You hit a mine.")
                    break

                if self.check_win():
                    self.print_board(reveal=True)
                    print("🎉 Congratulations! You won!")
                    break

        except KeyboardInterrupt:
            # Handle Ctrl+C gracefully
            print("\n\n⛔ Game interrupted by user. Goodbye!")

if __name__ == "__main__":
    game = Minesweeper()
    game.play()
