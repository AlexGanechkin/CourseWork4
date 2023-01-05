# это файл для классов доступа к данным (Data Access Object). Здесь должен быть класс с методами доступа к данным
# здесь в методах можно построить сложные запросы к БД

class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_all_movies(self):
        movies = Movie.query.all()
        return