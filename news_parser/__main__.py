from pprint import pprint

from news_parser.parsing import parse_all_news


def main():
    all_news = parse_all_news("https://mosmetro.ru/press/news/")


if __name__ == '__main__':
    main()