"""
   Filename: oo_resale_shop.py
Description: Using OOP to create a resaleShop class
     Author: Marybella Martinez
       Date: 18 April 2023
"""

from computer import *
class ResaleShop:
    """This class can buy,sell, and refurbish computers and print out the shops inventory"""
    # What attributes will it need?
    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self):
        self.inventory = []

    # What methods will you need?
    """adds a computer to the inventory list"""
    def buy(self,computer: Computer):
        self.inventory.append(computer)

    """removes a computer from the inventory list, prints an error if that computer is not in the inventory"""
    def sell(self,computer):
        if computer in self.inventory:
            self.inventory.remove(computer)
        else:
            print("Sorry, we do not have this computer.")

    """makes new price for computer and finds if there is a new os system """
    def refurbish(self,computer,new_os):
        if computer in self.inventory:
            if(computer.year_made < 2000):
                computer.price = 0
            elif(computer.year_made < 2012):
                computer.price = 250
            elif(computer.year_made < 2018):
                computer.price = 500
            else:
                computer.price = 1000
            if new_os is not None:
                computer.operating_system = new_os
        else:
            "This computer is not in out inventory."

    """prints all the items in the inventory,if it is empty then prints error"""
    def printInv(self):
        if len(self.inventory):
            print("Inventory: ")
            for computer in self.inventory:
                computer.printDetails()
        else:
            print("Inventory is empty.")

def main():
    co = Computer("Mac Pro (Late 2013)","3.5 GHc 6-Core Intel Xeon E5",1024, 64,"macOS Big Sur", 2013, 1500)
    co2 = Computer("Lenovo PC","3.5 GHc 7-Core Intel",1024, 82,"LenovoOS", 2022, 1500)

    shop = ResaleShop()
    shop.buy(co)
    shop.buy(co2)
    shop.printInv()
    shop.refurbish(co2,"new OS")
    shop.sell(co)
    shop.sell(co)
    shop.printInv()

main()