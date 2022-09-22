""" 
Coding challenge!

Peter can see a clock in the mirror from the place he sits in the office. When he saw the clock shows 12:22. He knows that the time is 11:38
In the same manner:

05:25 --> 06:35
01:50 --> 10:10
11:58 --> 12:02
12:01 --> 11:59

Please create an application which solves the problem. 
Return the real time as a string.
Consider hours to be between 1 <= hour < 13.
So there is no 00:20, instead it is 12:20.
There is no 13:20, instead it is 01:20.
Please don’t use Bash. 
"""

def mirrored_clock(time_from_mirror):
    time_parts = time_from_mirror.split(":") # Assuming the input time is a string (as it is expected in the output) it is split into 2 parts divided by the ":"
    hours = time_parts[0]
    mins = time_parts[1]

    if mins == "00": 
        real_hours = str(12 - int(hours))
        real_mins = mins
    else:
        real_hours = str(11 - int(hours))
        real_mins = str(60 - int(mins))
    return f"{real_hours}:{real_mins}"
