from flask import Flask,render_template,url_for,redirect,request,session
from data_control import get_all_books, get_all_courses, get_all_resurs, get_all_blog, get_blog
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
    blogs = get_all_blog()
    print(f"Блоги: {blogs}")
    return (render_template('blog.html',blogs=blogs))

@app.route('/read-blog.html/<int:id>',methods=['GET','POST'])
def read_blog(id):
    blog = get_blog(id)
    print("hi",blog)
    return (render_template('read-blog.html',blog=blog))

@app.route('/books.html')
def books():
    books = get_all_books()
    print(f"Книг: {books}")
    return (render_template('books.html',books=books))

@app.route('/course.html')
def course():
    courses = get_all_courses()
    print(f"Курсы: {courses}")
    return (render_template('course.html',courses=courses))

@app.route('/lection.html')
def lection():
    resources = get_all_resurs()
    print(f"Ресурсы: {resources}")
    return (render_template('lection.html',resources=resources))


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