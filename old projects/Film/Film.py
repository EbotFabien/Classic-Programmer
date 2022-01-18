from flask import Flask,render_template,url_for,flash,redirect,request
from flask_bootstrap import Bootstrap
from form import filmform
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
bootstrap=Bootstrap(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///film.db'
app.config['SECRET_KEY'] ='fabs'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Cartoon(db.Model):
    __tablename__ = 'cartoons'

    id = db.Column(db.Integer,primary_key=True)
    Cartoon_name = db.Column(db.String(80) , nullable=False)
    Cartoon_link = db.Column(db.String(300) , nullable=False)
    Cartoon_description = db.Column(db.String(300) , nullable=False)
    
    def __init__(self,Cartoon_name,Cartoon_link,Cartoon_description):
        self.Cartoon_name=Cartoon_name
        self.Cartoon_link=Cartoon_link
        self.Cartoon_description=Cartoon_description

    def __repr__(self):
        return '<Cartoon %r>' %self.id

class Series(db.Model):
    __tablename__ = 'Series'

    id = db.Column(db.Integer,primary_key=True)
    Series_name = db.Column(db.String(80) , nullable=False)
    Series_link = db.Column(db.String(300), nullable=False)
    Series_description = db.Column(db.String(300) , nullable=False)
    
    def __init__(self,Series_name,Series_link,Series_description):
        self.Series_name=Series_name
        self.Series_link=Series_link
        self.Series_description=Series_description

    def __repr__(self):
        return '<Series %r>' %self.id

class Film(db.Model):
    __tablename__ = 'Films'

    id = db.Column(db.Integer, primary_key=True)
    Film_name = db.Column(db.String(80), nullable=False)
    Film_link = db.Column(db.String(120), nullable=False)
    Film_description = db.Column(db.String(120) , nullable=False)
    
    def __init__(self,Film_name,Film_link,Film_description):
        self.Film_name=Film_name
        self.Film_link=Film_link
        self.Film_description=Film_description

    
    def __repr__(self):
        return '<Film %r>' %self.id 
    
db.create_all()

posts =[
    {
        'author':'Corey Schafey',
        'title':'http://dancsa.hu/naruto/%5bDB%5d_Naruto_Movie_%5bD367824A%5d.avi',
        'content':'First post',
        'date_posted':'April 20,2018'
    },
    {
        'author':'Corey Schafey',
        'title':'http://dancsa.hu/naruto/%5bDB%5d_Naruto_Movie_%5bD367824A%5d.avi',
        'content':'First post',
        'date_posted':'April 20,2018'
    },
]

@app.route('/film',methods=['GET','POST'])
def film():
    form = filmform()
    if form.validate_on_submit:
        cartoon=Cartoon.query.filter_by(Cartoon_name=form.film.data).first()
        film=Film.query.filter_by(Film_name=form.film.data).first()
        series=Series.query.filter_by(Series_name=form.film.data).first()
        if cartoon:
           return render_template("downloadpage.html",cartoon=cartoon,legend="cartoon_select")
        elif film:
            return render_template("downloadpage.html",film=film,legend="film_select")
        elif series:
            return render_template("downloadpage.html",series=series,legend="series_select")
        else:
            return render_template("film.html" , form=form)
    

@app.route('/downloadpage/cartoon')
def cartooN():
    cartoon=list(Cartoon.query.all())
    return render_template('downloadpage.html',cartoon=cartoon,legend="cartoon")

@app.route('/downloadpage/series')
def serieS():
    series=list(Series.query.all())
    return render_template('downloadpage.html',series=series,legend="series")

@app.route('/downloadpage/film')
def filM():
    film=list(Film.query.all())
    return render_template('downloadpage.html',film=film,legend="film")

if __name__ == '__main__':
    app.run()

