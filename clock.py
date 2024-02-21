# I sort of made a clock

def clock():
    for hours in range(0, 24):
        for minutes in range(0, 60):
            for seconds in range(0, 60):
                print(hours, minutes, seconds)

clock()