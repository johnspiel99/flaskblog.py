from flask import Flask, render_template
app = Flask(__name__)

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


if __name__ == '__main__':
	app.run(debug=True)
