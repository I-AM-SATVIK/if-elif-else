print("THIS IS THE PROGRAM TO CALCULATE THE PERIMETER, AREA AND VOLUME OF FEW 2D AND 3D SHAPES.")
print("FORMULAE FOR CALCULATING THE PERIMETER, AREA AND VOLUME OF 2D AND 3D SHAPES")
print("PERIMETER OF RECTANGLE=2*(Length+Breath)")
print("PERIMETER OF SQUARE=4*Side")
print("PERIMETER OF CIRCLE=2*pie*Radius")
print("PERIMETER OF SCALENE TRIANGLE=Sum of all Sides of Triangle")
print("PERIMETER OF ISOSCELES TRIANGLE=(2*Measure of one of the two equal side)Third side")
print("PERIMETER OF EQUILATERIAL TRIANGLE=3*Measure of one side")
print("PERIMETER OF RHOMBUS=4*Side")
print("PERIMETER OF PARALLELOGRAM=2*(Sum of Adjacent sides)")
print("AREA OF RECTANGLE=Length*Breath")
print("AREA OF SQUARE=Side*Side")
print("AREA OF CIRCLE=pie*Radius*Radius")
print("AREA OF CYLINDER=(2*pie*Radius*Height)+(2*pie*Height*Height)")
print("AREA OF PARALLELOGRAM=Base*Height")
print("AREA OF TRIANGLE=(Base*Height)/2")
print("AREA OF RHOMBUS=Base*Height")
print("VOLUME OF CUBOID=Length*Breath*Height")
print("VOLUME OF CUBE=Side*Side*Side")
print("VOLUME OF CYLINDER=pie*Radius*Radius*Height")
while True:
    in_=input("Do you want to calculate[Y/N] : ")
    if in_ is "N" or in_ is "n":
        break
    a=str(input("What do you want to calculate {PERIMETER, AREA OR VOLUME}?"))
    if a=="PERIMETER" or a=="Perimeter" or a=="perimeter":
        b=str(input("Enter the name of the shape of which you want to calculate the perimeter [in uppercase letters]="))
        if b=="RECTANGLE" or b=="Rectangle" or b=="rectangle":
            l=float(input("LENGTH="))
            b2=float(input("BREATH="))
            p1=2*(l+b2)
            print("AREA OF RECTANGLE=",p1,"unit")
        elif b=="SQUARE" or b=="Square" or b=="square":
            s=float(input("LENGTH OF ONE SIDE="))
            p2=4*s
            print("PERIMETER OF SQUARE=",p2,"unit")
        elif b=="CIRCLE" or b=="Circle" or b=="circle":
            r=float(input("ENTER THE RADIUS OF CIRCLE [taking pie=22/7]="))
            p3=2*22/7*r
            print("PERIMETER OF CIRCLE=",p3,"unit")
        elif b=="SCALENE TRIANGLE" or b=="Scalene Triangle" or b=="scalene triangle":
            z2=float(input("Enter the measure of the first side of the triangle="))
            z3=float(input("Enter the measure of the second side of the triangle="))
            z4=float(input("Enter the measure of the third side of the triangle="))
            p4=z2+z3+z4
            print("Giving you the perimeter of the Scalene Triangle")
            print("PERIMETER OF THE TRIANGLE=",p4,"unit")
        elif b=="ISOSCELES TRIANGLE" or b=="Isosceles Triangle" or b=="isosceles triangle":
            z5=float(input("Enter the measure of one of the equal side="))
            z6=float(input("Enter the measure of the third side="))
            p6=(2*z5)+z6
            print("Giving you the perimeter of the Isosceles Triangle")
            print("PERIMETER OF THE TRIANGLE=",p6,"unit")
        elif b=="EQUILATERIAL TRIANGLE" or b=="Equilaterial Triangle" or b=="equilaterial triangle":
            z7=float(input("Enter the measure of one of the side of triangle="))
            p8=3*z7
            print("Giving you the perimeter of the Equilaterial triangle")
            print("PERIMETER OF THE TRIANGLE=",p8,"unit")
        elif b=="RHOMBUS" or b=="Rhombus" or b=="rhombus":
            z5=float(input("LENGTH OF ONE SIDE="))
            p5=4*z5
            print("PERIMETER=",p5,"unit")
        elif b=="PARALLELOGRAM" or b=="Parallelogram" or b=="parallelogram":
            m8=float(input("Enter the measure of one side="))
            m9=float(input("Enter the measure of another adjacent side="))
            v9=2*(m8+m9)
            print("PERIMETER OF PARALLELOGRAM=",v9,"unit")
        else:
            print("Unable to calculate sorry!")
    elif a=="AREA" or a=="Area" or a=="area":
        b3=str(input("Enter the name of the shape of which you want to calculate the area [in uppercase letters]="))
        if b3=="RECTANGLE" or b3=="Rectangle" or b3=="rectangle":
            l2=float(input("LENGTH="))
            b4=float(input("BREATH="))
            a1=l2*b4
            print("AREA OF RECTANGLE=",a1,"unit.sq.")
        elif b3=="SQUARE" or b3=="Square" or b3=="square":
            s1=float(input("LENGTH OF SIDE="))
            a2=s1*s1
            print("AREA OF SQUARE=",a2,"unit.sq.")
        elif b3=="CIRCLE" or b3=="Circle" or b3=="circle":
            r1=float(input("ENTER THE RADIUS OF THE CIRCLE [taking pie=22/7]="))
            a3=22/7*r1*r1
            print("AREA OF CIRCLE=",a3,"unit.sq.")
        elif b3=="CYLINDER" or b3=="Cylinder" or b3=="cylinder":
            z=float(input("Enter the radius of the base of the cylinder"))
            x=float(input("Enter the height of the cylinder"))
            a4=(2*22/7*z*x)+(2*22/7*z*z)
            print("Giving you the area of the closed circular cylinder \n ",a4,"unit.sq.")
        elif b3=="TRIANGLE" or b3=="Triangle" or b3=="triangle":
            z1=float(input("Enter the measure of the Base="))
            x1=float(input("Enter the mearure of the Height="))
            a5=(z1*x1)/2
            print("Giving you the area of only isosceles triangle")
            print("AREA OF THE TRIANGLE=",a5,"unit.sq.")
        elif b3=="PARALLELOGRAM" or b3=="Parallelogram" or b3=="parallelogram":
            z8=float(input("Enter the measure of the base of the Parallelogram="))
            z9=float(input("Enter the measure of the height of the Parallelogram="))
            a6=z8*z9
            print("AREA OF THE PARALLELOGRAM=",a6,"unit.sq.")
        elif b3=="RHOMBUS" or b3=="Rhombus" or b3=="rhombus":
            n=float(input("Enter the measure of the base of the Rhombus="))
            n1=float(input("Enter the measure of the height of the Rhombus="))
            a7=n*n1
            print("AREA OF THE RHOMBUS=",a7,"unit.sq.")
        else:
            print("Unable to calculate sorry!")
    elif a=="VOLUME" or a=="Volume" or a=="volume":
        b4=str(input("Enter the name of the shape of which you want to calculate the volume [in uppercase letters]="))
        if b4=="CYLINDER" or b4=="Cylinder" or b4=="cylinder":
            r2=float(input("ENTER THE MEARURE OF THE RADIUS OF THE BASE OF CYLINDER [taking pie=22/7]="))
            h=float(input("ENTER THE MEARURE OF THE HEIGHT OF CYLINDER="))
            b9=22/7*r2*r2*h
            print("THE VOLUME OF THE CYLINDER=",b9,"unit.cube.")
        elif b4=="CUBOID" or b4=="Cuboid" or b4=="cuboid":
            l2=float(input("ENTER THE LENGTH="))
            b5=float(input("ENTER THE BREATH="))
            h1=float(input("ENTER THE HEIGHT="))
            v1=l2*b5*h1
            print("VOLUME OF CUBOID=",v1,"unit,cube.")
        elif b4=="CUBE" or b4=="Cube" or b4=="cube":
            l3=float(input("ENTER THE MEASURE OF ONE SIDE OF THE CUBE="))
            v2=l3*l3*l3
            print("THE VOLUME OF THE CUBE=",v2,"unit.cube.")
        else:
            print("Unable to calculate sorry!")
    else:
        print("Unable to calculate sorry!")
print("#"*30, "Ending Program", "#"*30)

