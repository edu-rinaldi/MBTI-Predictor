import json
from os import error
from sys import argv
from enum import Enum
from pprint import pprint

class MBTI(Enum):
    ISTJ = 'ISTJ', 
    ISFJ = 'ISFJ', 
    INFJ = 'INFJ', 
    INTJ = 'INTJ', 
    ISTP = 'ISTP', 
    ISFP = 'ISFP', 
    INFP = 'INFP', 
    INTP = 'INTP', 
    ESTP = 'ESTP', 
    ESFP = 'ESFP',
    ENFP = 'ENFP', 
    ENTP = 'ENTP', 
    ESTJ = 'ESTJ', 
    ESFJ = 'ESFJ', 
    ENFJ = 'ENFJ', 
    ENTJ = 'ENTJ'

    def __str__(self) -> str:
        return self.name

def getPostWithType(data, type : MBTI):
    posts = list(filter(lambda d: d['author_flair_text'] != None and type.value[0] in d['author_flair_text'].upper(), data))
    users = set(map(lambda post: post['author'], posts))
    print(f"- Num. of posts found for {type}: {len(posts)}")
    print(f"- {type} users found: {len(users)}")
    return posts
def main(argv):
    if len(argv) < 2:
        print("path to json needed")
        exit()
    
    file_path = argv[1]
    with open(file_path, 'r', encoding='utf-8') as fp:
        file = json.load(fp)

    scrape_settings = file['scrape_settings']
    data            = file['data']
    print(f"Analyzing:\n- subreddit: {scrape_settings['subreddit']}\n- category: {scrape_settings['category']}\n- num. of results: {scrape_settings['n_results_or_keywords']}\
        \n- time filter: {scrape_settings['time_filter']}")

    print('\n'+'-'*20+'\n')
    a = getPostWithType(data, MBTI.ESFP)


if __name__ == '__main__':
    main(argv)