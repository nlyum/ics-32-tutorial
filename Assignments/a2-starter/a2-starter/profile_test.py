import Profile
from pathlib import Path

path_string = "C:/Users/natha/OneDrive/Desktop/UCI/ICS32/Assignments/a2-starter/a2-starter/profile1_test.dsu"
def create_profile1():
    profile1 = Profile.Profile("first", "NATHAN", "SECRET")
    
    profile1.save_profile(path_string)

def open_profile1():
    profile1 = Profile.Profile()
    profile1.load_profile(path_string)
    profile1.save_profile(path_string)

def add_user_pass():
    profile1 = Profile.Profile()
    profile1.load_profile(path_string)
    profile1.username = "new_username"
    profile1.password = "new_password"
    profile1.bio = "new_bio"
    profile1.save_profile(path_string)

def add_post():
    profile1 = Profile.Profile()
    profile1.load_profile(path_string)
    post1 = Profile.Post("Feeling pretty good today")
    profile1.add_post(post1)
    profile1.save_profile(path_string)

def read_posts():
    profile1 = Profile.Profile()
    profile1.load_profile(path_string)
    print(profile1.get_posts())


if __name__ == "__main__":
    read_posts()