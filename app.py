# import sys
# sys.path.append('/faceswap/faceswap/ocr/')

# from app import app


from flask import *  
import os
# import asyncio
import process

app = Flask(__name__) 
app.config['UPLOAD_FOLDER'] = 'files'

@app.route('/')  
def upload():  
    return render_template("file_upload_form.html")


@app.route('/success', methods = ['POST'])  
def success():  
    source_image = ''
    driving_video = ''
    if request.method == 'POST':  
        files = request.files.getlist("file")
        for file in files:
            extention = file.filename.split('/')[-1]
            if extention == 'jpeg' or extention == 'png' or extention == 'jpeg':
                source_image = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            else:
                driving_video = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        
        flag = process.get(source_image, driving_video)

        # return render_template("success.html", name = f.filename)  
        if flag == True:
            return send_file(os.path.join(app.config['UPLOAD_FOLDER'], 'generated.mp4'), as_attachment=True)
        # else:
        #     flash('Plese try again...') 
        #     return


if __name__ == '__main__':  
    app.run(debug = True)  