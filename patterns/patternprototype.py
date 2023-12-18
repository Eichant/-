import copy

# Клас, який представляє мультимедійний контент
class MediaContent:
    def __init__(self):
        self.title = None
        self.format = None
        self.duration = None

    def __str__(self):
        return f"{self.title} ({self.format}), {self.duration} mins"

    def clone(self):
        # Використовуємо глибоке копіювання для створення клону об'єкта
        return copy.deepcopy(self)

# Клас, який представляє статтю
class Article:
    def __init__(self):
        self.title = None
        self.content = None

    def __str__(self):
        return f"{self.title}: {self.content}"

    def clone(self):
        # Використовуємо глибоке копіювання для створення клону об'єкта
        return copy.deepcopy(self)

# Використання прототипу для клонування об'єктів
original_media_content = MediaContent()
original_media_content.title = "Original Song"
original_media_content.format = "MP3"
original_media_content.duration = 3.5

cloned_media_content = original_media_content.clone()
cloned_media_content.title = "Cloned Song"

print(original_media_content)  # Original Song (MP3), 3.5 mins
print(cloned_media_content)    # Cloned Song (MP3), 3.5 mins

original_article = Article()
original_article.title = "Original Article"
original_article.content = "This is the original content."

cloned_article = original_article.clone()
cloned_article.title = "Cloned Article"

print(original_article)  # Original Article: This is the original content.
print(cloned_article)    # Cloned Article: This is the original content.
