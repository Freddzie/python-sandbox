# alocating 3.3 skill time blocks for this
# objective is: make zig zag split off and either mirror or follow. and to make it change colour
# result: colour change was easy, splitting it mirrored was very hard, i jjust followed my brain down rabbit holes which didnt work and then
# result2: had to backtrack and then try again. this felt not efficient and stupid and i was wasting time, so i stepped back, drew a plan on
# result3: how to make the mirror work indipendantly from the main block and it worked, and i accidentaly made it work with the fixed zigzag
# result4: aswell so it was a big success. if i plan how to conbine them im sure i could do it into one system now but i have no time left

# Architectural Insight: To make two elements truly independent, they each need their own complete set of "state" variables (e.g., indent_A, direction_A, indent_B, direction_B). Trying to control both with one indent_increasing flag is messy and limits what I can do.

# Technical Insight (The "Aha!" Moment): The most interesting discovery was a hidden property of Python strings. Multiplying a string by a negative or zero value (e.g., ' ' * -5) results in an empty string. This is why the zigzags appeared to "join" when splitIndent was less than or equal to 0. This is a powerful, non-obvious behavior of the language itself.

# Process Insight: My initial "dive-in" approach was slow and led to backtracking. I made much faster progress once I stopped and wrote a simple pseudocode plan. This confirms that the "Blueprint Before Building" protocol is more efficient.

import time, sys, random
indent = 0  # How many spaces to indent
splitIndent = 0
splitMode = True
indent_increasing = True  # Whether the indentation is increasing or not
colour = 37
print("BEGIN")


try:
    def randomEvent(percentChance):
        if random.randint(1,100) >= (100-percentChance):
            return True
        else:
            return False

    while True:  # The main program loop
        if randomEvent(20):
            indent_increasing = not indent_increasing

        if randomEvent(5):
            colour = random.randint(31,37)

        if randomEvent(1):
            splitMode = True

        print(f'\u001b[{colour}m', end='')
        print(' ' * indent, end='')
        print('****', end='')
        print(' ' * (splitIndent*2), end='')
        print('****')

        time.sleep(0.1) # Pause for 1/10th of a second.

        if splitMode:
            if indent_increasing:
                # Increase the number of spaces:
                indent = indent - 1
                splitIndent = splitIndent + 1
                if indent >= 20 or splitIndent >= 10:
                    # Change direction:
                    indent_increasing = False
            else:
                # Decrease the number of spaces:
                indent = indent + 1
                splitIndent = splitIndent - 1
                if indent <= 0 or splitIndent <= 10:
                    # Change direction:
                    indent_increasing = True
            
        if indent_increasing:
            # Increase the number of spaces:
            indent = indent + 1
            if indent >= 20:
                # Change direction:
                indent_increasing = False
        else:
            # Decrease the number of spaces:
            indent = indent - 1
            if indent <= 0:
                # Change direction:
                indent_increasing = True
        # print(indent)
except KeyboardInterrupt:
    sys.exit()

# I added the random part of it because im the GOAT