from flask import Flask, render_template
from models import db, Movie

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:12345@localhost/moviedb'
db.init_app(app)

@app.route('/movies/')
def movies():
    all_movies = Movie.query.all()
    return render_template('index.html', movies=all_movies)

@app.route('/movies/<int:movie_id>')
def movie_detail(movie_id):
    movie = Movie.query.get_or_404(movie_id)
    return render_template('movie.html', movie=movie)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        # insert_sample_movies()  # Uncomment if you need to insert sample movies
    app.run(debug=True)