from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '069a15c6f1157fe65d03819c83d6cada'

posts = [
	{
		'author': 'Drax Ravo',
		'title': 'Blog post 1',
		'content': 'First post content',
		'date_posted': 'April 26, 2020'
	},
	{
		'author': 'Vrax Tavo',
		'title': 'Blog post 2',
		'content': 'Second post content',
		'date_posted': 'April 27, 2020'
	}
]
@app.route("/")
@app.route('/Home')
def home():
	return render_template('Home.html', posts=posts)

@app.route('/About')
def about():
	return render_template('About.html',title='About')



@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)



@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
	app.run(debug=True)
