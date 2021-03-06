#!/usr/local/bin/python

config = {
	"directory": "../pblog", # Your markdown files and the output go here. No trailing slash.
	"site_url": "http://www.cse.msu.edu/~wangyua6/", # site URL including an ending backslash.
	"site_title": "Watch back!", # used for the RSS feed's title.
	"site_description": "Why serious?!", # used for the RSS feed's description.
	"google_analytics_tag": "UA-33129226-1", # used to track the site with Google Analytics.
	"author_name": "doubletony",
	"author_bio_link": "http://www.cse.msu.edu/~wangyua6/", # relative or absolute depending on where you keep it.
	"amazon_tag": " ", # Your tag to Amazon, used in the article footer and RSS feed.
	"twitter_tag": "doubletony", # The twitter tag to which you want tweeted articles referenced.
	"author_email": "doubletony@gmail.com", # The feedback email address.
	"sidebar_on_article_pages": False, # Show the sidebar on all pages. Anything but 1 will only show it on the homepage.
	"minify_html": False, # set to True to remove line breaks from the HTML output for speed
}

youyanEmbed="""
<!-- UY BEGIN -->

<div class="uyan_comment" id="uyan_frame"></div>
<script type="text/javascript" id="UYScript" src="http://v1.uyan.cc/js/iframe.js?UYUserId=1641150" async=""></script>
<!-- UY END -->
"""
youyanEmbed=""

disqusEmbed ="""
        <div id="disqus_thread"></div>
        <script type="text/javascript">
            /* * * CONFIGURATION VARIABLES: EDIT BEFORE PASTING INTO YOUR WEBPAGE * * */
            var disqus_shortname = 'dtegrblog'; // required: replace example with your forum shortname

            /* * * DON'T EDIT BELOW THIS LINE * * */
            (function() {
                var dsq = document.createElement('script'); dsq.type = 'text/javascript'; dsq.async = true;
                dsq.src = 'http://' + disqus_shortname + '.disqus.com/embed.js';
                (document.getElementsByTagName('head')[0] || document.getElementsByTagName('body')[0]).appendChild(dsq);
            })();
        </script>
"""

dMathJaxEmbed="""
<script type="text/javascript"
   src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>
"""

MathJaxEmbed="""
     <script type="text/x-mathjax-config">
      MathJax.Hub.Config({
      tex2jax: {
      inlineMath: [ ['$','$'] ],
      processEscapes: true
      }
      });
    </script>

    <script type="text/x-mathjax-config">
      MathJax.Hub.Config({
      tex2jax: {
      skipTags: ['script', 'noscript', 'style', 'textarea', 'pre', 'code']
      }
      });
    </script>

    <script type="text/x-mathjax-config">
      MathJax.Hub.Queue(function() {
      var all = MathJax.Hub.getAllJax(), i;
      for(i=0; i < all.length; i += 1) {
   all[i].SourceElement().parentNode.className += ' has-jax';
   }
   });
</script>

    <script type="text/javascript"
    src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML">
    </script>
"""

codeHighlight="""
<link rel="stylesheet" href="http://yandex.st/highlightjs/7.0/styles/monokai.min.css">
<script src="http://yandex.st/highlightjs/7.0/highlight.min.js"></script>
"""

prettyprintCSS="sons-of-obsidian.css"

nonentryfiles = [] # a list of text files you DON'T want to process.

# Pueblo: Python Markdown Static Blogger
#
# License:
#
# Copyright (c) 2012 Michael E. Shea, http://mikeshea.net/pueblo.html
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#
# 12 March 2012
#
# A single Python script to build a simple blog from a directory full of markdown files.
#
# This script requires the Markdown python implementation available at:
# http://pypi.python.org/pypi/Markdown/2.1.0
#
# This script requires markdown files using the following multimarkdown metadata as the first three lines
# of the processed markdown files as follows:
#
# Title: the Title of your Document
# Author: Joe Blow
# Date: 15 December 2011
#
# The program will generate an index.html homepage file, an archive.html archive file, 
# and an index.xml RSS file.
#
# Header and footer data can be edited in the variables throughout the program. 
#
# This script expects the following additional files:
# style.css: The main site's stylesheet.
# iphone.css: The mobile version of the site's stylesheet.
# sidebar.html: A secondary set of data usually displayed as a sidebar.
#
# Instructions
# Install the Markdown python module.
# Configure this script by changing the configuration variables below.
# Put your static markdown files in the configured directory
# Run the script either manually, with a regular cronjob, or as a CGI script.
# View the output at index.html
#
# Updated 12 March 2012: Removed header image. Text is good enough, 
#  better for SEO, and faster.
#
# Updated 29 March 2012: Removed iPhone stylesheet. Use @media in the CSS
#
# Updated 31 May 2012: Removed Twitter tag. Let them do their own advertising.


# Main Program
import glob
import re
import rfc822
import time
import cgi
import datetime
import markdown
from time import gmtime, strftime, localtime, strptime

def rebuildsite ():
	textfiles = glob.glob(config["directory"]+"//*.md")
	for nonfile in nonentryfiles:
		textfiles.remove(config["directory"]+"/"+nonfile)
	indexdata = []
	
	# Rip through the stack of markdown files and build HTML pages from it.
	for eachfile in textfiles:
		eachfile = eachfile.replace(config["directory"]+"\\", "")
		content = open(eachfile).read()
		lines = re.split("\n", content)
		title = re.sub("(Title: )|(  )", "", lines[0])
		title = cgi.escape(title)
		urltitle = title.replace("&", "%26")
		author = lines[1].replace("Author: ","")
		date = re.sub("(  )|(\n)|(Date: )","",lines[2])
		date = date.strip()
		numdate = strftime("%Y-%m-%d", strptime(date, "%d %B %Y"))

		skip_index = content.find('\n') + 1
		skip_index = content[skip_index:].find('\n') + 1 + skip_index
		skip_index = content[skip_index:].find('\n') + 1 + skip_index
		#content = markdown.markdown(re.sub("(Title:.*\n)|(Author:.*\n)|(Date:.*\n\n)|    ", "", content))
		content = markdown.markdown(content[skip_index:])
		summary = re.sub("<[^<]+?>","", content)
		summary = summary.replace("\n", " ")[0:80]
		htmlfilenamefull = htmlfilename = eachfile.replace(".md", ".html")
		htmlfilename = htmlfilename.replace(config["directory"]+"/", "")
		postname = htmlfilename.replace(".html", "")
		# Build the HTML file, add a bit of footer text.
		htmlcontent = [buildhtmlheader("article", title, date)]
		htmlcontent.append(content)
		htmlcontent.append(buildhtmlfooter("article", urltitle))
		htmlfile = open(htmlfilenamefull, "w")
		htmlfile.write(minify("".join(htmlcontent)))
		htmlfile.close()
		if numdate <= datetime.datetime.now().strftime("%Y-%m-%d"):
			indexdata.append([[numdate],[title],[summary],[htmlfilename],[content]])

	# The following section builds index.html, archive.html and index.xml.	
	indexdata.sort()
	indexdata.reverse()
	indexbody=archivebody=rssbody=""
	count=0
	
	for indexrow in indexdata:
		dateobject = strptime(indexrow[0][0], "%Y-%m-%d")
		rssdate = strftime("%a, %d %b %Y 06:%M:%S +0000", dateobject)
		nicedate = strftime("<span class='day'>%d</span> <span class='month'>%b</span> <span class='year'>%Y</span>", dateobject)
		articleitem = '''
<h2><a href="%(article_link)s">%(article_title)s</a></h2>
<p><span class='date'>%(date)s</span> %(summary)s...<a href="%(article_link)s"> [more]</a></p>
'''		% {
		'article_link': indexrow[3][0],
		'article_title': indexrow[1][0],
		'date': nicedate,
		'summary': indexrow[2][0],
		}

		rssitem = '''
<item>
<title>%(title)s</title>
<link>%(link)s</link>
<guid>%(link)s</guid>
<pubDate>%(pubdate)s</pubDate>
<description>%(description)s</description>
<content:encoded>
<![CDATA[%(cdata)s]]>
</content:encoded>
</item>
'''		% {
		'title': indexrow[1][0],
		'link': config["site_url"]+indexrow[3][0],
		'pubdate': rssdate,
		'description': indexrow[2][0],
		'cdata': indexrow[4][0],
		}

		count = count + 1
		if count < 15:
			rssbody = rssbody + rssitem
		if count < 4:
			indexbody = indexbody+articleitem
		archivebody = archivebody + articleitem
	sidebardata = open(config["directory"]+"/sidebar.html").read()
	rssdatenow = rfc822.formatdate()
	
	indextitle = config["site_title"]

	indexdata = [buildhtmlheader("index", indextitle, "none")]
	indexdata.append(indexbody)
	indexdata.append("<h2><a href=\"archive.html\">View All %(article_count)s Articles</a> and <a href=\"http://www.cse.msu.edu/~wangyua6/\">even older Articles</a> </h2>\n" 
		% { 'article_count': str(count) })
	indexdata.append("Powered by <a href=\"http://mikeshea.net/pueblo.html\">Pueblo</a>")
	indexdata.append(buildhtmlfooter("index", ""))
	indexfile = open(config["directory"]+"/index.html", "w").write(minify("".join(indexdata)))

	archivedata = [buildhtmlheader("archive", config["site_title"]+" Article Archive", "none")]
	archivedata.append(archivebody)
	archivedata.append(buildhtmlfooter("archive", ""))
	archivefile = open (config["directory"]+"/archive.html", "w").write(minify("".join(archivedata)))

	rsscontent = '''<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0"
xmlns:atom="http://www.w3.org/2005/Atom"
xmlns:content="http://purl.org/rss/1.0/modules/content/"
xmlns:dc="http://purl.org/dc/elements/1.1/\"
>

<channel>
<title>%(site_title)s</title>
<link>%(site_url)s</link>
<description>%(site_description)s</description>
<pubDate>%(rssdatenow)s</pubDate>
<language>en</language>
<atom:link href="%(site_url)sindex.xml" rel="self" type="application/rss+xml" />
%(rssbody)s
</channel>
</rss>
'''	% {
	'site_url': config["site_url"],
	'site_title': config["site_title"],
	'site_description': config["site_description"],
	'rssdatenow': rssdatenow,
	'rssbody': rssbody,
	}
	
	rssfile = open(config["directory"]+"/index.xml", "w").write(minify(rsscontent))
		
# Subroutine to build out the page's HTML header
def buildhtmlheader(type, title, date):
	htmlheader = ['''
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">	
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>%(title)s</title>
<link rel="stylesheet" type="text/css" href="style.css">
<link href="%(prettyprintCSS)s" type="text/css" rel="stylesheet" />
<script type="text/javascript" src="prettify.js"></script>
<link rel="alternate" type="application/rss+xml" title="%(title)s" href="index.xml">
<meta name="viewport" content="user-scalable=yes, width=device-width" />
<script type="text/javascript">
var _gaq = _gaq || [];
_gaq.push(['_setAccount', '%(google_analytics_tag)s']);
_gaq.push(['_trackPageview']);
(function() {  var ga = document.createElement('script');
 ga.type = 'text/javascript';
 ga.async = true;
ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
var s = document.getElementsByTagName('script')[0];
s.parentNode.insertBefore(ga, s);
})();
</script>
%(LatexInjection)s
%(CodeHighlight)s
</head>
<body onload="prettyPrint()">
''' 	% {
		'title': title, 
		'google_analytics_tag': config["google_analytics_tag"],
		'LatexInjection':MathJaxEmbed,
		'CodeHighlight':codeHighlight,
		'prettyprintCSS':prettyprintCSS,
		} ]

	if config["sidebar_on_article_pages"] != True and type == "article":
		htmlheader.append("\n<div class=\"article_container\">\n")
	else:
		htmlheader.append("\n<div class=\"container\">\n")

	if type == "index":
		htmlheader.append('''
<div class="index_header">
<h1>%(site_title)s</h1>
<p class="site_description">%(site_description)s</p>
</div>
''' 	% {
		'site_title': config["site_title"],
		'site_description': config["site_description"],
		} )
	else:
		htmlheader.append('''
<p class="return_link">
<a href="index.html">Back to home</a>
</p>
'''		% {
		'site_title': config["site_title"]
		} )

	# What does the rest of the header look like for each page type?
	if type == "index":
		htmlheader.append("\n<div class=\"article_list\">\n")
	elif type == "archive":
		htmlheader.append("\n<div class=\"article_list\">\n<h1>Article Archive</h1>\n")
	elif type == "article":
		htmlheader.append('''
<div class="article">
<h1>%(title)s</h1>
<p>by <a href="%(author_bio_link)s">%(author_name)s</a> on %(date)s</p>
'''		% {
		'author_bio_link': config["author_bio_link"],
		'title': title,
		'author_name': config["author_name"],
		'date': date,
		} )
	return "".join(htmlheader)

# Remove all line breaks for minified HTML and XML output.
def minify(content):
	if config["minify_html"]:
		content = re.sub("\n","",content)
	return content
	
# Subroutine to build out the footer.
def buildhtmlfooter (type, urltitle):
	footer_parts = []
	if type == "article":
		footer_parts.append("\n</div>")
		footer_parts.append(youyanEmbed)
		#footer_parts.append(disqusEmbed)
		footer_parts.append(
'''
<div class="article">
<p>Send feedback to <a href="mailto:%(email)s">%(email)s</a></p>
<p>Powered by <a href="http://mikeshea.net/pueblo.html">Pueblo</a></p>
'''		% {
		'email': config['author_email'], 
		'urltitle': urltitle,
		})
	footer_parts.append("</div>")

	sidebardata = open(config["directory"]+"/sidebar.html").read()

	if type == "index" or type == "archive" or config["sidebar_on_article_pages"]:
		footer_parts.append(sidebardata)
	footer_parts.append("\n</body>\n</html>")

	return "".join(footer_parts)

# This program is designed to run as a CGI script so you can rebuild your site by hitting a URL.
# print "Content-type: text/html\n\n"
rebuildsite()
# print "<html><head><title>Site Rebuilt</title></head><body><h1>Site Rebuilt</h1></body></html>"
