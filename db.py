from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///posts.db'
db=SQLAlchemy(app)
class Blog(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(100),nullable=False,default='n\a')
    name=db.Column(db.String(100),nullable=False,default='N/A')
    def __repr__(self):
        return 'blogy'

@app.route('/posts',methods=['GET','POST'])
def posts():
    if request.method=='POST':
        tit=request.form['title']
        nam=request.form['name']
        newp=Blog(title=tit,name=nam)
        db.session.add(newp)
        db.session.commit()
        return render_template('res.html',postss=newp)
if __name__=="__main__":
    app.run(debug=True)
