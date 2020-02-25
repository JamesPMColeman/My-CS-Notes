# RSS and Atom

### What are they?
#### From RSS vs Atom
#### by Sathish Easuwaran
##### https://www.saksoft.com/rss-vs-atom/

* RSS stands for Really Simple Syndication
* Both are web syndications
	- meaning they are technologies that allow easy transfer of headlines 
	or small portions of a website to other websites or to a desktop application
* Atom was supposed to be an improvement on RSS but RSS is still more popular

### But what is it actually?
#### From How to Create a RSS Reader App in Java Script
#### by Preethi Ranjit
#####https://www.hongkiat.com/blog/rss-reader-in-javascript/

* RSS and atom feeds are XML documents 
	- The documents are created by the source website
	- Only contains publisher approved content
* Very common for news and blog sites
* Are frequently updated
* Program that retrieve this data are called RSS readers (or Atom readers I guess)

### How does this help us make our own reader?

* The XML document reads like an HTML document
* Is rooted with an <rss> tag
* The document contains basic info
	- title
	- website
	- description
* And also the headlines, posts or articles

### How do we get the feed? 

* Inside the HTML of a web site there will be a <link> tag
	- The <link> tag will contain a type="application/rss+xml"
* We must first fetch the HTML of the desired web site
* Parse it so that we can find the appropriate <link>
	- This should produce the RSS feed's URL


### Great, we've got it. Now what?

* In a similar process to getting the HTML we need to parse the XML 
to a DOM 
* Once we have this document we can loop through all of it's elements 
and using their tags we can decide what we want to do with them.

