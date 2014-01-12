Title: Code Highlight
Author: doubletony
Date: 30 June 2012

## Python Code

Here is a piece of code:

	import wordpresslib
	import time
	import datetime
	oldId = 0
	today = datetime.date.today()
	while True:
	    tomorrow = datetime.date.today()
	    if str(tomorrow) == str(today):
	        tm = time.localtime()
	        print str(tm.tm_hour) + ":"+ str(tm.tm_min)
	        print "sleeping...."
	        time.sleep(300)
	        continue
	    #indicates day updated
	    url = 'blogaddress/xmlrpc.php'
	    wp = wordpresslib.WordPressClient(url, 'username', 'password')
	    wp.selectBlog(0)
	    post = wordpresslib.WordPressPost()
	    title = 'blog_title'
	    post.title =  title
	    content = 'content_of_post'
	    post.description = content
	    idPost = wp.newPost(post, True)
	    cat = []
	    cat.append({'categoryId' : 51, 'isPrimary' : 1})
	    wp.setPostCategories(oldId, cat)
	    oldId = idPost
	    today = datetime.date.today()
	    time.sleep(23*60*60)

Looks sweet!
