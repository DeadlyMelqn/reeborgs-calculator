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
"""

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

    def __init__(self, operator, num1, num2):
        self.operator = operator
        self.num1 = num1
        self.num2 = num2

    #def operation(v):
    #    for i, op in enumerate(operators):
    #        if op in self.operator:
    #            self.operator = operators[i]

    def main_p1(self):
        self.total = 0
        self.remainder = 0
        if "add" in self.operator:
            self.total = self.num1 + self.num2
        elif "sub" in self.operator:
            self.total = self.num1 - self.num2
            if (self.total < 0):
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
        return [self.num1, self.num2, self.total, self.remainder]

# Functions that better enable and improve reeborg's ability to move and etc
#manipulate turn_left() to make a definiton to turn right, left, or look behind
def turn(x):
    if x == "left" or not x:
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
    if x == '0':
        if y == "star":
            put("token")
        elif y == "carrot":
            put("strawberry")
        else:
            raise ReeborgError(" ! What to substitute zero with?")
    else:
        for i in range(0,x):
            put(y)
#move down appropiatly and reset to plot rest of equation
# TODO: remove
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

def main(x):
    calc = x
    plot = {}

    digit_amount = digits(max(calc))
    print("DEBUG: digit_amount is %d" % (digit_amount))

    for i, value in enumerate(calc[:-1]):
        print("DEBUG: i is %d and value is %d" % (i, value))
        plot[i] = split_digits(value)
        print("DEBUG: before placeholders", plot)

        if i != 3:
            if (digit_amount > digits(value)):
                placeholders = digit_amount - digits(value)
                print("DEBUG: placeholders is %d" % (placeholders))
                for c in range(0,placeholders):
                    plot[i].insert(0,'a')
                print("DEBUG: after placeholders", plot)

            for k, d in enumerate(plot[i]):
                print("DEBUG: k is %d and d is %d" % (i, value))
                if i == 1:
                    adv_move()
                    turn("right")
                    build_wall()
                    turn("left")
                    adv_put(d,"star")
                else:
                    adv_move()
                    adv_put(d,"star")

        if i != 2:
            move_lane("right")
            adv_move(digit_amount + 1)
            turn("behind")
        else:
            if i == 3 and (value > 0):
                for k, d in enumerate(plot[i]):
                    adv_move()
                    adv_put(d,"carrot")
            adv_move()
            turn("left")
            adv_move(2)
            turn("right")

    print("DEBUG: Finished nested loop")

## CODE ##
print("##- Reeborg's Calculator - #")
print("## - - - - - - - - - - - - #")

"""
Create interface to define how much operations you want to calculate and plot
TODO: - create count variable and instead create a calculation object for each equation
      - instead of looping and resetting class object, make multiple class objects and
      just loop plotting instead
"""
while loop == 1:
    c = calculation(
        input("Enter operation: "),
        int(input("Enter a number: ")),
        int(input("Enter a second number: "))
        )
    c.main_p1()
    print("Total: ", c.total)
    if (c.remainder > 0):
        print("Remainder: ", c.remainder)

    print("Plotting ...")
    main(c.returnValue())

    del c

    choice = input("#- Another Equation? Yes/No")
    if 'y' in choice:
        continue
    elif 'n' in choice:
        loop = 0
        break
    else:
        raise ReeborgError(" ! Invalid response")

raise ReeborgOK("##- Finished")
