# /usr/bin/env python3

# Created by: Liam Fletcher
# Created on: Oct 2021
# This program asks the user for the radius and height
# to calculate and output the volume of a cone

import math


def volume_cone(radius, height):
    # calculate volume

    # process
    volume = round((1 / 3) * math.pi * radius * radius * height)

    return volume


def main():
    # this function calls the precedent function

    # input & output
    user_radius = input("Enter the radius of the cone (mm): ")
    user_height = input("Enter the height of the cone (mm): ")

    try:
        user_radius_int = int(user_radius)
        user_height_int = int(user_height)

        if user_radius_int < 0:
            print("")
            print("That is an invalid number.")
        if user_height_int < 0:
            print("")
            print("That is an invalid number.")

        else:
            calculate_volume = volume_cone(
                radius=user_radius_int,
                height=user_height_int,
            )  # call function
            print("")
            print("The volume of your cone is {0} mm³".format(calculate_volume))

    except Exception:
        print("")
        print("That is an invalid number.")

    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
