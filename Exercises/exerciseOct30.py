# import turtle
# import colorsys
# t = turtle.Turtle()
# s = turtle.Screen()
# s.bgcolor('purple')
# t.speed(0)
# n = 500
# h = 0
# for all in range(280):
#     c = colorsys.hsv_to_rgb(h, 0.5, 1)
#     t.color(c)
#     h = h + 1/n
#     t.forward(all * 2)
#     t.left(100)
# turtle.done()


powers = [3, 8, 9, 7] 
   
mini, maxi = 0, 0
   
for power in powers: 
    if mini == 0 and maxi == 0: 
        mini, maxi = powers[0], powers[0] 
        print(mini, maxi) 
    else: 
        mini = min(mini, power) 
        maxi = max(maxi, power) 
        print(mini, maxi) 