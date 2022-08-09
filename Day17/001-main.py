class User:
    def __init__(self, user_id, user_name):
        self.id = user_id
        self.username = user_name
        self.follower = 0

user1 = User(1, "SK")

print(user1.id)
print(user1.follower)