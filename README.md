# HackerNewsAPI
python wrapper for hackernews api

#Installation
`$ pip install hacker_news`

#Usage
`import hn
top_posts = hn.get_post()
# print top 10 posts from hacker news
for post in top_posts:
    print post.title`
    

#API
##get_post(post_type, limit)
###parameter: 
  post_type----->any one of [top_posts, new_posts, askhn_posts, showhn_posts, job_posts]
  limit----->number of posts to return. Default value is 10

##Example
`import hn
showhn_posts = hn.get_post('showhn_posts', 20)
# print top 20 SHOW HN posts.
for post in showhn_posts:
  print str(post.points), post.title, post.submitter, post.num_comments`
  
##user(username)

