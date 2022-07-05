class Movie:
    __watched_movies = 0

    def __init__(self, name: str, director: str) -> None:
        self.name = name
        self.director = director
        self.watched = False

    def change_name(self, new_name: str):
        self.name = new_name

    def change_director(self, new_director: str):
        self.director = new_director

    def watch(self):
        if not self.watched:
            Movie.__watched_movies += 1
            self.watched = True

    def __repr__(self) -> str:
        return f"Movie name: {self.name}; Movie director: {self.director}. Total watched movies: {self.__watched_movies}"
