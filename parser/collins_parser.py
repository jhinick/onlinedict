import os.path
import requests
from bs4 import BeautifulSoup

default_file_path_1 = r'../collins_address/address.html'
default_file_path_2 = r'bank.html'


class Example:
    """
    Every <Example> contains a single sentence as an example
    """

    def __init__(self, tag):
        """
        :param tag: <div class="cit type-example>...</div>
        """
        self.a_type = 'unknown'
        self.sentence = None
        self.success = True

        assert tag.name == 'div' and tag['class'] == ['cit', 'type-example']

        self.a_type = tag.span['class'][0]  # <class> attr has multiple values of it will return a list
        self.sentence = tag.span.text


class Hom:
    def __init__(self, tag):
        """
        :param tag: <div class="hom">...</div>
        """
        self.index = None
        self.gramGrp = []  # Usually one, sometimes multiple. Such as 'transitive verb', 'intransitive verb'
        self.sense = []
        self.example = []

        assert tag.name == 'div' and tag['class'] == ['hom']
        self.index = tag.find('span', {'class': 'span sensenum'}).text
        for i in tag.find('span', {'class': 'gramGrp'}).find_all('span', {'class': 'pos'}):
            self.gramGrp.append(i.text)
        for i in tag.find('div', {'class': 'sense'}).find_all('div', {'class': 'def'}):
            self.sense.append(i.text)
        for i in tag.find('div', {'class': 'sense'}).find_all('div', {'class': 'cit type-example'}):
            self.example.append(Example(i))


class Frequency:  # done

    def __init__(self, tag):
        """
        All info we need is stored in the tag <div class="word-frequency-container res_hos res_hot res_hod frenquency-title"> => <span class="word-frequency-img'....>...</span>
        :param tag: <div class="word-frequency-container res_hos res_hot res_hod frenquency-title>...</div>
        """
        self.word = 'unknown'  # attr<data-word>
        self.frequency = 'unknown'  # attr<data-band>
        self.describe = None  # attr<title> A string describing the frequency

        assert tag.name == 'div'
        info_tag = tag.find('span', {'class': 'word-frequency-img'})
        assert info_tag is not None
        self.word = info_tag['data-word']
        self.frequency = info_tag['data-band']
        self.describe = info_tag['title']


class Phrase:
    def __init__(self, tag):
        pass


class CollinsDictentry:
    def __init__(self, tag):
        """
        todo: field, pronounce
        :param tag: <div class="dictentry">...</div>
        """
        self.word = None  # The word's name
        self.field = None  # The field that the meaning is used in
        self.pronounce = None  # todo
        self.frequency = None
        self.form = []
        self.hom = []
        self.phrase = []

        assert tag.name == 'div' and tag['class'] == ['dictentry']

        head = tag.find('div', {'class': 'content-box-header'})
        self.word = head.find('h2', {'class': 'h2_entry'}).find('span', {'class': 'orth'}).text
        self.field = head.find('h2', {'class': 'h2_entry'}).find('span', {'class': 'lbl type-misc'}).text

        # todo: handle pronounce

        self.frequency = Frequency(
            tag.find('div', {'class': 'word-frequency-container res_hos res_hot res_hod frenquency-title'}))
        info = tag.find('div', {'class': 'content definitions cobuild am'})
        for i in info.find('span', {'class': 'form inflected_forms type-infl'}).find_all('span', {'class': 'orth'}):
            self.form.append(i.text)
        for i in info.find_all('div', {'class': 'hom'}):
            self.hom.append(Hom(i))

        # handle phrases
        pass


def parse_from_file(file_path=default_file_path_2):
    with open(default_file_path_2, 'r', encoding='utf-8') as fp:
        tag = BeautifulSoup(fp)
    return tag


give_url = 'https://www.collinsdictionary.com/us/dictionary/english/give'


def parse_from_url(url=give_url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text)
    return soup

def test():
    soup = parse_from_file()
    soup = parse_from_url()
    cit_type_example_tag = soup.find('div', {'class': 'cit type-example'})
    span_quote_tag = cit_type_example_tag.span
    hom = soup.find_all('div', {'class': 'hom'})[0]
    # parse_hom = Hom(hom)
    temp = soup.find('div', {'class': 'dictionary Cob_Adv_US'})
    collinsDictentry = CollinsDictentry(
        soup.find('div', {'class': 'dictionary Cob_Adv_US'}).find_all('div', {'class': 'dictentry'})[0])

    pass


if __name__ == '__main__':
    test()
    exit()
