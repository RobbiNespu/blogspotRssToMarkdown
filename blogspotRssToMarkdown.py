# -*- coding: utf-8 -*-
# The MIT License (MIT)
# Copyright (c) 2021 robbinespu@gmail.com
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
# DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
# OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE
# OR OTHER DEALINGS IN THE SOFTWARE.

import feedparser
import os.path
from markdownify import markdownify
from urllib.parse import urlparse
directory = './html/'
# nenez9595.blogspot.com/feeds/posts/default?start-index=3?max-results=500
# nenez9595.blogspot.com/feeds/posts/default?n=1000
# nenez9595.blogspot.com/feeds/posts/default?alt=json
#rss_url = "https://nenez9595.blogspot.com/feeds/posts/default"
#NewsFeed = feedparser.parse(rss_url)
#entry = NewsFeed.entries[1]
#print(entry.keys()) 
# # dict_keys(['id', 'guidislink', 'link', 'published', 'published_parsed', 'updated', 'updated_parsed', 'title', 'title_detail', 'content', 'summary', 'links', 'authors', 'author_detail', 'author', 'gd_image', 'thr_total'])
#print(entry) 

def main():
    # Opening file
    file1 = open('ayam', 'r')
    count = 0
    # Using for loop
    print("Using for loop")
    for line in file1:
        count += 1
        print("Scraping rss feed {}- {}".format(count, line.strip()))
        feed = feedparser.parse(line.strip() )
        items = feed["items"]
        for item in items:
            #print(item)
            time = item[ "published_parsed" ]
            title = item[ "title" ]
            slug = item[ "title" ].replace(' ', '-').lower().replace('?', '').replace('#', '')
            year = str(time.tm_year)
            mon = str(time.tm_mon)
            day = str(time.tm_mday)
            clock= item[ "updated" ]
            #print("Time:"+year + '-' + mon  + '-' + day)
            #print("Title:"+title)
            link = item[ "link" ]
            #print("Link - "+link)
            fileName = year + '-' + mon  + '-' + day + '-' + slug + '.md'
            fileName = fileName.replace('/', '')
            file_path = os.path.join(directory, fileName)
            if not os.path.isdir(directory):
                os.mkdir(directory)
            f = open(file_path,'w')
            value = item["content"][0]['value']
            f.write('---\nlayout: post\ntitle: "' + title + '"\n')
            f.write('\ndate: ' + clock + '\n')
            f.write('draft: false\ntype: post\n')
            f.write('---\n')
            f.write(markdownify(value))
            f.write('\nLink: ['+link+']('+link+')\n')
            f.close()
        print('end')
    # Closing files
    file1.close()

if __name__ == "__main__":
    main()