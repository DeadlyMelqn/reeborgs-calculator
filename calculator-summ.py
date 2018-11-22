"""
Title: Calculator Reeborg's world
Date: Nov. 7, 2018
Author: Yuvraj Chohan

2 Portions - Calculating, Plotting

star - integers
 ^ token - zero
carrot - remainder
 ^ strawberry - zero

a > b - a is greater than
a < b - a is smaller than

elif - else if - make it check another condition if last one failed
list = allows you to store multiple values

THIS CODE IS MENT TO BE USED ON AN EMPTY TEMPLATE! CODE BELOW WILL DO SO,
IF NOT THEN SWITCH TO WORLD "ALONE", SET ROBOT POS TO 1,10.
THEN GIVE ENOUGH STARS, CARROTS, TOKENS, STRAWBERRIES TO ROBOT
"""
import reeborg_en

## WORLD/ROBOT SETTINGS ##
# create environment automatically, drastically reduces processing time
think(0)
World("Alone")
remove_robots()
reeborg = UsedRobot(1, 10)
for item in ["star", "carrot", "token", "strawberry"]:
    RUR.give_object_to_robot(item,100)

## GLOBAL VARIABLES ##
loop = 1

## CLASSES AND DEFINITONS ##
# CALCULATING #
class calculation:
    #operators=['add', 'sub', 'mul', 'mod']

    # init used to put initial equation
    def __init__(self, operator, num1, num2):
        # self. is used to allow var to be used in all functions in the class
        self.operator = operator
        self.num1 = num1
        self.num2 = num2

    #def operation(v):
    #    for i, op in enumerate(operators):
    #        if op in self.operator:
    #            self.operator = operators[i]

   # calculate
    def main_p1(self):
        # create new vars to return
        self.total = 0
        self.remainder = 0
        # identify what operator has been inputted
        if "add" in self.operator:
            self.total = self.num1 + self.num2
        elif "sub" in self.operator:
            self.total = self.num1 - self.num2
            if (self.total < 0):
                # raise an error as reeborg cannot place negative objects
                raise ReeborgError(" ! You're only allowed to subtract a smaller number")
        elif "mul" in self.operator:
            self.total = self.num1 * self.num2
        elif "div":
            self.total = self.num1 // self.num2
            self.remainder = self.num1 % self.num2
        elif "mod" in self.operator:
            self.total = self.num1 % self.num2
        else:
            raise ReeborgError(" ! Unknown operation")

    def returnValue(self):
        # return values to give to main function, so it can plot the values
        return [self.num1, self.num2, self.total, self.remainder]

# Functions that better enable and improve reeborg's ability to move and etc
#manipulate turn_left() to make a definiton to turn right, left, or look behind
def turn(x):
    if x == "left" or x == 0:
        turn_left()
    elif x == "right" or x == 1:
        for i in range(0,3):
            turn_left()
    elif x == "behind" or x == 2:
        for i in range(0,2):
            turn_left()
    else:
        raise ReeborgError(" ! You can only move behind, left, right")
#now define amount of steps and stop running into walls
def adv_move(x=1):
    for i in range(0,x):
        if not wall_in_front():
            move()
        else:
            print(" ! Cannot move any further. Exiting function")
            break
#allows you to put a specific amount and appropiately substitute zeros
def adv_put(x=1,y="star"):
        for i in range(0,x):
                put(y)
#move down appropiatly and reset to plot rest of equation
# TODO: remove, unnecessary and can type in loop. more specific-scenario for calculator
def move_lane(x):
    for i in range(0,2):
        adv_move()
        turn(x)

# PLOTTING #

# Functions to fulfill plotting requirements by dividing and/or modulus.
# Could have just used string and then the length of it.
#count amount of digits
def digits(x):
    count = 0
    while (x > 0):
        x = x // 10
        count = count + 1
    return count
#split digits into list
def split_digits(x):
    if (x < 10):
        return [x]
    else:
        return split_digits(x // 10) + [x % 10]

# Create a nested loop that sorts out digit length, splits digits into appropiate location, and plots
def main(calc):
    # create dict that makes a list for each lane to properly place each digit
    plot = {}

    # identify digit length to space appropiately
    digit_amount = digits(max(calc))
    print("DEBUG: digit_amount is", digit_amount)

    robot = position_here()
    enough_space = 10 - robot[0]
    if ((digit_amount + 1) >= enough_space):
        turn("right")
        adv_move(4)
        turn("right")
        adv_move(robot[0])
        turn("behind")

    """
    Enumerate is used to grab an iterative of a list or dict with list (in my case) and
    they are assigned to local variables of my choosing.

    Enumerate can be used in lots of cases but explained for my case of use.
    """
    for i, value in enumerate(calc[:-1]):
        # split digits into each lane. using the dict i had initiatited
        plot[i] = split_digits(value)
        print("DEBUG: before placeholders", plot[i])

        # prevents looping into last lane and starting new lane. allows me to place remainder
        if i != 3:
            # compares current digits to largest digits and makes placeholders to ensure proper digit location
            if (digit_amount > digits(value)):
                placeholders = digit_amount - digits(value)
                print("DEBUG: placeholders is", placeholders)
                for c in range(0,placeholders):
                    plot[i].insert(0,'a')
                print("DEBUG: after placeholders", plot[i])

            # places digits now. loop for per lane.
            for k, d in enumerate(plot[i]):
                # once on the 2nd lane it will build the seperator while placing necessary objects
                if i == 1:
                    # wall border
                    print("DEBUG: move and walls")
                    adv_move()
                    turn("right")
                    build_wall()
                    # place object and move
                    turn("left")
                    if d != 'a':
                        adv_put(d,"star")
                    elif d == 0:
                        adv_put(1,"token")
                else:
                    # no wall border, place object and move
                    print("DEBUG: move")
                    adv_move()
                    if d != 'a':
                        adv_put(d,"star")
                    elif d == 0:
                        adv_put(1,"token")

        if i != 2:
            print("DEBUG: reset to next lane")
            move_lane("right")
            # takes in max amount of digits and allows you to reset to proper location ...
            # to place next digits
            adv_move(digit_amount + 1)
            turn("behind")
        else:
            # remainder portion
            # UNTESTED!!
            if (calc[3] > 0):
                print("DEBUG: remainder, place carrot")
                adv_move()
                adv_put(calc[3],"carrot")
            # once we finish our digits move to next position to start new equation
            print("DEBUG: reset to start next")
            adv_move()
            turn("left")
            adv_move(2)
            turn("right")

    return print("Plotted")

## CODE ##

# intro
print("##- Reeborg's Calculator - #")
print("## - - - - - - - - - - - - #")

"""
Create interface to define how much operations you want to calculate and plot
TODO: - create count variable and instead create a calculation object for each equation
      - instead of looping and resetting class object, make multiple class objects and
      just loop plotting instead
"""
# loop will break once user does not want anymore equation
while loop == 1:
    # user input
    c = calculation(input("Enter operation: "), int(input("Enter a number: ")), int(input("Enter a second number: ")))
    # calculate as object
    c.main_p1()
    # provide total and if remainder to user
    print("Total: ", c.total)
    if (c.remainder > 0):
        print("Remainder: ", c.remainder)

    # begin plotting with provided object
    print("Plotting ...")
    main(c.returnValue())

    del c

    # ask the user if you want to place more digits
    choice = input("#- Another Equation? Yes/No")
    if 'y' in choice:
        continue
    elif 'n' in choice:
        loop = 0
        break
    else:
        raise ReeborgError(" ! Invalid response")

# finish code
raise ReeborgOK("##- Finished")
