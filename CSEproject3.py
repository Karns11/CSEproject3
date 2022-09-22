    ###########################################################
    #
    #  CSE 231 project #3
    #
    #  Algorithm.
    #    prompt for 3 triangle side lengths.
    #    calculate degree of angles, in radians and print results.
    #    convert radians to degrees and print results.
    #    calculate perimeter of given triangle and print results.
    #    calculate area of given triangle and print results.
    #    determine the types of triangles and print results.
    #    if given lenths are not a valid triangle, display that.
    #    display closing message
    ###########################################################

import math

BANNER = '''

╭━━━━╮╱╱╱╱╱╱╱╱╱╱╭╮
┃╭╮╭╮┃╱╱╱╱╱╱╱╱╱╱┃┃
╰╯┃┃┣┻┳┳━━┳━╮╭━━┫┃╭━━╮
╱╱┃┃┃╭╋┫╭╮┃╭╮┫╭╮┃┃┃┃━┫
╱╱┃┃┃┃┃┃╭╮┃┃┃┃╰╯┃╰┫┃━┫
╱╱╰╯╰╯╰┻╯╰┻╯╰┻━╮┣━┻━━╯
╱╱╱╱╱╱╱╱╱╱╱╱╱╭━╯┃
╱╱╱╱╱╱╱╱╱╱╱╱╱╰━━╯
'''

print(BANNER)
print()

#ask user if they'd like to process a triangle
request = input("Do you wish to process a triangle (Y or N)?  ")

#covert to lowercase
request_lower = request.lower()

#decalre a varible to count valid triangles
num_triangles = 0

#if user would like to proceed, run while loop containing calculations
while request_lower == 'y':
    #prompt user for 3 side lengths
    ab_length = float(input("\nEnter length of side AB: "))
    bc_length = float(input("\nEnter length of side BC: "))
    ca_length = float(input("\nEnter length of side CA: \n"))
    if (ab_length + bc_length) > ca_length: #If a valid triangle:
        num_triangles += 1 #add 1 to valid count
        #calculate angles of the 3 sides, in radians
        rad_angle_ab = math.acos(((ab_length**2)+(ca_length**2)-(bc_length**2))/(2*ab_length*ca_length))
        rad_angle_bc = math.acos(((ab_length**2)+(bc_length**2)-(ca_length**2))/(2*ab_length*bc_length))
        rad_angle_ca = math.acos(((bc_length**2)+(ca_length**2)-(ab_length**2))/(2*bc_length*ca_length))
        #calculate angles of the 3 sides, in degrees
        deg_angle_ab = (rad_angle_ab * 180) / math.pi
        deg_angle_bc = (rad_angle_bc * 180) / math.pi
        deg_angle_ca = (rad_angle_ca * 180) / math.pi
        #s = half of perimeter, used in area calculation
        s = (.5) * (ab_length + bc_length + ca_length)
        #calculate area
        area_triangle = math.sqrt((s)*((s) - (ab_length)) * ((s) - (bc_length)) * ((s) - (ca_length)))
        #perimeter = s*2
        perimeter_triangle = s * 2
        print("\n  Valid Triangle\n")
        print("  Triangle sides:")
        print("    Length of side AB:", ab_length)
        print("    Length of side BC:", bc_length)
        print("    Length of side CA:", ca_length)
        print("\n  Degree measure of interior angles:")
        print("    Angle A:", round(deg_angle_ab, 1))
        print("    Angle B:", round(deg_angle_bc, 1))
        print("    Angle C:", round(deg_angle_ca, 1))
        print("\n  Radian measure of interior angles:")
        print("    Angle A:", round(rad_angle_ab, 1))
        print("    Angle B:", round(rad_angle_bc, 1))
        print("    Angle C:", round(rad_angle_ca, 1))
        print("\n  Perimeter and Area of triangle:")
        print("    Perimeter of triangle:", round(perimeter_triangle, 1))
        print("    Area of triangle:", round(area_triangle, 1))
        print("\n  Types of triangle:")
        if ab_length == bc_length or ab_length == ca_length or bc_length == ca_length:
            print("    Isosceles Triangle")
            if deg_angle_ab > 90 or deg_angle_bc > 90 or deg_angle_ca > 90:
                print("    Obtuse Triangle")
            if ab_length == bc_length and ab_length == ca_length:
                print("    Equilateral Triangle")
            if deg_angle_ab != 90 or deg_angle_bc != 90 or deg_angle_ca != 90:
                print("    Oblique Triangle")
        elif ab_length == bc_length and ab_length == ca_length:
            print("    Equilateral Triangle")
        elif ab_length != bc_length or ab_length != ca_length or bc_length != ca_length:
            print("    Scalene Triangle")
            if deg_angle_ab == 90 or deg_angle_bc == 90 or deg_angle_ca == 90:
                print("    Right Triangle")
            if deg_angle_ab != 90 and deg_angle_bc != 90 and deg_angle_ca != 90:
                print("    Oblique Triangle")
            if deg_angle_ab > 90 or deg_angle_bc > 90 or deg_angle_ca > 90:
                print("    Obtuse Triangle")
        elif deg_angle_ab == 90 or deg_angle_bc == 90 or deg_angle_ca == 90:
            print("    Right Triangle")
        elif deg_angle_ab != 90 and deg_angle_bc != 90 and deg_angle_ca != 90:
            print("    Oblique Triangle")
        elif deg_angle_ab > 90 or deg_angle_bc > 90 or deg_angle_ca > 90:
            print("    Obtuse Triangle")
    elif (ab_length + bc_length) == ca_length:
        print("\n  Degenerate Triangle")
    else:
        print("\n  Not a Triangle")
    request = input("\nDo you wish to process another triangle? (Y or N) ")
    request_lower = request.lower()
print("\nNumber of valid triangles:", num_triangles)