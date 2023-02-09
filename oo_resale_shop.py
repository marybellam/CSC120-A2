from computer import *
class ResaleShop:
#Class with all the shop atributes and information
    # What attributes will it need?
    inventory = []
    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self):
        self.inventory = []
        # You'll remove this when you fill out your constructor

    # What methods will you need?
    #adds a computer to the inventory list
    def buy(self,computer: Computer):
        self.inventory.append(computer)

    #removes a computer from the inventory list
    def sell(self,computer):
        self.inventory.remove(computer)

    #makes new price for computer and finds if there is a new os sysytem
    def refurbished(self,computer,new_os):
        if(computer.year < 2000):
            computer.pr = 0
        elif(computer.year < 2012):
            computer.pr = 250
        elif(computer.year < 2018):
            computer.pr = 500
        else:
            computer.pr = 1000
        if new_os is not None:
            computer.op = new_os

    #prints out the inventory
    def printInv(self):
        print(self.inventory)