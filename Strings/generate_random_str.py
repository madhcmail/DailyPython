import random
import string
import time

def gen_random_str():
    possible_chars = string.ascii_lowercase+string.ascii_uppercase+string.digits+'., !?;:'
   
    t = "geek"
    iteration = 0
    found = False
    attemptThis = ''.join(random.choice(possible_chars) for n in range(len(t)))

    attemptNext = ''

    while found == False:
        print(attemptThis)

        attemptNext = ''
        found = True

        for i in range(len(t)):
            if attemptThis[i] != t[i]:
                found = False
                attemptNext += random.choice(possible_chars)
            else:
                attemptNext += t[i]
        iteration += 1
        attemptThis = attemptNext
        time.sleep(0.1)

    return f"Target Matched after {iteration} Iterations"

print(gen_random_str())