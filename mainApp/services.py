import datetime
from typing import Any, List, Dict

import feedparser
import pytz

from .models import Feed
from .exceptions import InvalidFeedLink


def parse_feed_articles(feed: Feed) -> List[Dict[str, Any]]:
    """
    parse given feed and return it's articles

    :param feed: Feed object
    :type feed: Feed

    :return articles_data: list of article objects
    :rtype: list
    """

    # parse feed url with feedparser
    content = feedparser.parse(feed.rss_link)

    # check if feed url is valid or raise exception
    if content["version"] == 'rss20' or content["version"] == 'atom10':
        # get feed articles and version
        articles = content["entries"]
        feed_version = content["version"]

        # determine article published date key based on feed version
        if feed_version == 'rss20':
            published = 'published'
            published_parsed = 'published_parsed'
        else:
            published = 'updated'
            published_parsed = 'updated_parsed'

        articles_data = []
        for article in articles:
            datetime_object = datetime.datetime(
                article[published_parsed][0],
                article[published_parsed][1],
                article[published_parsed][2],
                article[published_parsed][3],
                article[published_parsed][4],
                article[published_parsed][5],
                tzinfo=pytz.UTC
            )
            articles_data.append({
                "feed": feed,
                "title": article["title"],
                "summary": article["summary"],
                "link": article["link"],
                "published_str": article[published],
                "published": datetime_object.strftime("%d-%m-%Y, %H:%M:%S"),
            })

        return articles_data
    else:
        raise InvalidFeedLink
