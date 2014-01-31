#!/usr/bin/python
#
#   Cycle through your different Gravatar.com images, changing your default avatar on interval.
#
#   Usage:
#
#       cycle-gravatars.py -e "<emailaddress>" -p "<password>" -d <delayinseconds>
#   or
#       cycle-gravatars.py --email="<emailaddress>" -password="<password>" -delay=<delayinseconds>
#
#   for help:
#       cycle-gravatars.py -h
#
__author__ = 'Blake Caldwell http://blakecaldwell.net'

import sys, getopt
import time
from pprint import pprint
import itertools
from libgravatar import GravatarXMLRPC

# Show the help, then exit with the input code
def show_help(exit_code):
    print 'cycle-gravatars.py -e "<emailaddress>" -p <password> -d <delayinseconds>'
    sys.exit(exit_code)

# Given email, password, and a delay (in seconds) between images, connect to Gravatar.com
# and loop through the account's avatar images.
def cycle_all_images(email, password, delay):
    # Get all of the images from Gravatar
    g = GravatarXMLRPC(email, password=password)

    # get all images for this account
    user_images = g.userimages()

    # make sure we have something to do
    if len(user_images) < 2:
        print "You need at least two Gravatar images to cycle through."
        exit(2)

    print "Cycling through each of your", len(user_images), "Gravatar.com images every", delay, "seconds."

    # loop over the images forever
    for user_image in itertools.cycle(user_images):
        print "Setting image to", user_image
        pprint(g._call("useUserimage", params={'userimage' : user_image, 'addresses' : [email]}))
        time.sleep(delay)


# Main - get all arguments from input, and cycle through user's Gravatars
def main(argv):
    email = ''
    password = ''
    delay = 300     # 5 minutes default

    # parse arguments
    try:
        opts, args = getopt.getopt(argv, "he:p:d:",["email=", "password=", "delay="])
    except getopt.GetoptError:
        show_help(2)

    # interpret arguments
    for opt, arg in opts:
        if opt == '-h':
            show_help(0)
        elif opt in ("-e", "--email"):
            email = arg
        elif opt in ("-p", "--password"):
            password = arg
        elif opt in ("-d", "--delay"):
            delay = float(arg)

    # make sure we have the required params
    if not all((email, password, delay)):
        show_help(2)

    # go!
    cycle_all_images(email, password, delay)


if __name__ == "__main__":
    main(sys.argv[1:])
