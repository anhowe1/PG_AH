name = "anabel"

subjects = ["English" , "French", "science" , "math"]

print ("hello " +  name)

for i in subjects:
    print ("one of your classes is " + i)
      
characters = ["eleven", "mike","will", "dustine"]

for i in characters:
    if i == "eleven":
        print( i + " is the best character!")
    else:
        print("one of the characters in Stranger things is " + i)



movies = []

while True:
    print ("what's a movie you like? type 'end' to quit.")
    answer = input()

    if answer == "end":
        break
    else:
        movies.append(answer)


for i in movies:
    print ("one of your favorite movies " + i)
