from flask import Flask, render_template, url_for, redirect, request,send_file
# from replit import web
import sertube
import tubedown
import fileaval
import tempclr
import os

app = Flask(__name__)


@app.before_request
def before_request_func():
  temp = os.listdir('static/temp')    
  if len(temp) > 15:
    for file in temp:
      if file != "ignore":
        os.remove("static/temp/" + file)


@app.route('/', methods=["GET", "POST"])
def index():
  
  if request.method == "POST":
    name = request.form.get("lname")
    return redirect("/search?song=" + name)
  return render_template("index.html")


@app.route('/search')
def search():
  name = request.args.get('song')
  data = sertube.search_youtube(name)
  

  return render_template("search.html", data=data)


@app.route('/player')
def player():
  
  id = request.args.get('s')
  artist = request.args.get('a')
  data = tubedown.tubedata(id)
  yn = fileaval.file_avalable(id)
  print(yn)
  if False == yn:
    tubedown.youtubedownload(id)
    
  name = data["title"]
  thumb = data['thumb']
  chrurl = data['chrurl']
  vidurl = data["vidurl"]
  audio = f"temp/{id}.mp3"
  return render_template("player.html",
                         name=name,
                         artist=artist,
                         thumb=thumb,
                         audio=audio,
                         vidurl=vidurl,
                         chrurl=chrurl,
                         id=id)


@app.route('/cls')
def cls():
  tempclr.cleaner()
  return "succesfully cleaned"


@app.route('/about')
def about():
  return render_template("about.html")


@app.route('/download-song')
def download_song():
  return render_template("about.html")



if __name__ == '__main__':
  app.run(debug=True)
  # web.run(app)
