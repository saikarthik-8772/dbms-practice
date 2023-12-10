#This is the mail file for app creation

from flask import Flask,session,render_template,request,redirect,g,url_for
import mysql.connector

import os
 
app = Flask(__name__)

app.secret_key = os.urandom(24)

conn = mysql.connector.connect(host ="localhost",username="root",password="Karthik-337-",database="kathik")
mycursor=conn.cursor()

@app.route('/')
def index():
    return render_template('portal.htm')

@app.route('/left_portal')
def left_portal():
    return render_template('left_portal.htm')

@app.route('/right_portal')
def right_portal():
    return render_template('right_portal.htm')

@app.route('/return')
def retur():
    return render_template('return.htm')


@app.route('/upgradestatic')
def upgrade():
    return render_template('upgradesheet.htm')

@app.route('/authenticate',methods = ['POST'])
def authenticate():

    rollno = request.form['rol']
    passw = request.form['pass']
    query="select count(*) from signup where roll='%s' and pass='%s'" %(rollno,passw)
    mycursor.execute(query)
    cnt=mycursor.fetchall()
    if cnt[0][0]==1:
        session['rollno'] = rollno
        return render_template("studentportal.htm")
    else:
        return render_template('return.htm')


@app.route('/sign',methods = ['POST'])        
def sign():

    rollno = request.form['rol']
    nam = request.form['nam']
    passw = request.form['pass']
    phoneno = request.form['phn']
    addres = request.form['address']
    dob = request.form['Dob']
    query="select count(*) from signup where roll='%s'" %(rollno)
    mycursor.execute(query)
    cnt=mycursor.fetchall()
    if cnt[0][0]==1:
        return render_template('success.htm')
    else:
        query = "insert into signup (name,roll,pass,address,phnno,Dob) values('%s','%s','%s','%s',%s,'%s')" %(nam,rollno,passw,addres,phoneno,dob)
        mycursor.execute(query)
        conn.commit()
        return render_template('success2.htm')  
    

@app.route('/details',methods = ['GET'])        
def details():
    rollno = session['rollno']
    query="select * from signup where roll='%s'" %(rollno)
    mycursor.execute(query)
    user=mycursor.fetchall()
    
    str = "<html><body><label for ='nam'>Name:</label><br>"+user[0][0]+"<br><br><label for ='rol'>Roll no:</label><br>"+user[0][1]+"<br><br><label for ='phn'>Phone no:</label><br>"+user[0][3]+"<br><br><label for ='add'>Address:</label><br>"+user[0][4]+"<br><br></body></html>"
    return str

@app.route('/update',methods = ['POST'])
def update():
    rollno = session['rollno']
    query="select count(*) from gradesheet where rollno='%s'" %(rollno)
    mycursor.execute(query)
    cnt=mycursor.fetchall()
    if cnt[0][0]==1:
        subA = request.form['subA']
        subB = request.form['subB']
        query = "update gradesheet set subA = '%s' , subB = '%s' where rollno = '%s';" %(subA,subB,rollno)
        mycursor.execute(query)
        conn.commit()
        return render_template('success3.htm')
    else :
            subA = request.form['subA']
            subB = request.form['subB']
            query = "insert into gradesheet (rollno,subA,subB) values('%s','%s','%s')" %(rollno,subA,subB)
            mycursor.execute(query)
            conn.commit()
            return render_template('success3.htm')
    
@app.route('/grade',methods = ['get'])
def grade():
    rollno = session['rollno']
    query="select * from gradesheet where rollno ='%s'" %(rollno)
    mycursor.execute(query)
    user=mycursor.fetchall()

    str = "<html><body><label for ='subA'>subjectA:</label><br>"+user[0][0]+"<br><br><label for ='subB'>subjectB:</label><br>"+user[0][1]+"<br><br>"
    return str
    
@app.route('/logout')
def logout():
    session.pop('rollno',None)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
