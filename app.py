from flask import Flask, render_template, url_for, redirect, request
import sertube

#import tubedown
import fileaval
import tempclr
app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("lname")
        return redirect("/search?song="+name)
    return render_template("index.html")


@app.route('/search')
def search():
    name = request.args.get('song')
    data = sertube.search_youtube(name)
    
    return render_template("search.html" , data=data)


@app.route('/player')
def player():
    id = request.args.get('s')
    artist = request.args.get('a')
    #data = tubedown.tubedata(id)
    #yn = fileaval.file_avalable(id)
    #print(yn)
    #if False == yn:
        #tubedown.youtubedownload(id)
    #name = data["title"]
    #thumb = data['thumb']
    #audio = f"temp/{id}.mp3"
    #return render_template("player.html", name=name , artist=artist , thumb=thumb, audio=audio)
    return render_template("player.html",  artist=artist)
    #return id+artist 

@app.route('/cls')
def cls():
    
    return "succesfully cleaned"

@app.route('/about')
def about():
    tempclr.cleaner()
    return render_template("index.html", user="hello")


if __name__ == '__main__':

    app.run()
