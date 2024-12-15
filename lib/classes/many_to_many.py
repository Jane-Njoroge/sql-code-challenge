class Article:
    def init(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title

@property
def author(self):
    return self._author

@author.setter
def author(self, value):
    if not isinstance(value, Author):
        raise Exception("Author must be an instance of Author.")
    self._author = value

@property
def magazine(self):
    return self._magazine

@magazine.setter
def magazine(self, value):
    if not isinstance(value, Magazine):
        raise Exception("Magazine must be an instance of Magazine.")
    self._magazine = value

@property
def title(self):
    return self._title

@title.setter
def title(self, value):
    if not isinstance(value, str) or len(value) < 5 or len(value) > 50:
        raise Exception("Title must be a string between 5 and 50 characters.")
    self._title = value
class Author:
    def init(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise Exception("Name must be a non-empty string.")
        self._name = name
        self._articles = []

@property
def name(self):
    return self._name

def articles(self):
    return self._articles

def magazines(self):
    return list(set([article.magazine for article in self._articles]))

def add_article(self, magazine, title):
    new_article = Article(self, magazine, title)
    self._articles.append(new_article)
    return new_article

def topic_areas(self):
    if not self._articles:
        return None
    return list(set([article.magazine.category for article in self._articles]))
class Magazine:
    all_magazines = []

def __init__(self, name, category):
    if not isinstance(name, str) or len(name) < 2 or len(name) > 16:
        raise Exception("Name must be a string between 2 and 16 characters.")
    if not isinstance(category, str) or len(category) == 0:
        raise Exception("Category must be a non-empty string.")
    self._name = name
    self._category = category
    self._articles = []
    Magazine.all_magazines.append(self)

@property
def name(self):
    return self._name

@property
def category(self):
    return self._category

@category.setter
def category(self, value):
    if not isinstance(value, str) or len(value) == 0:
        raise Exception("Category must be a non-empty string.")
    self._category = value

def articles(self):
    return self._articles

def contributors(self):
    return list(set([article.author for article in self._articles]))

def article_titles(self):
    if not self._articles:
        return None
    return [article.title for article in self._articles]

def contributing_authors(self):
    if not self._articles:
        return None
    author_counts = {}
    for article in self._articles:
        if article.author not in author_counts:
            author_counts[article.author] = 0
        author_counts[article.author] += 1
    return [author for author, count in author_counts.items() if count > 2]

@classmethod
def top_publisher(cls):
    if not cls.all_magazines:
        return None
    return max(cls.all_magazines, key=lambda mag: len(mag.articles()))
