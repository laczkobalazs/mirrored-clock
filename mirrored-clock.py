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
    time_parts = time_from_mirror.split(":")    # Assuming the input time is a string (as it is expected in the output) it is split into 2 parts divided by the ":"
    hours = time_parts[0]
    mins = time_parts[1]

    if mins == "00":                            # An edge case the the clock shows exact hours
        real_hours = 12 - int(hours)
        real_mins = int(mins)
    else:
        real_hours = 11 - int(hours)
        real_mins = 60 - int(mins)
    print(f"{real_hours:02d}:{real_mins:02d}")
    return f"{real_hours:02d}:{real_mins:02d}"

def main():
    mirrored_clock("02:21") # The real time should be 09:39
    mirrored_clock("01:00") # The real time should be 11:00
    mirrored_clock("04:03") # The real time should be 07:57
    mirrored_clock("10:59") # The real time should be 01:01
    mirrored_clock("11:44") # The real time should be 12:26
    mirrored_clock("12:00") # The real time should be 12:00
    mirrored_clock("12:59") # The real time should be 11:01

if __name__ == '__main__':
    main()
