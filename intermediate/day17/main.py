class User:
    # constructor - special method used to initialize attributes of a class 
    def __init__(self, id, username):
        self.id = id
        self.username = username
        print('new user has been created...')
        self.followers = 0 # default value - not necessary in the initialize step

user_1 = User("001", "joy")
# every object from this User class must now have the id and username values

print(user_1.id)