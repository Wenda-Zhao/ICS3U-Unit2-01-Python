#!/usr/bin/env python3

# Created by Wenda Zhao
# Created on Nov 2020
# This program calculates the area and perimeter of a circle
#     with radius 15mm

import math


def main():
    # This function calculates the area and perimeter
    print("if a circle has a radius of 15mm:")
    print("")
    print("Area is {}mm^2".format(math.pi*15**2))
    print("Perimeter is {}mm".format(2*math.pi*15))


if __name__ == "__main__":
    main()
