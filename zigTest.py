# alocating 3.3 skill time blocks for this
# objective is: make zig zag split off and either mirror or follow. and to make it change colour

import time, sys, random
indent = 20  # How many spaces to indent
splitIndent = 0
indent_increasing = True  # Whether the indentation is increasing or not
colour = 37


try:
    def randomEvent(percentChance):
        if random.randint(1,100) >= (100-percentChance):
            return True
        else:
            return False

    while True:  # The main program loop
        if randomEvent(20) and splitIndent != 0 and splitIndent != 20:
            indent_increasing = not indent_increasing

        if randomEvent(5):
            colour = random.randint(31,37)

        print(f'\u001b[{colour}m', end='')

        print(' ' * indent, end='')
        print('****', end='')
        print(' ' * splitIndent, end='')
        print('****', end='')
        print(' ' * indent)

        time.sleep(0.1) # Pause for 1/10th of a second.

        if indent_increasing:
            # Increase the number of spaces:
            indent -= 1
            splitIndent += 2
            if splitIndent == 20:
                # Change direction:
                indent_increasing = False
        else:
            # Decrease the number of spaces:
            indent += 1
            splitIndent -= 2
            if splitIndent == 0:
                # Change direction:
                indent_increasing = True
except KeyboardInterrupt:
    sys.exit()

# I added the random part of it because im the GOAT