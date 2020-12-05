# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from flask import Flask, request, render_template
from models import XYZ
import os, glob
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import true, select, and_, or_
from datetime import date, time
import numpy as np

app= Flask(__name__)


app.jinja_env.filters['zip'] = zip
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'


app.config["SQLALCHEMY_DATABASE_URI"] = "mssql+pyodbc://RAMADHELPD3ITD/PPE_VIOLATION?driver=SQL+Server?trusted_connection=yes"
#app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
db.init_app(app)


xx = ['Helmet', 'Jacket', 'Shoes']
date_= date.today().strftime('%Y-%m-%d')

# conn = pyodbc.connect('Driver={SQL Server};'
#                           'Server=RAMADHELPD3ITD;'
#                           'Database=PPE_VIOLATION;'
#                           'Trusted_Connection=yes;')


class Ppe_vio(db.Model):

    SrNo = db.Column(db.Integer, primary_key=True)
    Date = db.Column(db.String(80), unique=False, nullable=False)
    Time = db.Column(db.String(120), unique=False, nullable=False)
    Helmet = db.Column(db.String(120))
    Jacket = db.Column(db.String(120))
    Shoes = db.Column(db.String(120))
    Camera = db.Column(db.String(120))
    Image = db.Column(db.String(120))


def ppe_vio():
    if request.method=='POST':
        name= request.form.get('name')
        entry= Ppe_vio()

query= Ppe_vio.query.all()
print('now queryyy is...', query)
aa= Ppe_vio.query.filter_by(Date= date_).all()
#print('images are', aa[0].Image)
#for q in query:
    # print(q.Date)

def image_name():
    # files= glob.glob(os.path.join('C:\\Users\\rstps.ithelpdesk3\\Documents\\PPE_VIOLATION', 'LM_6'+'\\*'))
    # print(os.getcwd())
        # for file in files:
        #     if file.endswith('.jpg'):
        #         return file
        files= []


        x= glob.glob(os.path.join('C:\\Users\\rstps.ithelpdesk3\\PycharmProjects\\ppe_violation\\static\\img', 'LM_6'+'\\*'))
        for xx in x:
            #for file in files:
                # if file.endswith('.jpg'):
            files.append(xx.split('\\')[-1:])
        return files

files= image_name()

@app.route('/', methods= ['GET', 'POST'])
def print_hi():

    xyz= XYZ()

    # for file in files:
    #     print('file name iss......', file[0])
    q1= Ppe_vio.query.filter_by(Date=date_).all()
    print(files)

    xyz.name= 'jay'
    xyz.img='heart.jpg'

    x2= XYZ()
    x2.name= 'akshay'
    x2.img= 'VIO_21.JPG'

    xx= ['Helmet', 'Jacket', 'Shoes']



    # Use a breakpoint in the code line below to debug your script.
    return  render_template('index.html', x1= files, qq= q1, x2= xx, d1= date_)



@app.route('/result', methods= ['POST', 'GET'])
def result():

    if request.method=='POST':
        helmet= request.form.get('helmet')
        jacket= request.form.get('jacket')
        shoes= request.form.get('shoes')
        from_= request.form.get('form')
        lm_6 = request.form.get('lm_6')
        lm_8 = request.form.get('lm_8')
        stock_yard = request.form.get('stock_yard')
        to_= request.form.get('to')

        print('returned values are......',helmet, jacket, from_, to_)
        cam= ['LM_6', 'LM_8', 'LM_7']
        val= [lm_6, lm_8, stock_yard]
        camera= []
        for cam_, val_ in zip(cam, val):
            if val_:
                camera.append(cam_)
            else:
                camera.append(None)

        print(camera)
        print('lm6...', lm_6)
        print('lm8...', lm_8)
        print('lm6...', lm_6)
        print('stock yard', stock_yard)
        qry = Ppe_vio.query.filter(Ppe_vio.Date >= from_, Ppe_vio.Date <= to_,).filter(or_(Ppe_vio.Helmet==helmet,
                                        Ppe_vio.Jacket==jacket, Ppe_vio.Shoes== shoes)).filter(or_(
            Ppe_vio.Camera==camera[0], Ppe_vio.Camera==camera[1], Ppe_vio.Camera==camera[2],
        )).all()
        #lst_1= select([Ppe_vio.Date]).where(true())

        lst_1= select([Ppe_vio]).where(
                        and_(
                            Ppe_vio.Helmet == True,
                            Ppe_vio.Jacket == False
                        )
                    )
        print('helmet true....', lst_1)
        #q1 = Ppe_vio.query.filter_by(Date='2020-11-27').all()
        #date= Ppe_vio.query.filter(Date.between= ('1985-01-17', '1988-01-17'))
        print('queryyyyy.....', qry)
        return render_template('index.html',x1= files, qq= qry, x2= xx, d1= date_)
    else:
        pass

@app.route('/about')
def about():
    return render_template('about.html')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(debug= True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
