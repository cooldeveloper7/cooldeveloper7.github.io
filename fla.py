from flask import Flask,redirect,url_for
app=Flask(__name__)
@app.route('/home/<name>')
def home(name):
    if name=='admin':
        return redirect(url_for('rev',revn=20.0))
    else:
        return "hello world %s"%name
@app.route('/rev/<float:revn>')
def rev(revn):
    return 'revision no %f'%revn
if __name__=='__main__':
    app.run(debug=True)
