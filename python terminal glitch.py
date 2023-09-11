#input() #for some reason, double clicking this .py results in a garbled terminal unless you do this...?

def discrete_linear_convolution(x,y):
    sums = {}
    for ix in range(len(x)):
        for iy in range(len(y)):
            sums[ix+iy] = sums.get(ix+iy, 0) + x[ix]*y[iy]
    return tuple(x for x in sums.values()) #convert to tuple before returning

def fairdie(sides): #for example, for 6 sides this will return (0, 1/6, 1/6, 1/6...)
    return 0.0, *tuple(1/sides for _ in range(sides))

def printlist(x): #makes it pretty
    for i in range(len(x)):
        print(str(i).ljust(5), str(x[i]))

print("Two fair dice:")
pairs = discrete_linear_convolution(fairdie(6), fairdie(6))
printlist(pairs) #print a pretty table of values
print("Sum: ", sum(pairs)) #this will have a little floating-point error but oh well

#we can use discrete convolutions to make a recursive function that will find the probabilities for any number of die, of any size, with any weighting
def find_sum_dice(*dice):
    if(len(dice) == 2): #if this is the final recursion step
        return discrete_linear_convolution(dice[0], dice[1])
    else:
        return discrete_linear_convolution(find_sum_dice(*dice[:-1]), dice[-1]) #recurse over the dice until we're left with (((a*b)*c)*d)*e

print("\n\n\nMultiple dice: ")
unfair_die = (0.0, 0.2, 0.3, 0.3, 0.1, 0.05, 0.05)


dice = (fairdie(6), fairdie(6), fairdie(6)) #change this to whatever you want
printlist(find_sum_dice(*dice))

input()