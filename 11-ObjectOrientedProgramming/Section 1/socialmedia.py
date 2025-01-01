class SocialMediaProfile:
    def __init__(self, username):
        self.username = username
        self.posts = []

    def add_post(self, content):
        self.posts.append(content)
        print(f"{self.username} added a new post: {content}")

    def display_timeline(self):
        for i, num in enumerate(self.posts, start=1):
            print(f'{i} - {num}')
    
def main():
    user = SocialMediaProfile('johndoe')
    user.add_post("Hello, world!")
    user.add_post("Had a great day at the park!")
    user.add_post("What's up, Natalie? How are you?")

    user.display_timeline()

if __name__ == "__main__":
    main()
