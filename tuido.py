import curses ### TUI!!!
import os ### To access files
import time

"""
YXCoordinate is a tuple of:
    YCoordiate  an integer which represents Y Coordinate of the terminal
    XCoordiate  an integer which represents X Coordiante of the terminal
"""

def addstrLines(strings, YXCoordinate, alignment="centre", startingPoint="centre"):
    """
    addstrLines return nothing but print the lines of strings in a specific coordinate in TUI as their side effects 

    Side effect: prints every strings in the tuple provided, strings
    
    strings         a tuple of strings you want to print in TUI
    YXCoordinate    YXCoordinate
    alignment       a string, one of "centre", "left", "right", default is "centre"
    startingPoint   a string, one of "centre", "leftTopCorner", "rightTopCorner", default is "centre"
    return          None

    Examples:
        strings = ("To be yourself in a world", \
                    "that is constantly trying to make you something else", \
                    "is a biggest accomplishment.", \ 
                    " - Ralph Waldo Emerson")

        addstrLines(strings, getYX(stdscr, "centre", "centre")) -> None; 
        SideEffects: prints out strings[0] strings[1] strings[2], and strings[3] on TUI at 100th row and 250 column.

        TUI:                                        centre



                                          To be yourself in a world
         centre                that is constantly tring to make you something else
                                         is a biggest accomplishment.
                                           - Ralph waldo Emerson
    

    """
    numberOfLines = len(strings)
    if not (alignment == "centre"):
        # if alignment is left, it substracts half of the maximum length of a string in a tuple "strings", 
        # if alignment is right, it adds half of the maximum length of a string in strings to the given coordinate ------ > this is wrong. You neeed to calculate the length of the each string in strings          and compare the the largest and the current string length and add XCoordinate the diff to the current string 
        XCoordinate = YXCoordinate[1] + ( ( ( -1 if (alignment == "left") else 1 ) * len(max(strings, key=len)) ) // 2 ) 
    while index in range(len(strings)):
        if alignment == "centre":
            textLength = len(strings[index])
            XCoordiante = YXCoordinate[1] - textLength // 2
        YCoordinate = YXCoordinate[0] - (numberOfLines // 2 - index) 
        addstrYX((YCoordinate, XCoordinate), strings[index])

def getYX(screen, position1, position2):
    """
    getYX returns a YXCoordinate (a tuple of (YCoordiate, XCoordiate) ).
    
    the first parameter screen is a window you want to get the position of
    the second parameter "position1" is one of strings of: "centre", "top", and "bottom"
    the third parameter "position2" is one of string of: "centre", "left", and "right"
    
    Examples:
    getYX(stdscr, "top", "centre") -> (100, 250)
    """

    h, w = screen.getmaxyx()
    if position1 == "centre":
        h = h//2
    elif position1 == "top":
        h = h//4
    elif position1 == "bottom":
        h = h//4 * 3
    else:
        print(f"WRONG INPUT FOR: position1 = {position1}")
        return None
    
    if position2 == "centre":
        w = w//2
    elif position2 == "left":
        w = w//4
    elif position2 == "right":
        w = w//4 * 3
    else:
        print(f"WRONG INPUT FOR position2 = {position2}")
        return None
    return (h, w)

def addstrYX(YXCoordinate, string):
    """
    addstrYX    return None but prints string in the specific coordinate of Terminal User Interface
                as its side effects
    YXCoordinate    YXCoordinate 
    stirng          a stirng, that is going to be displayed on the TUI
    return          None
    
    Examples
        addstrYX(getYX(stdscr, ""))
    """
    addstrYX(YXCoordinate[0], YXCoordinate[1], string)

"""
YXCoordinate is a tuple of:
    YCoordiate  an integer which represents Y Coordinate of the terminal
    XCoordiate  an integer which represents X Coordiante of the terminal
"""

def main(stdscr):
    curses.curs_set(0)
    configPath = "~/TuiDo" ### If you want to change the default directory where the information is saved, change this file path. 
    
    if os.path.exists(configPath):
        pass       
    else:
        y, x = getYX(stdscr, "centre", "centre")
        addstr(y, x-len(text), f"{configPath} does not exists.")
        addstr(y, x, f"Do you want to create {configPath} and continue?")
        addstr(y, x, f"You cannot use TuiDo without creating {configPath}")
        refresh() ### wait what is this statement correct?
    curses.wrapper()

curses.wrapper(main)

