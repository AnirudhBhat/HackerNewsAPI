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

post_types = ['top_posts', 'new_posts', 'askhn_posts', 'showhn_posts', 'job_posts']

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


def get_json(url):
	data = make_request(url)
	json_data = json.loads(data)
	return json_data

def parse_json_for_id(json_data):
	p = Post()
	p.submitter = json_data['by']
	p.points = json_data['score']
	p.title = json_data['title']
	p.url = json_data['url']
	p.story_type = json_data['type']
	p.num_comments = json_data['descendants']
	return p

def user(name):
	u = User()
	USER_URL = "https://hacker-news.firebaseio.com/v0/user/%s.json?print=pretty"%name
	user_json_data = json.loads(make_request(USER_URL))
	u.name = user_json_data['id']
	u.karma = user_json_data['karma']
	u.about = user_json_data['about']
	return u


def id(id):
	url = TOP_POSTS_ITEM %id
	json_data = get_json(url)
	return parse_json_for_id(json_data)


def top_posts():
	json_data = get_json(TOP_POSTS_URL)
	return parse_json(limit, json_data)

def new_posts():
	json_data = get_json(NEW_POSTS_URL)
	return parse_json(limit, json_data)

def askhn_posts():
	json_data = get_json(ASK_POSTS_URL)
	return parse_json(limit, json_data)

def showhn_posts():
	json_data = get_json(SHOW_POSTS_URL)
	return parse_json(limit, json_data)

def job_posts():
	json_data = get_json(JOB_POSTS_URL)
	return parse_json(limit, json_data)


def make_request(url):
	r = requests.get(url).text
	return r

class InvalidPostTypeException(Exception):
	pass

def get_post(post_type = 'top_posts', limit = 10):	
	if post_type not in post_types:
		raise InvalidPostTypeException('invalid post type!')	
	else:
		return eval(post_type + '()')
