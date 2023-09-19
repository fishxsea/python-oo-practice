from random import choice

"""Word Finder: finds random words from a dictionary."""


class WordFinder:
    
    def __init__(self, file_path):
        
        file = open(file_path)
        self.words = self.parse(file)
        
        print(f'{len(self.words)} words read')
        
    def random(self):
        '''Returns random word from file'''
        return choice(self.words)
    
    def parse(self, file):
        return [word.strip() for word in file]
    
class SpecialWordFinder(WordFinder):
    
    def parse(self, file):
        '''Removes all blank spaces and commented lines'''
        return [word.strip() for word in file if word[0] != '#']
            

wf = WordFinder('words.txt')
swf = SpecialWordFinder('words.txt')

print(swf.random())


            
            
        
