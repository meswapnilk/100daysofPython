class User:
    # Constructor
    def __init__(self, user_id, user_name):
        self.id = user_id
        self.username = user_name
        self.followers = 0
        self.following = 0
    
    def follow(self, user):
        user.followers += 1
        self.following += 1

user1 = User(1, "SK")
user2 = User(2, "AK")

user1.follow(user2)

print("User 1 Details")
print(user1.followers)
print(user1.following)

print("User 2 Details")
print(user2.followers)
print(user2.following)