k = [4]
d = [5]
b = 5
def getMoneySpent(keyboards, drives, b):
    max = 0 # Starting counter
    for keyboard in keyboards: # For each item in keyboard array
        for usb in drives: # Check each item in usb array for following condition
            # if keyboard cost + usb cost is less than or equal to budget
            if keyboard + usb <= b and keyboard + usb > max: # and if that sum is less than current max
                max = keyboard + usb # assign sum to max
    if max == 0: # If nothing was under budget, thus max didn't change, return -1
        return -1
    else:
        return max # return max amount that could be spent


print(getMoneySpent(k, d, b))
