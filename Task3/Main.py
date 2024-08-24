import pymysql
from datetime import datetime

# MySQL bağlantısı
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='12345',
    database='moviedb',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

def create_db_and_table():
    with connection.cursor() as cursor:
        cursor.execute("CREATE DATABASE IF NOT EXISTS moviedb;")
        cursor.execute("USE moviedb;")
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS movie_info (
                id INT PRIMARY KEY AUTO_INCREMENT,
                title VARCHAR(255) NOT NULL,
                released DATE,
                director VARCHAR(255) NOT NULL,
                genre VARCHAR(255)
            );
        """)
        connection.commit()

def insert_movie(title, released, director, genre):
    with connection.cursor() as cursor:
        cursor.execute("""
            INSERT INTO movie_info (title, released, director, genre)
            VALUES (%s, %s, %s, %s)
        """, (
            title,
            datetime.strptime(released, '%d %b %Y').date() if released != 'N/A' else None,
            director,
            genre
        ))
        connection.commit()

def get_some_movies(searched_text):
    api_key = '5d9df2b8'
    response = requests.get(f"http://www.omdbapi.com/?s={searched_text}&apikey={api_key}")
    data = response.json()
    
    if data.get('Response') == 'True':
        for item in data['Search']:
            movie_id = item['imdbID']
            movie_response = requests.get(f"http://www.omdbapi.com/?i={movie_id}&apikey={api_key}")
            movie_data = movie_response.json()
            
            if movie_data.get('Response') == 'True':
                title = movie_data['Title']
                released = movie_data['Released']
                director = movie_data['Director']
                genre = movie_data['Genre']
                insert_movie(title, released, director, genre)
            else:
                print(f"Could not fetch details for movie ID: {movie_id}")
    else:
        print(f"No movies found with '{searched_text}' in the title.")

if __name__ == "__main__":
    create_db_and_table()
    searched_movie_title = input("Enter the movie title: ")
    get_some_movies(searched_movie_title)
    connection.close()

# def get_some_movies(searched_text):
#     response = requests.get("http://www.omdbapi.com/?s="+searched_text+"&apikey=fff9b9a4")
#     data = response.json()
    
#     if data.get('Response') == 'True':
#         for item in data['Search']:
#             movie_id = item['imdbID']
#             movie_response = requests.get(f"{OMDB_URL}?i={movie_id}&apikey={API_KEY}")
#             movie_data = movie_response.json()
            
#             if movie_data.get('Response') == 'True':
#                 insert_movie_info(movie_data)
#             else:
#                 print(f"Could not fetch details for movie ID: {movie_id}")
#     else:
#         print("No movies found with '"+searched_text+"' in the title.")

if __name__ == "__main__":
    print("---------------------------1----------------------")
    # create_database_and_table()
    # print("---------------------------10----------------------")
    # searched_movie_title="Batman"
    # get_some_movies(searched_movie_title)
    print("---------------------------30----------------------")
    # connection.close()