import re
import requests
from rank_bm25 import BM25Okapi
from secret import API_KEY


def parse_records(records):
    """
    A helper function to parse a record returned by Springer API
    """
    DEFAULT_TEXT = 'Not avaliable'

    if len(records) == 0:
        return [{'title': DEFAULT_TEXT, 'publicationName': DEFAULT_TEXT,
                 'abstract': DEFAULT_TEXT, 'doi': DEFAULT_TEXT,
                 'url': DEFAULT_TEXT}]

    results = ['title']
    for record in records:
        result = {}
        result['title'] = record.get('title', DEFAULT_TEXT)
        result['publicationName'] = record.get('publicationName', DEFAULT_TEXT)
        result['abstract'] = record.get('abstract', DEFAULT_TEXT)
        result['doi'] = record.get('doi', DEFAULT_TEXT)
        result['url'] = DEFAULT_TEXT
        if 'url' in record:
            result['url'] = record['url'][0].get('value', None)
        results.append(result)
    return results


def rank(text, size):
    """
    Fetch top @code{size} docs related to the given @code{text}
    :text str: user input
    :size int: number of relevent docs to return
    :return [{title: str, publicationName: str, dio: str, abstract: str, url: str}]:
        a list of dictionaries, each dictionary contains four keys:
            - title: title of the article
            - citations: number of times the article has been cited
            - doi: doi of the article
            - abstract: abstract of the article
    """
    API_RETURN_SIZE = 10
    URL_TEMPLETE = "https://api.springernature.com/metadata/json?q=keyword:{}&p={}&api_key={}"

    response = requests.get(URL_TEMPLETE.format(
        text, API_RETURN_SIZE, API_KEY))

    records = parse_records(response.json()['records'])

    return records


if __name__ == "__main__":
    # an example of springer API useage
    url_templete = "https://api.springernature.com/metadata/json?q=keyword:{}&p={}&api_key={}"
    size = 10
    query = "covid"
    response = requests.get(url_templete.format(query, size, API_KEY))
    records = response.json()['records']
    print(parse_records(records))
