from flask import Flask, request, render_template, redirect, url_for, jsonify, flash
import dbconnection
import timer

app = Flask(__name__)
app.secret_key = 'bring day'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def start_index():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['pass']
        if email == 'admin@admin.com' and password == 'admin':
            return redirect(url_for('admin'))
        else:
            if dbconnection.check_info_student(email, password) == True:
                if timer.timerdb(dbconnection.get_time_take(email)) == timer.today().isoformat():
                    flash("Please choose new book", "warning")
                else:
                    flash("Days to bring " + timer.timerdb(dbconnection.get_time_take(email)), "success")
                return render_template('personinfo.html', name = dbconnection.get_info_student(email, password)[0],
                                        surname = dbconnection.get_info_student(email, password)[1],
                                        email = dbconnection.get_info_student(email, password)[2], 
                                        phonenumber = dbconnection.get_info_student(email, password)[3],
                                        takenbook = dbconnection.taken_book(email),
                                        results = dbconnection.get_book_name())
            else:
                return 'Error! Email or password is not correct, please try again(go back)', 404

@app.route('/', methods=['GET', 'POST'])
def choice():
    if request.method == 'POST':
        return redirect(url_for('stud'))
    elif request.method == 'POST':
        return redirect(url_for('admin'))
    else:
        return redirect(url_for('stud'))

@app.route('/studinfo/')
def studinfo():
    return render_template('resall.html')

@app.route('/stud/')
def stud():
    return render_template('registration.html', free_books = dbconnection.get_free_books())

@app.route('/stud/', methods=['POST'])
def post_data_stud():
    gender_type = ['M', 'F']
    if request.method == 'POST':
        id_ = request.form['id']
        fname = request.form['fname']
        sname = request.form['lname']
        email = request.form['email']
        password = request.form['pass']
        dtime = request.form['datetime']
        gender = request.form['gender']
        job = request.form['job']
        point = request.form['point']
        phonenumber = request.form['phonenumber']
        if gender in gender_type:
            dbconnection.insert_students(id_, fname, sname, email, password, dtime, gender, job, point, phonenumber)
            return render_template('result.html', results = dbconnection.get_book())
        else:
            return 'Something went wrong try again', 404

@app.route('/admin/')
def admin():
    return render_template('admins.html')

@app.route('/admin/', methods=['GET','POST'])
def admin_work():
    if request.args.get('work') == 'add':
        return redirect(url_for('addauthbooks.html'))
    elif request.args.get('work') == 'delete':
        return redirect(url_for('deleteauthbooks.html'))
    elif request.args.get('work') == 'borrow':
        return redirect(url_for('borrow.html'))

@app.route('/addauthbooks/')
def addauthbooks():
    return render_template('addauthbooks.html')

@app.route('/addauthbooks/', methods=['POST'])
def addauthbooks_work():
    if request.method == 'POST':
        id_author = request.form['id_author']
        name_author = request.form['fname_author']
        sname_author = request.form['lname_author']
        
        id_book = request.form['id_book']
        name_book = request.form['name_book']
        pagecount = request.form['pagecount']
        point = request.form['point']
        authorId = request.form['author_id']
        typeId = request.form['type_id']
        textbook = request.form['textbook']
        dbconnection.insert_authorz(id_author, name_author, sname_author)
        dbconnection.insert_book(id_book, name_book, pagecount, point, authorId, typeId, textbook)
        return render_template('resall.html', results= dbconnection.get_book())

@app.route('/deleteauthbooks/')
def deleteauthbooks():
    return render_template('deleteauthbooks.html')

@app.route('/deleteauthbooks/', methods=['POST'])
def deleteauthbooks_work():
    if request.method == 'POST':
        name_author = request.form['fname_author']
        name_book = request.form['name_book']
        dbconnection.delete_author(name_author)
        dbconnection.delete_book(name_book)
        return 'Deleted successfully!'

@app.route('/borrow/')
def borrow():
    return render_template('borrow.html', results = dbconnection.get_borrows_student())

@app.route('/borrow/', methods=['POST'])
def borrow_work():
    if request.method == 'POST':
        search = request.form['borrow']
        return jsonify(dbconnection.search_student(search))

@app.errorhandler(404)
def not_found_page(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500

if __name__ == "__main__":
    app.run()