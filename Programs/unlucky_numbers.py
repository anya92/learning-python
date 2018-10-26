for n in range(1, 21):
    if n == 4 or n == 13:
        state = 'unlucky'
    elif n % 2 == 0:
        state = 'even'
    else:
        state = 'odd'
    print(f"{n} is {state}")
