class User:
    # constructor - special method used to initialize attributes of a class 
    def __init__(self, id, username):
        self.id = id
        self.username = username
        print('new user has been created...')
        self.followers = 0 # default value - not necessary in the initialize step
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

user_1 = User("001", "joy")
# every object from this User class must now have the id and username values
user_2 = User("002", "gloria")

user_1.follow(user_2)
print(user_1.following)
print(user_1.followers)
print(user_2.following)
print(user_2.followers)

# print(user_1.id)
