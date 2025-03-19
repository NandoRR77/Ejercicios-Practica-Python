# Define class MyFirstClass
class MyFirstClass():
    # Define string variable called index
    print('Who wrote this?')
    index = 'Author-Book'
    
    # Define function hand_list()
    def hand_list(self, philosopher,book):
        print(MyFirstClass.index)
        # variable + “ wrote the book: ” + variable
        print(philosopher + ' wrote the book: ' + book)

# Call function handlist()
whodunnit = MyFirstClass()
whodunnit.hand_list("Sun Tzu" , "The Art of War")