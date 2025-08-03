
def generate_story():
    story=input("Enter a story: ")
    words=story.split()
    for word in words:
        if word.startswith("_"):
            user_input=input(f"Enter a word for {word}: ")
            story=story.replace(word,user_input)
    return story

print(generate_story())
