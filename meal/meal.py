def main():

# Get time from user
answer = input("What time is it?" )

# Convert Function
time = convert(answer)

# Breakfast between 7:00 and 8:00
if 


# lunch between 12:00 and 13:00



# dinner between 18:00 and 19:00


def convert(time):

# Get hour and minute
hours, minutes = time.split(":")

# Convert time to float
new_minute = float(minutes)/ 60

# Return result
return float(hours) + new_minute

if _name_ == "_main_":

    main()
