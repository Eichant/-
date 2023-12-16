# Абстрактний клас для мультимедійного об'єкта
class MultimediaObject:
    def play(self):
        pass

# Конкретні класи мультимедійних об'єктів
class Audio(MultimediaObject):
    def play(self):
        return "Playing audio"

class Video(MultimediaObject):
    def play(self):
        return "Playing video"

class AudioBook(MultimediaObject):
    def play(self):
        return "Playing AudioBook"

class Photo(MultimediaObject):
    def play(self):
        return "Displaying photo"

class Book(MultimediaObject):
    def play(self):
        return "Displaying book"

# Абстрактна фабрика для створення мультимедійних об'єктів
class MultimediaFactory:
    def create_audio(self):
        pass

    def create_video(self):
        pass

    def create_audiobook(self):
        pass

    def create_photo(self):
        pass

    def create_book(self):
        pass

# Конкретна реалізація фабрики
class SimpleMultimediaFactory(MultimediaFactory):
    def create_audio(self):
        return Audio()

    def create_video(self):
        return Video()

    def create_audiobook(self):
        return AudioBook()

    def create_photo(self):
        return Photo()

    def create_book(self):
        return Book()
