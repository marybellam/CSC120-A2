class Computer:
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
    def __init__(self, des,processor, hard_drive,mem,op, year, pr):
        self.description = des
        self.processor_type = processor
        self.hard_drive_capacity = hard_drive
        self.memory = mem
        self.operating_system = op
        self.year_made = year
        self.price = pr
        # You'll remove this when you fill out your constructor

    # What methods will you need?
    #no methods needed in this class

        
