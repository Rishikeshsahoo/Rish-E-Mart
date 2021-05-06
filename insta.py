from flask import Flask,render_template
from instaloader import Instaloader,Profile

app=Flask(__name__)
L=Instaloader()
L.login()
profile=Profile.from_username(L.context,'rishikeshsahoo_2828')

list1=[]
list2=[]
list3=[]

for things in profile.get_followers():
    list1.append(things.username)

for things in profile.get_followees():
    list2.append(things.username)

for thing in list2:
    if thing not in list1:
        list3.append(thing)

@app.route('/')
def home_page():
    print(list3)
    return render_template('insta.html',list3=list3)

if __name__=="__main__":
    app.run(debug=True)