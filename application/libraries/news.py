import feedparser
import os


class News:

    def headlines():
        feed = feedparser.parse(os.getenv('TOP_NEWS_RSS_URL'))
        titles = []

        for index in range(10):
            article = feed.entries[index]
            titles.append(article.title)

        titles = str.join(' ', ['%s. %s.' % (index + 1, title) for index, title in enumerate(titles)]);

        return 'Top Headlines Today: %s' % (titles)
