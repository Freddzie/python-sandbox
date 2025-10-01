# alocating 3.3 skill time blocks for this
# objective is: make zig zag split off and either mirror or follow. and to make it change colour
result: colour change was easy, splitting it mirrored was very hard, i jjust followed my brain down rabbit holes which didnt work and then
        had to backtrack and then try again. this felt not efficient and stupid and i was wasting time, so i stepped back, drew a plan on
        how to make the mirror work indipendantly from the main block and it worked, and i accidentaly made it work with the fixed zigzag
        aswell so it was a big success. if i plan how to conbine them im sure i could do it into one system now but i have no time left

# Architectural Insight: To make two elements truly independent, they each need their own complete set of "state" variables (e.g., indent_A, direction_A, indent_B, direction_B). Trying to control both with one indent_increasing flag is messy and limits what I can do.

# Technical Insight (The "Aha!" Moment): The most interesting discovery was a hidden property of Python strings. Multiplying a string by a negative or zero value (e.g., ' ' * -5) results in an empty string. This is why the zigzags appeared to "join" when splitIndent was less than or equal to 0. This is a powerful, non-obvious behavior of the language itself.

# Process Insight: My initial "dive-in" approach was slow and led to backtracking. I made much faster progress once I stopped and wrote a simple pseudocode plan. This confirms that the "Blueprint Before Building" protocol is more efficient.
