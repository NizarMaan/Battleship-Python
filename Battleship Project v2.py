#Nizar Maan ID 10103889
#University of Calgary
#CPSC 231 - 03 Nathaly Verwaal
#Tutorial T11 Hesam Alizadeh Talarposhti

GRID_WIDTH = 10
GRID_HEIGHT = 10


vessel_names = ["Aircraft Carrier", "Battleship", "Submarine", "Destroyer"]
vessel_sizes = [5, 4, 3, 2]

num_of_vessels = 0

# Create a grid filled with blanks
B = '_'
grid = [[B,B,B,B,B,B,B,B,B,B], \
            [B,B,B,B,B,B,B,B,B,B], \
            [B,B,B,B,B,B,B,B,B,B], \
            [B,B,B,B,B,B,B,B,B,B], \
            [B,B,B,B,B,B,B,B,B,B], \
            [B,B,B,B,B,B,B,B,B,B], \
            [B,B,B,B,B,B,B,B,B,B], \
            [B,B,B,B,B,B,B,B,B,B], \
            [B,B,B,B,B,B,B,B,B,B], \
            [B,B,B,B,B,B,B,B,B,B]]

global num_of_vessels
global vessel_names
global vessel_sizes
global grid

def info() :
    splash_screen = print('''
 __    __     _ 
/ / /\ \ \___| | ___ ___  _ __ ___   ___ 
\ \/  \/ / _ \ |/ __/ _ \| '_ ` _ \ / _ \
 \  /\  /  __/ | (_| (_) | | | | | |  __/
  \/  \/ \___|_|\___\___/|_| |_| |_|\___|


 _ 
| |_ ___  
| __/ _ \ 
| || (_) |
 \__\___/

   ___       _   _   _        __ _     _       
  / __\ __ _| |_| |_| | ___  / _\ |__ (_)_ __  
 /__\/// _` | __| __| |/ _ \ \ \| '_ \| | '_ \ 
/ \/  \ (_| | |_| |_| |  __/ _\ \ | | | | |_) |
\_____/\__,_|\__|\__|_|\___| \__/_| |_|_| .__/ 
                                        |_|   
   
                                       ''')
        

# Prints the content in the global variable grid to the console
# in a way that is easy to read for the user.
def print_grid() :
    # print the labels of the columns first
    print("   A B C D E F G H I J")
    for row_index in range(0, GRID_HEIGHT) :
        # print the label of the row on the current line
        print(row_index + 1, '', end="")
        # add an extra space if the number is a single digit number
        # this is to ensure rows with a single and double digit
        # number line up the same.
        if (row_index + 1 < 10) :
            print(' ', end="")

        for column_index in range(0, GRID_WIDTH) :
            print(grid[row_index][column_index], '', end="")

        # finished printing all items in the row.  Print a newline to go to
        # the next row.
        print()


def get_location(vessel_name, vessel_size):
    #set up variables for while loop checks
    valid_direction = False
    valid_str = False
    valid_int = False

    print("Enter the location of your", vessel_name)

    while valid_str == False:
        column = input("Left Column (A-J): ") 
        if column not in ("ABCDEFGHIJ"):
            print("Please enter a capital letter between A-J")
        else:
            valid_str= True   

    while valid_int == False:
        row = int(input("Top Row (1-10): "))
        if row > 10 or row < 1: 
            print("Please enter a number between 1-10")            
        else:
            valid_int = True
    #Get the direction of the vessel
    direction = input("Give the direction of your vessel (horizontal or vertical): ")

    while valid_direction == False:
        if direction != ("horizontal") and direction !=("vertical"):
            direction = input("Please give a valid direction: ")
        else:
            valid_direction = True 
def main() :
    info()
    print("Empty grid:")
    print_grid()
    print()

    x=0
    for names in vessel_names:
        get_location(vessel_names[x],vessel_sizes[x])
        x= x+1
    
    grid[0][0] = 5
    grid[0][1] = 5
    grid[0][2] = 5
    grid[0][3] = 5
    grid[0][4] = 5
    print("Added aircraft carrier: ")
    print_grid()

        

main()
