
import argparse
import requests

from bs4 import BeautifulSoup


def get_args():
    parser = argparse.ArgumentParser()      # parser will hold all the info
    parser.add_argument("dictionary", help="Indicates what dictionary you want to use.")
    parser.add_argument("word_to_search", help="The word you want to look up.")
    args = parser.parse_args()
    return args


def get_webpage(url):
    return requests.get(url)



def get_address(dictionary, word_to_search):
    url = None
    if dictionary == "collins":
        url = "https://www.collinsdictionary.com/us/dictionary/english/" + word_to_search
    return url


def main():
    # print(get_args())
    foo = get_webpage("https://www.collinsdictionary.com/us/dictionary/english/address")
    s = str(foo.headers)

    exit(0)


if __name__ == '__main__':
    main()
