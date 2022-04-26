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

    results = []
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


def get_corpus(records):
    corpus = []
    for record in records:
        corpus.append(record['title'])
    return corpus


def get_top_k(scores, records, k):
    if (k > len(scores)):
        k = len(scores)

    scores_with_idx = [(scores[i], i) for i in range(len(scores))]
    sorted_with_idx = sorted(
        scores_with_idx, key=lambda item: item[0], reverse=True)

    res = []
    for i in range(k):
        res.append(records[sorted_with_idx[i][1]])
    return res


def rank(text, size):
    """
    Fetch top @code{size} docs related to the given @code{text}
    :text str: user input
    :size int: number of relevent docs to return
    :return [{title: str, publicationName: str, doi: str, abstract: str, url: str}]:
        a list of dictionaries, each dictionary contains four keys:
            - title: title of the article
            - publicationName: name of the publisher
            - doi: doi of the article
            - abstract: abstract of the article
            - url: url of the article
    """
    API_RETURN_SIZE = 10
    RE_RULE = '-| '
    URL_TEMPLETE = "https://api.springernature.com/metadata/json?q=keyword:{}&p={}&api_key={}"

    response = requests.get(URL_TEMPLETE.format(
        text, API_RETURN_SIZE, API_KEY))
    records = parse_records(response.json()['records'])

    corpus = [re.split(RE_RULE, doc.lower()) for doc in get_corpus(records)]
    bm25 = BM25Okapi(corpus)
    scores = bm25.get_scores(re.split(RE_RULE, text.lower()))

    return get_top_k(scores, records, size)


if __name__ == "__main__":
    # an example of springer API useage
    url_templete = "https://api.springernature.com/metadata/json?q=keyword:{}&p={}&api_key={}"
    size = 10
    query = "covid 19"
    response = requests.get(url_templete.format(query, size, API_KEY))
    records = parse_records(response.json()['records'])
    split_str = '-| '
    corpus = [re.split(split_str, doc.lower()) for doc in get_corpus(records)]

    bm25 = BM25Okapi(corpus)
    scores = bm25.get_scores(re.split(split_str, query.lower()))
    print(scores)
    print(get_top_k(scores, records, 10000))
