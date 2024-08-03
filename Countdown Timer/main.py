import time

def countdown(t):
    """
    Starts a countdown from the given time in seconds.

    Args:
        t (int): Time in seconds.

    Example:
        >>> countdown(10)
        # Starts a countdown from 10 seconds

    Note:
        The countdown is displayed in the format MM:SS and updates in real-time.
    """
    while t:
        if t > 0:
            if t <=3600:
                mins, secs = divmod(t, 60)
                timer = '{:02d}:{:02d}'.format(mins, secs)
            elif t < 86400:
                hours, remainder = divmod(t, 3600)
                mins, secs = divmod(remainder, 60)
                timer = '{:02d}:{:02d}:{:02d}'.format(hours, mins, secs)
            else:
                days, remainder = divmod(t, 86400)
                hours, remainder = divmod(remainder, 3600)
                mins, secs = divmod(remainder, 60)
                timer = '{:02d}:{:02d}:{:02d}:{:02d}'.format(days, hours, mins, secs)
            print(timer, end="\r")
            time.sleep(1)
            t -= 1
        else:
            print('Enter a value greater than zero!')
    print('Time Up!!')

''' Ensures that the code only runs when the script is executed directly,
    not when it's imported as a module. '''
if __name__ == "__main__":
    t = int(input("Enter the time in seconds: "))
    countdown(t)