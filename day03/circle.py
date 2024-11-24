import argparse
import math

# Set up parser

parser=argparse.ArgumentParser()
parser.add_argument('--radius',help='radius of a circle (positive number) ',required=True, type=float)

args = parser.parse_args()

# Main code

def circle_area_circumference(radius):
    area = math.pi*radius**2
    circumference = 2*math.pi*radius
    return area, circumference

if args.radius <=0 :
    print ('error, radius must be a positive number')
else:
    area,circumference=circle_area_circumference(args.radius)
    print("Area:", area), print("circumference:", circumference)
