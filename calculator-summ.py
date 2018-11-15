"""
Title: Calculator Reeborg's world
Date: Nov. 7, 2018
Author: Yuvraj Chohan

2 Portions - Calculating, Plotting
Keep plotting portions as string to ensure leading zeros

a > b - a is greater than
a < b - a is smaller than

elif - else if - make it check another condition if last one failed
list = allows you to store multiple values
"""
__author__  = "Yuvraj Chohan"

## VARIABLES ## -------------
# calculating
# num1 num2 total remainder
calc=[]
plot_calc={}

# plotting portion

# amount we have to step back
line=0
# digit var to get placeholders
adigits=0

## DEFINITIONS ##  -------------

# Calculating Portion
# Create functions to add, subtract, multiply, divide appropiately in Reeborg's world
# TODO: calculate(x,y,z) and x is add, subtract, multiply, divide

"""
# Subtraction   # Addition  # Multiplication    # Dividing & Remainders
#    x          #    x      #    x              #     x
#  - y          #  + y      #  * y              #  // y
#  ---          #  ---      #  ---              #  ----
#    z          #   z       #   z               #     z  r

operator = v
"""
def calculate(v,x,y):
    # prep var
    r=0
    print("Input:", x, "and", y)
    print("Operation:", v)
    if "add" in v:
        z = x + y
    elif "sub" in v:
        z = x - y
        # check for negatives
        if (z < 0):
            # do not allow subtracting larger amounts from smaller amounts
            # as per rubric and limitations on what can be done during mapping
            print(" ! You're only allowed to subtract a smaller number")
    elif "mul" in v:
        z = x * y
    elif "div":
        z = x // y
        r = x % y
    elif "mod" in v:
        z = x % y
    else:
        print(" ! Unknown operation")
    result=[x, y, z, r, v]
    return result
"""
Determines amount of digit places by dividing the int by 10 until
it reaches single-digits and you get 0. That way your while loop exits
and you get your value needed for the line that seperates the total and rest.
via integers only and modulation as per rubric.
"""
def digits(x):
    count = 0
    while (x > 0):
        x = x // 10
        count = count + 1
    return count
# similiar means above but used to split digits and place them in order
def split_digs(x):
    if (x < 10):
        return [x]
    else:
        return split_digs(x // 10) + [x % 10]

# Plotting portion
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
#Create a better move function that allows you to choose the distance Reeborg moves
#default parameter of 1
def adv_move(x=1):
    for i in range(0,x):
        if not wall_in_front():
            move()
        else:
            print(" ! Cannot move any further")
            break
#Allows you to put a specific amount and still specificy amount of carrots
def adv_put(x=1,y="star"):
    for i in range(0,x):
        # skip if space
        if x == (0,"a"):
            continue
        else:
            put(y)
# move down and orientate correctly to finish equation
def move_lane(j):
    adv_move()
    turn(j)
    adv_move()
    turn(j)

## CODE ##  -------------
# Setup
think(0)
#
calc=calculate("add",21,12)

# Pickup bunch of stars and carrots to be able to plot and start operation
# think of it as he already had it.
turn("left")
while object_here():
    take("star")
adv_move()
while object_here():
    take("carrot")
# Starting pos - (1,10) cords - cuz maybe multi-step equation means need room
adv_move(8)
turn("right")

# enumerate used as counter for this list - allows me to use value and iterative
# determine amount of digits in order to space correctly
for i, value in enumerate(calc[:-2]):
    if (value > adigits):
        adigits = digits(calc[i])
# define line var
line = adigits + 1
# create dictionary for plotting except for remainder
for i, value in enumerate(calc[:-2]):
    plot_calc[i]=split_digs(calc[i])
    # create placeholders in each list to space evenly
    # can't and shouldnt be done in calculating portion as they are integers
    new_digits=digits(calc[i])
    placeholders=0
    if (new_digits < adigits):
        placeholders = adigits - placeholders
        for c in range(0,placeholders):
            plot_calc[i] = [0] + plot_calc[i]
    for k, __ in enumerate(plot_calc[i]):
        # builds wall everytime it plots. abandon wall length
        if i == 1:
            adv_move()
            turn("right")
            build_wall()
            turn("left")
            adv_put(plot_calc[i][k],"star")
        else:
            adv_move()
            adv_put(plot_calc[i][k],"star")
    # no need bcz only 3 parts/lanes
    if i != 2:
        move_lane("right")
        adv_move(line)
        turn("behind")
    else:
        # modulus/remainder portion
        if i == 4 and (plot_calc[i] > 0):
            for k, __ in enumerate(plot_calc[i]):
                adv_move()
                adv_put(plot_calc[i][k],"carrot")
        adv_move()
        turn("left")
        adv_move(2)
        turn("right")
