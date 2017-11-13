from flask import Flask, render_template
import urllib2, json

app = Flask(__name__)

#snasa = urllib2.urlopen("https://api.nasa.gov/planetary/apod?api_key=eoKXcNJaUFK52CD4hbq2OSj8MsM52TVoUnLuP7pk").read()
#dicnasa = json.loads(s)

urlnutri = "https://api.nutritionix.com/v1_1/search/mcdonalds?results=0:20&fields=item_name,brand_name,item_id,nf_calories&appId=f53f0c1b&appKey=b011e581b9455ac62f9720112cafa8bf"
nutri = urllib2.urlopen("https://api.nutritionix.com/v1_1/search/mcdonalds?results=0:20&fields=item_name,brand_name,item_id,nf_calories&appId=f53f0c1b&appKey=b011e581b9455ac62f9720112cafa8bf").read()
dicnutri = json.loads(nutri)

@app.route('/')
def root():
    print dicnutri
    return render_template ('nutri.html', dic = dicnutri)
    #return render_template('base.html', title=dic['title'], date=dic['date'], hdurl=dic['hdurl'], explanation=dic['explanation'])


if __name__ == "__main__":
    app.debug = True
    app.run()
