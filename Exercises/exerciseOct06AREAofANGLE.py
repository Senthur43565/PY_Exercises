# initializing function to create area of all
# calculate area of rectangle
def calculate_rectangle_area(x, y):
    return x*y
#  calculate area of circle


def calculate_circle_area(z):
    return 3.14159 * (z ** 2)
# calculate area of triangle


def calculate_triangle_area(x, y):
    return 0.5 * x * y


while True:
    print("choose a shape to calculate area..")
    print("1.rectangle")
    print("2.circle")
    print("3.triangle")

    user_choice = input("Enter your choice 1|2|3|4:\n")

    if user_choice == "1":
        length = float(input("Enter length value:\n"))
        width = float(input("Enter Width value:\n"))
        rectangle = calculate_rectangle_area(length, width)
        print(rectangle)
    elif user_choice == "2":
        radius = float(input("Enter radius value:\n"))
        circle = calculate_circle_area(radius)
        print(circle)
    elif user_choice == "3":
        base = float(input("Enter length value:\n"))
        height = float(input("Enter Width value:\n"))
        triangle = calculate_triangle_area(base, height)
        print(triangle)
    else:
        print("Yhank you!")
print("😍")
   
