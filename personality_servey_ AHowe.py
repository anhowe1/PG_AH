print ("what's your name")
name=input().title()
print ("cool nice to meet you" + name)


print ("What's your favorite sport?")
sport=input().title()
if sport == "Skiing":
    print ("I love skiing too")
elif sport == "Snowboarding":
    print ("I have never tryed snowboarding")
elif sport == "Dance":
    print ("A lot of my friends dance")
else:
    print (sport + " sounds like a lot of fun.")

print ("What's your favorite animal?")
animal=input().title()
if animal == "Dog":
    print ("I have a dog, her name is Bailey and she is an australian shepherd.")
elif animal == "Cat":
    print ("I have three cats, their names are Mr. Cheeky Chops, Leo and Max")
elif animal == "Elephant":
    print ("They are beautiful, did you know they cover themselves in mud to protect their skin from the sun?")

elif animal == "Bear":
    print ("Did you know black bears love honey! What type of Bear do you like most: Black Bear, polar Bear or grizzly bear")
    bear = input().title()
    if bear == "Black Bear" or bear == "Grizzly Bear":
        print ("My favorite bear type is a polar Bear")
    elif bear == "Polar Bear":
        print ("I love polar bears as well")

print ("What's your favorite pass time activity, other than sports")
activity = input()
if activity == "reading":
    print ("my favorite book is The Golden Compass")
elif activity == "hanging out with my friends":
    print ("I like to hang out with my friends as well")
elif activity == "drawing":

    print ("I love drawing. Do you ever paint?(please just say Yes or No)")
    paint = input().title()
    if paint == "Yes":
        print("awesome")
    elif paint == "No":
        print("cool, you should try it some times")

