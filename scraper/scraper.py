import praw

import os, re, json, csv
from dotenv import load_dotenv
from praw.reddit import Comment
from prawcore.exceptions import Forbidden, NotFound

types = [
    'istj', 
    'isfj', 
    'infj', 
    'intj', 
    'istp', 
    'isfp', 
    'infp', 
    'intp', 
    'estp', 
    'esfp',
    'enfp', 
    'entp', 
    'estj', 
    'esfj', 
    'enfj', 
    'entj'
    ]

types_re = "(istj|isfj|infj|intj|istp|isfp|infp|intp|estp|esfp|enfp|entp|estj|esfj|enfj|entj)"

subreddits = [
    'mbti'
]
subreddits.extend(types)

def flair_is_valid(flair):
    return flair != None

def closest_mbti(mbti : str):
    if mbti is None:
        return None
    mbti = mbti.lower()
    s = re.search(types_re, mbti)
    return None if s is None else s.group(0)

def scrape_all_users_from_subreddit(subreddit_name: str, out_users : dict, limit : int = None):
    
    for submission in reddit.subreddit(subreddit_name).top("all", limit=limit):
        mbti = closest_mbti(submission.author_flair_text)
        if flair_is_valid(mbti):
            out_users[mbti].add(str(submission.author))

    for comment in reddit.subreddit(subreddit_name).comments(limit=limit):
        mbti = closest_mbti(comment.author_flair_text)
        if flair_is_valid(mbti):
            out_users[mbti].add(str(comment.author))

def scrape_all_posts_from_user(redditor, out_posts : list, type : str, limit : int = None):
    # look for user submissions
    for submission in redditor.submissions.top("all", limit=limit):
        # if there is text
        if submission.selftext != '':
            out_posts += [{"redditor_id": redditor.id, "post" : submission.selftext, "type": type, "text_type": "post"}]
        # else is a link post, so we should take the title
        else:
            out_posts += [{"redditor_id": redditor.id, "post" : submission.title, "type": type, "text_type": "title"}]
    # look for user comments
    for comment in redditor.comments.top("all", limit=limit):
        # empty comment with only mentioning user
        if comment.body.find("u/") == 0:
            continue
        out_posts += [{"redditor_id": redditor.id, "post" : comment.body, "type": type, "text_type": "comment"}]
    


def mbti_users_to_json():
    all_users = {t: set() for t in types}
    # get all users in mbti subreddit
    total = 0
    for subr in subreddits:
        scrape_all_users_from_subreddit(subr, all_users, limit=99999)
        old_total = total
        total = sum(map(lambda k: len(all_users[k]), all_users))
        print(f"Just got +{abs(total - old_total)} new users from {subr}\nWith a total of {total} users")
    
    all_users = dict(map(lambda kv: (kv[0], list(kv[1])) , all_users.items()))
    with open("categorized_users.json", "w", encoding="utf8") as f:
        json.dump(all_users, f)


if __name__ == '__main__':
    load_dotenv()
    
    reddit = praw.Reddit(
        client_id = os.getenv('CLIENT_ID'),
        client_secret = os.getenv('CLIENT_SECRET'),
        password = os.getenv('PASSWORD'),
        user_agent = os.getenv('USER_AGENT'),
        username = os.getenv('REDDIT_USERNAME'),
    )

    try:
        print("Authenticated as {}".format(reddit.user.me()))
    except:
        print("Something went wrong during authentication")

    # mbti_users_to_json()

    # mbti posts to json
    with open("../dataset/categorized_users.json", 'r', encoding="utf8") as f:
        all_users = json.load(f)

    posts = []
    total = 0

    # for each user get last posts
    for type, users in all_users.items():
        # this below is a "filter" in case program crash and so we don't have to restart from zero
        # if type in types[:-3]:
        #     continue
        num_users = len(users)
        print(f"Scraping {num_users} users with type {type}")
        for i, user in enumerate(users):
            try: 
                scrape_all_posts_from_user(reddit.redditor(user), posts, type, limit=100)
            except Forbidden as e:
                print(f"{user} user is forbidden")
            except NotFound as e:
                print(f"{user}'s submission/comment not found")
        old_total = total
        total = len(posts)
        print(f"Found +{abs(total - old_total)} new posts\nWith a total of {total} posts")
        with open("categorized_posts_2.json", "w", encoding='utf8') as f:
            json.dump(posts, f)
    
    
