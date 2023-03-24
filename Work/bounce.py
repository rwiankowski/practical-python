# bounce.py
#
# Exercise 1.5

height = 100
bounce_ratio = 3/5

for bounce in range(1, 11):
    height *= bounce_ratio
    print(f'{bounce} {height:0.2f}')