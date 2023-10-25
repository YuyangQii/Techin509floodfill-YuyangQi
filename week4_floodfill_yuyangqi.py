# -*- coding: utf-8 -*-
"""WEEK4_YuyangQi.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-BMKFZzf_KPoNZZzRIxhumKqqfxEy-pg

# Flood Fill Function and GitHub Version Control
"""

from typing import List

def flood_fill(input_board: List[str], old: str, new: str, x: int, y: int) -> List[str]:
    """
    Args:
        input_board (List[str]): The original board.
        old (str): The character to be replaced.
        new (str): The new character.
        x (int): The x-coordinate where the fill starts.
        y (int): The y-coordinate where the fill starts.

    Returns:
        List[str]: The modified board.
    """
    # Check if the starting point is within the bounds of the board and the character at (x, y) is the old character
    if y < 0 or y >= len(input_board) or x < 0 or x >= len(input_board[y]) or input_board[y][x] != old:
        return input_board
    # Convert each row of characters to a list
    board = [list(row) for row in input_board]

    def change(x: int, y: int):
        if x < 0 or x >= len(board[0]) or y < 0 or y >= len(board):
            return
        if board[y][x] == old:
            board[y][x] = new
    # Recursive calls to fill the surrounding areas
            change(x + 1, y)
            change(x - 1, y)
            change(x, y + 1)
            change(x, y - 1)

    change(x, y)
    # Convert each row back from a list to a string
    return [''.join(row) for row in board]


board = [
    "......................",
    "......##########......",
    "......#........#......",
    "......#........#......",
    "......#........#####..",
    "....###............#..",
    "....#............###..",
    "....##############....",
]

modified_board = flood_fill(input_board=board, old=".", new="~", x=12, y=5)  # 注意，根据您的画板和期望输出，坐标应该是x=12, y=5，而不是x=5, y=12

for a in modified_board:
    print(a)