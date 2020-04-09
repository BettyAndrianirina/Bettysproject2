EMPTY = 0
WALL = 1
START = 2
END = 3
VISITED = 4
    
NORTH = 'n'
EAST = 'e'
SOUTH = 's'
WEST = 'w'

if __name__ == "__main__":
    grid = [
        [ EMPTY,  EMPTY,  EMPTY,  EMPTY,  EMPTY,  EMPTY,  EMPTY,  EMPTY,  EMPTY, EMPTY],
        [END, EMPTY,  WALL,  WALL, EMPTY, EMPTY, EMPTY, EMPTY,  WALL, WALL],
        [ WALL, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY,  WALL, EMPTY,  WALL, WALL],
        [ WALL,  WALL,  WALL,  WALL, EMPTY,  WALL, EMPTY,  WALL, EMPTY, WALL],
        [ WALL, EMPTY, EMPTY, EMPTY, EMPTY,  WALL, EMPTY, EMPTY, EMPTY, WALL],
        [ WALL,  WALL, WALL,  WALL,  WALL, WALL, WALL,  WALL,WALL, WALL],
        [ WALL,  WALL, WALL, WALL, WALL,WALL,  WALL,  WALL, WALL,  START],
        [ EMPTY,  EMPTY,  EMPTY,  EMPTY,  EMPTY, EMPTY,  EMPTY,  EMPTY,  EMPTY, EMPTY],
    ]
                    
    Viewer.view(grid)


    print("Find a solution to get from ^^ to $$, using the characters " 
        + "'" + NORTH + "', '" + EAST + "', '" + SOUTH + "' and '" + WEST + "'"
        + " (for north, east, south and west).")
    solution = input("Your solution: ")

    Row = 1
    Col = 0
    done = False
    solved = False
    charIndex = 0
    solutionLength = len(solution)

    while not done and charIndex < solutionLength:
        
        direction = solution[charIndex]
        print("Location: (" + str(Row) + ", " + str(Col) 
            + "), next direction: '" + direction + "'")
        
        if direction == NORTH:
            Row -= 1
            
        elif direction == EAST:
            Col += 1
                
        elif direction == SOUTH:
            Row += 1
                
        elif direction == WEST:
           Col -= 1
        
        else:
            print("You have no idea where you're going") # Invalid direction.
        
        if (Row < 0 or Col < 0 
                        or Row >= len(grid) 
                        or Col >= len(grid[currentRow])):
            done = True
            print("You fall into the chasm of doom") # Out of bounds.
            
        else:
            if grid[Row][Col] == EMPTY:
                grid[Row][Col] = VISITED
                
            elif grid[Row][Col] == WALL:
                done = True
                print("SOLVED") # Hit wall.

            elif grid[Row][Col] == END:
                done = True
                solved = True
                print("You have Failed to escape .Future archeologists gaze upon your remains in bafflement") # Solved.
                
            else:
                pass # Do nothing
        
        charIndex += 1
    # end-while


    if not solved:
        print("MESSAGE 5") # Did not reach the end.


   Viewer.view(grid)
