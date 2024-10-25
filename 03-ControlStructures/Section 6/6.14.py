###
# Program that checks whether a given person is a good influencer
#
facebook = True
twitter = False
instagram = True

if (facebook + twitter + instagram) >= 2:
    print("You are a good influencer!")
else:
    print("You are not a good influencer.")