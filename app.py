from flask import Flask,render_template,url_for,redirect,request,session
from data_control import get_all_books
app = Flask(__name__)


@app.route('/')
def index():
    #books = get_all_books()
    #print(f"Книг: {books}")
    return (render_template('index.html'))

@app.route('/about.html')
def about():
    #books = get_all_books()
    #print(f"Книг: {books}")
    return (render_template('about.html'))

@app.route('/about_site.html')
def about_site():
    #books = get_all_books()
    #print(f"Книг: {books}")
    return (render_template('about_site.html'))

@app.route('/blog.html')
def blog():
    #books = get_all_books()
    #print(f"Книг: {books}")
    return (render_template('blog.html'))

@app.route('/books.html')
def books():
    #books = get_all_books()
    #print(f"Книг: {books}")
    return (render_template('books.html'))

@app.route('/course.html')
def course():
    #books = get_all_books()
    #print(f"Книг: {books}")
    return (render_template('course.html'))

@app.route('/lection.html')
def lection():
    #books = get_all_books()
    #print(f"Книг: {books}")
    return (render_template('lection.html'))


#@app.route('/cites/books.html')
#def index():
#   books = get_all_books()
#    print(f"Книг: {books}")
#   return (render_template('books.html',books=books))

#@app.route('/form.html',methods = ["GET","POST"])
#def form():
#    if request.method == "POST":
#        form = request.form
#        name = form["name"]
#        age = form["age"]
#        print(name,age)
#    return (render_template('form.html'))

@app.errorhandler(404)
def page_not_found(e):
    #return (render_template("error.html"))
    return "Страница не найдена"


if __name__ == "__main__":
    app.run(debug=True,port=5001)