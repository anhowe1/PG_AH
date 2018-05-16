import pyautogui as pg
import time
import webbrowser


points = 0


# Question
answer = pg.prompt(
"""
What is your favorite activitie out of these?

a) helping cats/dogs
b) sorting food

"""
    )

#Answer
pg.alert("You chose " + answer)

if answer == "a" or answer == "A":
    points += 1

elif answer == "b" or answer == "b":
    points +=2

# Question
answer = pg.prompt (
"""
What do you like more?

a) helping animals
b) helping people

"""
    )

#answer
pg.alert("You chose " + answer)

if answer == "a" or answer == "A":
    points += 1

elif answer == "b" or answer == "b":
    points +=2


# Question
answer = pg.prompt(
"""
Are you a people person or animal person?

a) people person
b) animal person

"""
    )

#answer
pg.alert("You chose " + answer)

if answer == "a" or answer == "A":
    points += 1

elif answer == "b" or answer == "b":
    points +=2
    
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
    
