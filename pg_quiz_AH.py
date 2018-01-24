import pyautogui as pg
import time
import webbrowser


points = 0



# Question
answer = pg.prompt(
"""
How big should your backyard be?

a) massive
b) medium
c) none exsistent

"""
    )

#Answer
pg.alert("You chose " + answer)

if answer == "a" or answer == "A":
    points +=1

elif answer == "b" or answer == "b":
    points +=2

elif answer == "c" or answer == "c":
    points +=3



# Question
answer = pg.prompt(
"""
How close should you be to your neighbors?

a) miles away
b) a safe distance
c)just a wall between each other

"""
    )

#Answer
pg.alert("You chose " + answer)

if answer == "a" or answer == "A":
    points +=1

elif answer == "b" or answer == "b":
    points +=2

elif answer == "c" or answer == "c":
    points +=3




# Question
answer = pg.prompt(
"""
How close should you be to shops?

a) a fifteen minute car ride away
b) at the most a 5 minute car ride away or bike ride
c) right outside my door

"""
    )

#Answer
pg.alert("You chose " + answer)

if answer == "a" or answer == "A":
    points +=1

elif answer == "b" or answer == "b":
    points +=2

elif answer == "c" or answer == "c":
    points +=3


# Question
answer = pg.prompt(
"""
How big should your house be?

a) quite big
b) medium
c) tiny

"""
    )

#Answer
pg.alert("You chose " + answer)

if answer == "a" or answer == "A":
    points +=1
    
elif answer == "b" or answer == "b":
    points +=2

elif answer == "c" or answer == "c":
    points +=3


# Question
answer = pg.prompt(
"""
What is paradise to you?

a) rolling hills and no one else in sight
b) room to move and but not no one or anything in sight
c) minimul room to move but lots of activities to do

"""
    )

#Answer
pg.alert("You chose " + answer)

if answer == "a" or answer == "A":
    points += 1

elif answer == "b" or answer == "b":
    points +=2

elif answer == "c" or answer == "c":
    points +=3


#end of survey
    pg.alert ("You will best live in...")

if points <3:
    pg.alert ("You should live with no one else in the middle of no where")
    webrowser.open("http://www.mycity-web.com/wp-content/uploads/2015/03/country_78.jpg")
elif points >= 3 and points < 4:
    pg.alert ("you should live in the suburbs")
    webroser.open("https://cdn.vox-cdn.com/uploads/chorus_asset/file/8737999/vancouver_suburb.jpg")
elif points >=5: 
    pg.alert(" live in New York and make some friends")
    webroser.open ("http://cdn-image.travelandleisure.com/sites/default/files/styles/1600x1000/public/1485547918/new-york-city-skyline-BIGCITY0117.jpg?itok=po0Op8ou")
    
