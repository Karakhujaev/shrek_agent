#!/usr/bin/env python3
"""
Simple Snake Game for Terminal
Use arrow keys or WASD to control the snake.
Press 'q' to quit.
"""

import curses
import random
import time


def main(stdscr):
    # Setup curses
    curses.curs_set(0)  # Hide cursor
    stdscr.nodelay(1)   # Non-blocking input
    stdscr.timeout(100) # Refresh rate (ms)
    
    # Get screen dimensions
    sh, sw = stdscr.getmaxyx()
    
    # Create game window
    win = curses.newwin(sh, sw, 0, 0)
    win.keypad(1)
    win.timeout(100)
    
    # Initialize snake position (start in middle)
    snake_x = sw // 4
    snake_y = sh // 2
    
    # Snake body (list of [y, x] positions)
    snake = [
        [snake_y, snake_x],
        [snake_y, snake_x - 1],
        [snake_y, snake_x - 2]
    ]
    
    # Initial food position
    food = [sh // 2, sw // 2]
    win.addch(food[0], food[1], '*')
    
    # Initial direction (moving right)
    key = curses.KEY_RIGHT
    
    # Score
    score = 0
    
    while True:
        # Display score
        win.addstr(0, 2, f' Score: {score} ')
        
        # Get next key press
        next_key = win.getch()
        
        # Keep previous direction if no key pressed or invalid key
        if next_key == -1:
            pass
        elif next_key == ord('q') or next_key == ord('Q'):
            break
        elif next_key in [curses.KEY_UP, ord('w'), ord('W')] and key != curses.KEY_DOWN:
            key = curses.KEY_UP
        elif next_key in [curses.KEY_DOWN, ord('s'), ord('S')] and key != curses.KEY_UP:
            key = curses.KEY_DOWN
        elif next_key in [curses.KEY_LEFT, ord('a'), ord('A')] and key != curses.KEY_RIGHT:
            key = curses.KEY_LEFT
        elif next_key in [curses.KEY_RIGHT, ord('d'), ord('D')] and key != curses.KEY_LEFT:
            key = curses.KEY_RIGHT
        
        # Calculate new head position
        head = snake[0]
        if key == curses.KEY_UP:
            new_head = [head[0] - 1, head[1]]
        elif key == curses.KEY_DOWN:
            new_head = [head[0] + 1, head[1]]
        elif key == curses.KEY_LEFT:
            new_head = [head[0], head[1] - 1]
        elif key == curses.KEY_RIGHT:
            new_head = [head[0], head[1] + 1]
        
        # Insert new head
        snake.insert(0, new_head)
        
        # Check if snake hit the wall
        if (new_head[0] <= 0 or new_head[0] >= sh - 1 or
            new_head[1] <= 0 or new_head[1] >= sw - 1):
            break
        
        # Check if snake hit itself
        if new_head in snake[1:]:
            break
        
        # Check if snake ate the food
        if new_head == food:
            score += 10
            food = None
            while food is None:
                new_food = [
                    random.randint(2, sh - 2),
                    random.randint(2, sw - 2)
                ]
                food = new_food if new_food not in snake else None
            win.addch(food[0], food[1], '*')
        else:
            # Remove tail
            tail = snake.pop()
            win.addch(tail[0], tail[1], ' ')
        
        # Draw snake head
        try:
            win.addch(snake[0][0], snake[0][1], '#')
        except curses.error:
            pass
    
    # Game Over
    win.nodelay(0)
    win.clear()
    game_over_msg = "GAME OVER!"
    score_msg = f"Final Score: {score}"
    quit_msg = "Press any key to exit..."
    
    win.addstr(sh // 2 - 1, (sw - len(game_over_msg)) // 2, game_over_msg)
    win.addstr(sh // 2, (sw - len(score_msg)) // 2, score_msg)
    win.addstr(sh // 2 + 1, (sw - len(quit_msg)) // 2, quit_msg)
    
    win.getch()


if __name__ == "__main__":
    curses.wrapper(main)
