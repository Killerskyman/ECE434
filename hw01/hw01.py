# import curses and the wrapper for easy initialization
import curses
from curses import wrapper


# main function of the program
def main(stdscr):
    # clear the screen
    stdscr.clear()
    # make it so the cursor doesn't blink (if supported)
    stdscr.leaveok(True)
    # make sure that getch is a blocking function
    stdscr.nodelay(False)
    # assign variables to the cursor position
    curX = 0
    curY = 0

    while True:
        # getch refreshes the screen and waits for user input
        c = stdscr.getch()
        # check to see which arrow key was pressed if any and adjust the cursor position
        if c == curses.KEY_UP:
            curY = curY - 1
        elif c == curses.KEY_DOWN:
            curY = curY + 1
        elif c == curses.KEY_LEFT:
            curX = curX - 1
        elif c == curses.KEY_RIGHT:
            curX = curX + 1
        # make sure the cursor position doesn't go to illegal values
        if curX >= curses.COLS:
            curX = curses.COLS - 1
        if curX <= 0:
            curX = 0
        if curY >= curses.LINES:
            curY = curses.LINES - 1
        if curY <= 0:
            curY = 0
        # move the cursor to the correct spot
        stdscr.move(curY, curX)
        # insert the text
        stdscr.addstr(chr(42))
        # clear screen if d is pressed 100 = 'd' in ascii
        if c == 100:
            stdscr.clear()
        # break the while loop and exit application if 'x' is pressed 120 = 'x'
        if c == 120:
            break


# this starts the program using the wrapper provided in curses
wrapper(main)
