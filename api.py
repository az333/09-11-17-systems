from flask import Flask, render_template
import urllib2, json

app = Flask(__name__)

s = urllib2.urlopen("https://api.nasa.gov/planetary/apod?api_key=eoKXcNJaUFK52CD4hbq2OSj8MsM52TVoUnLuP7pk").read()
dic = json.loads(s)

@app.route('/')
def root():
    return render_template('base.html', title=dic['title'], date=dic['date'], copyright=dic['copyright'], hdurl=dic['hdurl'], explanation=dic['explanation'])


if __name__ == "__main__":
    app.debug = True
    app.run()
