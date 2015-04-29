import json
import requests

from post import Post
from user import User 

TOP_POSTS_URL = "https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty"
TOP_POSTS_ITEM = "https://hacker-news.firebaseio.com/v0/item/%s.json?print=pretty"
NEW_POSTS_URL = "https://hacker-news.firebaseio.com/v0/newstories.json?print=pretty"
ASK_POSTS_URL = "https://hacker-news.firebaseio.com/v0/askstories.json?print=pretty"
SHOW_POSTS_URL = "https://hacker-news.firebaseio.com/v0/showstories.json?print=pretty"
JOB_POSTS_URL = "https://hacker-news.firebaseio.com/v0/jobstories.json?print=pretty"


def parse_json(limit, json_data):
	posts = []
	for i in range(limit):
		p = Post()
		url = TOP_POSTS_ITEM %(json_data[i])
		item_json_data = json.loads(make_request(url))
		try:
			p.submitter = item_json_data['by']			
			p.points = item_json_data['score']
			p.title = item_json_data['title']
			p.url = item_json_data['url']
			p.story_type = item_json_data['type']
			p.num_comments = item_json_data['descendants']
		except:
			pass
		posts.append(p)
	return posts


def user(name):
	u = User()
	USER_URL = "https://hacker-news.firebaseio.com/v0/user/%s.json?print=pretty"%name
	user_json_data = json.loads(make_request(USER_URL))
	u.name = user_json_data['id']
	u.karma = user_json_data['karma']
	u.about = user_json_data['about']
	return u

def top_posts(limit = 10):
	data = make_request(TOP_POSTS_URL)
	json_data = json.loads(data)
	return parse_json(limit, json_data)

def new_posts(limit = 10):
	data = make_request(NEW_POSTS_URL)
	json_data = json.loads(data)
	return parse_json(limit, json_data)

def ask_posts(limit = 10):
	data = make_request(ASK_POSTS_URL)
	json_data = json.loads(data)
	return parse_json(limit, json_data)

def show_posts(limit = 10):
	data = make_request(SHOW_POSTS_URL)
	json_data = json.loads(data)
	return parse_json(limit, json_data)

def job_posts(limit = 10):
	data = make_request(JOB_POSTS_URL)
	json_data = json.loads(data)
	return parse_json(limit, json_data)


def make_request(url):
	r = requests.get(url).text
	return r


def display_post(story_type = 'top_posts'):
	for p in eval(story_type + '()'):
		print str(p.points) + '----->' + p.title

#display_post('ask_posts')