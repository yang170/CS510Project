import requests
from rank_bm25 import BM25Okapi
from secret import API_KEY


def parse_record(records):
    """
    A helper function to parse a record returned by Springer API
    "return [{title: str, citations:}]"
    """
    pass


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
    example_result = [{'title': 'refrence 1', 'publicationName': "Journal of Cell Communication and Signaling", 'dio': '10.1007/978-3-540-46138-8_46',
                       'abstract': 'abstract1', 'url': "https://link.springer.com/article/10.1007/s11888-022-00476-z"},
                      {'title': 'refrence 2', 'publicationName': "Journal of Cell Communication and Signaling", 'dio': '20.1007/978-3-540-46138-8_46',
                       'abstract': 'abstract2', 'url': "https://link.springer.com/article/10.1007/s11888-022-00476-z"}]
    return example_result


if __name__ == "__main__":
    # an example of springer API useage
    url_templete = "https://api.springernature.com/metadata/json?q=keyword:{}&p={}&api_key={}"
    size = 10
    query = "covid"
    response = requests.get(url_templete.format(query, size, API_KEY))
    records = response.json()['records']
    print(records)
