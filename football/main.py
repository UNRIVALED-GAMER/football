from flask import Flask,render_template,request
import football
app=Flask(__name__)

@app.route("/")
def futbol():
    return render_template("home.html")

@app.route('/', methods=['POST'])
def upload_image():
   
    file = request.files['image']
    
    if file:
       
        # Dosyayı belirtilen klasöre kaydet
        file.save(f"./static/uploads/{file.filename}")
        sinif,skor=football.futbol2(f"./static/uploads/{file.filename}")
        a=skor*100
        return render_template("home.html",sinif=sinif,skor=round(a,2),x=f"./static/uploads/{file.filename}")
    else:
        hata="resim bulunamadı"
        return render_template("home.html",hata=hata)
app.run(debug=True)