# The program is going to show the amount of bugs you have collected for each day.
# For day one you only collected one. For the next four days you collected two each day.
# In the end it will show you how much you collected in those five days.
# 10-14-2019
# CTI-110 P4T2 - Bug Collector
# Alexis Navarro
#
total = 0 

for day in range(1, 6):
    print('Enter the bugs collected on day', day)

    bugs = int(input())
    total += bugs


print('You collected a total of', total, 'bugs.')
