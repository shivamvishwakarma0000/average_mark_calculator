from flask import Flask, render_template, request, redirect, url_for
app=Flask(__name__)

# @app.route('/',methods=['GET'])
# def welcome():
#     return "welcome shivam"
#     # return render_template('index.html')

# @app.route('/index',methods=['GET'])
# def index():
#     return "this is index page"


@app.route('/success/<int:score>')
def success(score):
    return "    the persion is passed the average score is : " +str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return "    the person is fail the average score is  :    "+str(score)


@app.route('/',methods=["GET","POST"])
def index():
    if request.method == "GET":
        return render_template('index.html')
    else:
        hindi=float(request.form['hindi'])
        english=float(request.form['english'])

        math=float(request.form['math'])
        physics=float(request.form['physics'])
        chemistry=float(request.form['chemistry'])
        biology=float(request.form['biology'])
        
        average_marks=(hindi+english+math+physics+chemistry+biology)/6
        res=""
        if average_marks>=40:
            res="success"
        else:
            res="fail"
            
        return redirect(url_for(res,score=average_marks))    
        # return render_template('form.html',score=average_marks)
    
        




if __name__ == '__main__':
    app.run(debug=True)  
