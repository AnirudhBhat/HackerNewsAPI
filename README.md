# HackerNewsAPI
python wrapper for hackernews api

#Installation
`$ pip install hacker_news`

#Usage
```
import hn
top_posts = hn.get_post()
#print top 10 posts from hacker news
for post in top_posts:
    print post.title
 ```
    

#API
##get_post(post_type, limit)
###parameter: 
  * post_type - any one of [top_posts, new_posts, askhn_posts, showhn_posts, job_posts]. Default value is top_posts.
  * limit - number of posts to return. Default value is 10

##Example
```
import hn
showhn_posts = hn.get_post('showhn_posts', 20)
#print top 20 SHOW HN posts.
for post in showhn_posts:
  print str(post.points), post.title, post.submitter, post.num_comments
```
  
##user(username)

##Example
```
import hn
user = hn.user('abhat38')
print user.name, user.karma, user.about
```

##id(id)

##Example
```
import hn
post = hn.id('8863')
print post.title, post.url
```

#class: Post
Each Post has following attributes
* title - title of the post
* url - url of the post
* domain - domain url of the post
* points - number of votes/points the post has recieved
* submitter - name of the poster
* num_comments - number of comments this post has got
* story_type - type of story

#class: User
Each user has following attributes
* name - name of the user
* created - created time
* karma - karma of the user
* about - brief description of the user
