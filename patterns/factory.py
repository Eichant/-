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
# Фабричний клас для створення мультимедійних об'єктів
class MultimediaFactory:
    def create_media(self, media_type):
        if media_type == "audio":
            return Audio()
        elif media_type == "video":
            return Video()
        elif media_type == "audiobook":
            return AudioBook()
        elif media_type == "photo":
            return Photo()
        elif media_type == "book":
            return Book()
        else:
            raise ValueError("Invalid media type")

#Приклад
#factory = MultimediaFactory()

#audio = factory.create_media("audio")
#print(audio.play())  # Playing audio

#video = factory.create_media("video")
#print(video.play())  # Playing video

#photo = factory.create_media("photo")
#print(photo.play())  # Displaying photo
