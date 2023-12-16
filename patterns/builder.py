# Клас, який представляє мультимедійний контент
class MediaContent:
    def __init__(self):
        self.title = None
        self.format = None
        self.duration = None

    def __str__(self):
        return f"{self.title} ({self.format}), {self.duration} mins"

# Клас, який представляє статтю
class Article:
    def __init__(self):
        self.title = None
        self.content = None

    def __str__(self):
        return f"{self.title}: {self.content}"

# Інтерфейс Builder для мультимедійного контенту
class MediaContentBuilder:
    def build_title(self, title):
        pass

    def build_format(self, format):
        pass

    def build_duration(self, duration):
        pass

    def get_result(self):
        pass

# Інтерфейс Builder для статті
class ArticleBuilder:
    def build_title(self, title):
        pass

    def build_content(self, content):
        pass

    def get_result(self):
        pass

# Конкретний Builder для мультимедійного контенту
class MediaContentConcreteBuilder(MediaContentBuilder):
    def __init__(self):
        self.media_content = MediaContent()

    def build_title(self, title):
        self.media_content.title = title
        return self

    def build_format(self, format):
        self.media_content.format = format
        return self

    def build_duration(self, duration):
        self.media_content.duration = duration
        return self

    def get_result(self):
        return self.media_content

# Конкретний Builder для статті
class ArticleConcreteBuilder(ArticleBuilder):
    def __init__(self):
        self.article = Article()

    def build_title(self, title):
        self.article.title = title
        return self

    def build_content(self, content):
        self.article.content = content
        return self

    def get_result(self):
        return self.article

# Director для мультимедійного контенту
class MediaContentDirector:
    def __init__(self, builder):
        self.builder = builder

    def construct(self, title, format, duration):
        return self.builder.build_title(title).build_format(format).build_duration(duration).get_result()

# Director для статті
class ArticleDirector:
    def __init__(self, builder):
        self.builder = builder

    def construct(self, title, content):
        return self.builder.build_title(title).build_content(content).get_result()

# Фабричний клас для створення мультимедійних об'єктів
class MultimediaFactory:
    def create_media_content(self, title, format, duration):
        builder = MediaContentConcreteBuilder()
        director = MediaContentDirector(builder)
        return director.construct(title, format, duration)

    def create_article(self, title, content):
        builder = ArticleConcreteBuilder()
        director = ArticleDirector(builder)
        return director.construct(title, content)

# Використання фабрики для мультимедійного контенту та статті
factory = MultimediaFactory()

audio = factory.create_media_content("Song Title", "MP3", 4.5)
print(audio)  # Song Title (MP3), 4.5 mins

news_article = factory.create_article("Breaking News", "This is the breaking news content.")
print(news_article)  # Breaking News: This is the breaking news content.
