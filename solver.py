# Ask the user for the text file input
import time
filename = input('Enter sudoku filename:\n')

# Import the text file into a matrix

f_open = open(filename, 'r')

text = f_open.read()

f_open.close()

list = text.split('\n')

list.remove('')

sudoku = []

for a in range(len(list)):
    sudoku.append([])
    for b in list[a]:
        sudoku[a].append(int(b))

# Check that the file is of the correct type (9 x 9 with numbers 0 - 9)

correct_file = True

digits = [0,1,2,3,4,5,6,7,8,9]

if len(sudoku) != 9:
    correct_file = False

for a in sudoku:

    if len(a) != 9:
        correct_file = False

    for b in a:
        if b not in digits:
            correct_file = False

if correct_file == False:
    print('Wrong filetype! Please read the documentation.')
    exit()

# Make a list with the positions of every zero

zeros = []

for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            zeros.append([i,j])

# Create a list with the coordinates of each box

boxes = [[[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]],[[0,3],[0,4],[0,5],[1,3],[1,4],[1,5],[2,3],[2,4],[2,5]],[[0,6],[0,7],[0,8],[1,6],[1,7],[1,8],[2,6],[2,7],[2,8]],[[3,0],[3,1],[3,2],[4,0],[4,1],[4,2],[5,0],[5,1],[5,2]],[[3,3],[3,4],[3,5],[4,3],[4,4],[4,5],[5,3],[5,4],[5,5]],[[3,6],[3,7],[3,8],[4,6],[4,7],[4,8],[5,6],[5,7],[5,8]],[[6,0],[6,1],[6,2],[7,0],[7,1],[7,2],[8,0],[8,1],[8,2]],[[6,3],[6,4],[6,5],[7,3],[7,4],[7,5],[8,3],[8,4],[8,5]],[[6,6],[6,7],[6,8],[7,6],[7,7],[7,8],[8,6],[8,7],[8,8]]]

# For each item in zeros, assign a score which is the sum of the number of zeros in its row, column and box

mydict = {}

for zero in zeros:

    score = 0
    
    # Boxes first
    
    box_index = -1
    
    for box in range(len(boxes)):
        if zero in boxes[box]:
            box_index = box
            
    for a in boxes[box_index]:
        if a in zeros:
            score += 1
            
    # Now rows
    
    row = zero[0]
    
    for a in zeros:
        if a[0] == row:
            score += 1
            
    # Now columns
    
    column = zero[1]
    
    for a in zeros:
        if a[1] == column:
            score += 1
            
    mydict[tuple(zero)] = score
    
# Now sort the dictionary according to the scores (so the backtracking algorithm starts with the zeros with the most information)

zeros = sorted(mydict, key=mydict.__getitem__)

# Convert zeros back to lists:

zeros_list = [[a[0],a[1]] for a in zeros]

zeros = zeros_list

# Now for the backtracking algorithm

sudoku_complete = False

index = 0

value = 1

attempts = 0

while sudoku_complete == False:

    attempts += 1
    
    sudoku[zeros[index][0]][zeros[index][1]] = value
    
    # Perform check to see if this value is ok:
    
    ok_guess = True
    
    # First check boxes
    
    box_index = -1
    
    for box in range(len(boxes)):
        if zeros[index] in boxes[box]:
            box_index = box

    for a in boxes[box_index]:
        if a == zeros[index]:
            continue
        elif sudoku[a[0]][a[1]] == value:
            ok_guess = False
            break
       
    # Now check rows
            
    row = zeros[index][0]
    
    for a in range(9):
        if ok_guess == False:
            break
        tempindex = [row, a]
        if tempindex == zeros[index]:
            continue
        elif sudoku[row][a] == value:
            ok_guess = False
            break
          
    # Now check columns
    
    column = zeros[index][1]
    
    for a in range(9):
        if ok_guess == False:
            break
        tempindex = [a,column]
        if tempindex == zeros[index]:
            continue
        elif sudoku[a][column] == value:
            ok_guess = False
            break
  
# Now implement what the backtracking algorithm should do
    if ok_guess == True:
        index += 1
        value = 1
        
    elif ok_guess == False and value != 9:
        value += 1
    
    elif ok_guess == False and value == 9:
        while sudoku[zeros[index][0]][zeros[index][1]] == 9:
            sudoku[zeros[index][0]][zeros[index][1]] = 0
            index += -1
        value = sudoku[zeros[index][0]][zeros[index][1]] + 1
      
    # Now check if the puzzle has been completed
        
    if index == len(zeros):
        sudoku_complete = True
        
    sudoku_string = '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n'

    for a in sudoku:
        for b in a:
            sudoku_string += str(b)
        sudoku_string += '\n'
        
    print(sudoku_string)
    #time.sleep(0.01)

# Now put the completed sudoku in a string


        
# Now put the string into a new file
        
new_filename = filename.replace('.txt', '_solved.txt')

new_file = open(new_filename, 'w')

new_file.write(sudoku_string)

new_file.close()

print('Number of iterations: ' + str(attempts))
        
