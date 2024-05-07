import threading

class Movie:
    def __init__(self, title):
        self.title = title

class Session:
    def __init__(self, movie, start_time, available_seats):
        self.movie = movie
        self.start_time = start_time
        self.available_seats = available_seats
        self.lock = threading.Lock()

class BookingSystem:
    def __init__(self):
        self.movies = []
        self.sessions = []
        self.lock = threading.Lock()

    def add_movie(self, movie):
        self.movies.append(movie)

    def add_session(self, session):
        self.sessions.append(session)

    def select_movie(self, movie):
        with self.lock:
            if movie in self.movies:
                self.selected_movie = movie
                print(f"Movie '{movie.title}' selected.")
            else:
                print(f"Movie '{movie.title}' does not exist.")

    def select_session(self, session):
        with self.lock:
            if session in self.sessions:
                self.selected_session = session
                print(f"Session '{session.start_time}' selected.")
            else:
                print(f"Session '{session.start_time}' does not exist.")

    def book_seat(self, seat):
        with self.selected_session.lock:
            if seat in self.selected_session.available_seats:
                self.selected_session.available_seats.remove(seat)
                print(f"Seat '{seat}' booked.")
            else:
                print(f"Seat '{seat}' is not available.")


movie1 = Movie("Film 1")
movie2 = Movie("Film 2")


session1 = Session(movie1, "10:00", ["A1", "A2", "A3"])
session2 = Session(movie1, "14:00", ["B1", "B2", "B3"])
session3 = Session(movie2, "19:00", ["C1", "C2", "C3"])

booking_system = BookingSystem()

booking_system.add_movie(movie1)
booking_system.add_movie(movie2)
booking_system.add_session(session1)
booking_system.add_session(session2)
booking_system.add_session(session3)

booking_system.select_movie(movie1)
booking_system.select_session(session2)


booking_system.book_seat("B2")
booking_system.book_seat("B3")
booking_system.book_seat("B3")