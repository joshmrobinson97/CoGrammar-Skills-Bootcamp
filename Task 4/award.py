""" award.py psuedo code
ask for three seperate inputs for the time of each event completion in minutes
store each value as separate values
combine all three to get total time
display the total time and the time for each segment

create time range within 0-100 minutes that'll display appropriate award
create time range within 101-105 minutes that'll display appropriate award
create time range within 106-110 minutes that'll display appropriate award
create time range above 111 minutes that'll display no award

depending on original time, call upon the relevant award
print award with criteria
"""

swim_time = int(input("Please enter the time for completing the swimming leg of your triathalon in minutes: "))
bike_time = int(input("Please enter the time for completing the cycling leg of your triathalon in minutes: "))
run_time = int(input("Please enter the time for completing the running leg of your triathalon in minutes: "))

total_time = swim_time + bike_time + run_time # calculating total triathalon time

print(f"\n\nYour times are: \nSwimming time: {swim_time} minutes.\nCycling time: {bike_time} minutes.\nRunning time: {run_time} minutes.")
print(f"Total triathalon time: {total_time} minutes")

if total_time <= 0:
    print("\n\nPlease enter a real race time")
if total_time > 0 and total_time <= 100:
    print("\n\nYou are within the qualifying time. Congratulations, you are awarded the Provincial Colours!")
if total_time >= 101 and total_time <= 105:
    print("\n\nYou are within 5 minutes of the qualifying time. You have been awarded with the Provincial Half Colours! Congratulations!")
if total_time >= 106 and total_time <= 110:
    print("\n\nYou are within 10 minutes of the qualifying time and thus have been awarded the Provincial Scroll. Well done!")
elif total_time >= 111:
    print("\n\nDue to finishing over 10 minutes off the qualifying time, you will not receive an award. Better luck next time!")
 
