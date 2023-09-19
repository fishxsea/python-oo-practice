"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    
    def __init__(self, start) -> int:
        self.start = start
        self.curr = start
        
    
    def generate(self):
        '''Increments starting number by 1'''
        self.curr += 1
        return self.curr - 1
    
    def reset(self):
        '''Resets back to starting number'''
        self.curr = self.start
        


        
        
        

