PI=3.14
shape = input('Choose a shape(triangle,rectangle,circle):')
while shape:
    if shape.strip() not in ("triangle", "rectangle", "circle"):
        print('Unknown shape')
    if shape.strip() == "triangle":
        base = float(input("Give base of the triangle: "))
        height = float(input("Give height of the triangle: "))
        print(f"The area is {0.5*base*height:.5f}")
    if shape.strip() == "rectangle":
        width = float(input("Give width of the rectangle: "))
        height = float(input('Give height of the rectangle: '))
        print(f"The area is {width * height:.5f}")
    if shape.strip() == "circle":
        radius=float(input('Give radius of the circle: '))
        print(f"The area is {PI*radius**2:.5f}")
    shape = input('Choose a shape(triangle,rectangle,circle): ')

#