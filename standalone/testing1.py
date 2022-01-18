import requests
from contextlib import closing
from breadability.readable import Article

url='https://amp.cnn.com/cnn/business/live-news/stock-market-news-101420/index.html'
SIGNIFICANT_TAGS = (
        "img"
    )
_HTTP_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36 OPR/31.0.1889.174",
    # "User-Agent": "Sumy (Automatic text summarizer) Version/%s" % __version__,
}

def fetch_url(url):
    with closing(requests.get(url, headers=_HTTP_HEADERS)) as response:
        response.raise_for_status()
        document= Article(response.content, url)
        print(document.readable)
        #for paragraph in document.main_text:
            #for text, annotations in paragraph:
                #print(annotations)
                #if document._contains_any(annotations, SIGNIFICANT_TAGS):
                    #words.extend(self.tokenize_words(text))



fetch_url(url)
