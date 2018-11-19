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
think(0)
World("Alone")

items = ["star", "carrot", "token", "strawberry"]
for item in items:
    RUR.give_object_to_robot(item,100)

## VARIABLES ##

## DEFINITIONS ##

# Manipulate turn_left() to make a definiton to turn right, left, or look behind
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
#Create a better move function that allows you to choose the distance Reeborg moves
#default parameter of 1
def adv_move(x=1):
    for i in range(0,x):
        if not wall_in_front():
            move()
        else:
            print(" ! Cannot move any further. Exiting function")
            break
#Allows you to put a specific amount and still specificy amount of carrots
def adv_put(x=1,y="star"):
    if x == 0:
        if y == "star":
            put("token")
        elif y == "carrot":
            put("strawberry")
        else:
            raise ReeborgError(" ! What to substitute zero with?")
    for i in range(0,x):
        put(y)

## - CALCULATING ##
class portion1:
    operators=['add', 'sub', 'mul', 'mod']

    def __init__(self, operator, num1, num2):
        self.operator = operator
        self.num1 = num1
        self.num2 = num2

    #def operation(v):
    #    for i, op in enumerate(operators):
    #        if op in self.operator:
    #            self.operator = operators[i]

    def main(self):
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

# - PLOTTING ##
class portion2:
    def __init__(self, calc):
        self.calc = [calc]

    def digits(self, x):
        count = 0
        while (x > 0):
            x = x // 10
            count = count + 1
        return count

    def split_digits(self, x):
        if (x < 10):
            return [x]
        else:
            return self.split_digits(x // 10) + [x % 10]

    def move_lane(self, x):
        for i in range(0,2):
            adv_move()
            turn(j)

    def main(self):
        plot = {}

        digit_amount = self.digits(max(self.calc))

        for i, v in enumerate(self.calc[:-1]):
                plot = self.split_digits(v)

                placeholder = digit_amount - self.digits(v)
                if (placeholder > 0):
                    for c in range(0,placeholders):
                        plot[i].insert(0,"a")

                for k, d in enumerate(plot[i]):
                    if i:
                        adv_move()
                        turn("right")
                        build_wall()
                        turn("left")
                        adv_put(d,"star")
                    else:
                        adv_move()
                        adv_put(d,"star")

                if i != 2:
                    self.move_lane("right")
                    adv_move(digit_amount + 1)
                    turn("behind")
                else:
                    if (calc[4] > 0):
                        for h, s in enumerate(plot[4]):
                            adv_move()
                            adv_put(d,"carrot")
                    adv_move()
                    turn("left")
                    adv_move(2)
                    turn_right("right")

## CODE ##
print("##- Reeborg's Calculator - #")
print("## - - - - - - - - - - - - #")


p1 = portion1("add",21,12)
p1.main()
calc = p1.returnValue()
print(calc)
p2 = portion2(calc)
p2.main()

"""
count=0
loop=1
while loop == 1:
    p1 = portion1(
        input("Enter operation: "),
        int(input("Enter a number: ")),
        int(input("Enter a second number: "))
        )
    p1.main()
    print("Total: ", p1.total)
    if (p1.remainder > 0):
        print("Remainder: ", p1.remainder)

    print("Plotting ...")
    p2=portion2(
        p1.num1,
        p1.num2,
        p1.total,
        p1.remainder,
        )
    p2.main()

    del p1
    del p2

    choice = input("#- Another Equation? Yes/No")
    if 'y' in choice:
        count = count + 1
        continue
    elif 'n' in choice:
        loop = 0
        break
    else:
        raise ReeborgError(" ! Invalid response")
"""

raise ReeborgOK("##- Finished")
