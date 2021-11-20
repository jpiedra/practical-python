# bounce.py
#
# Exercise 1.5

# constants
DROPOFF = 3 / 5

# counters
height = 100
bounce_num = 0

# simulate each bounce, adjusting the height/num of bounces each time
while bounce_num < 10:
    # calculate the new height, then print it
    height = height * DROPOFF
    print( round(height, 4) )
    # update number of bounces
    bounce_num = bounce_num + 1