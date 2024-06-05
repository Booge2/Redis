from user import User
from post import Post
from auth import Auth

def main():
    while True:
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            username = input("Username: ")
            password = input("Password: ")
            full_name = input("Full Name: ")
            email = input("Email: ")
            if Auth.register(username, password, full_name, email):
                print("Registration successful")
            else:
                print("User already exists")

        elif choice == '2':
            username = input("Username: ")
            password = input("Password: ")
            if Auth.login(username, password):
                print("Login successful")
                user_menu(username)
            else:
                print("Invalid credentials")

        elif choice == '3':
            break

def user_menu(username):
    while True:
        print("1. View Profile")
        print("2. Edit Profile")
        print("3. Add Friend")
        print("4. View Friends")
        print("5. Add Post")
        print("6. View Posts")
        print("7. Logout")
        choice = input("Enter choice: ")

        if choice == '1':
            user = User.get(username)
            print(f"Full Name: {user.full_name}")
            print(f"Email: {user.email}")

        elif choice == '2':
            full_name = input("New Full Name: ")
            email = input("New Email: ")
            user = User.get(username)
            user.update(full_name, email)
            print("Profile updated")

        elif choice == '3':
            friend_username = input("Friend Username: ")
            user = User.get(username)
            user.add_friend(friend_username)
            print("Friend added")

        elif choice == '4':
            user = User.get(username)
            friends = user.get_friends()
            print("Friends:", ", ".join(friends))

        elif choice == '5':
            post_id = input("Post ID: ")
            content = input("Post Content: ")
            post = Post(post_id, username, content)
            post.save()
            user = User.get(username)
            user.add_post(post_id)
            print("Post added")

        elif choice == '6':
            user = User.get(username)
            posts = user.get_posts()
            for post_id in posts:
                post = Post.get(post_id)
                print(f"Post ID: {post.post_id}")
                print(f"Content: {post.content}")
                print("---")

        elif choice == '7':
            break

if __name__ == "__main__":
    main()
