"""
   Filename: computer.py
Description: Using OOP to create a computer object
     Author: Marybella Martinez
       Date: 18 April 2023
"""

class Computer:
    """Creates and stores information about the computer object"""
    #stores computer data
    # What attributes will it need?
    description: str 
    processor_type: str
    hard_drive_capacity: int
    memory: int
    operating_system: str
    year_made: int
    price: int
    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, des:str ,processor:str, hard_drive:int,mem:int,op:str, year:int, pr:int):
        self.description = des
        self.processor_type = processor
        self.hard_drive_capacity = hard_drive
        self.memory = mem
        self.operating_system = op
        self.year_made = year
        self.price = pr
        
    # What methods will you need?
    def printDetails(self):
        """Prints out the details of the computer object"""
        print(self.description + ",", self.processor_type + ",", self.hard_drive_capacity, ","
              ,self.memory, ",", self.operating_system ,",", self.year_made, ",", self.price)

def main():
    computer = Computer("Mac Pro (Late 2013)","3.5 GHc 6-Core Intel Xeon E5",1024, 64,"macOS Big Sur", 2013, 1500)
    computer.printDetails()

if __name__ == "__main__": main()
        
