# hesari_adfree

### Introduction 
hesari_adfree.py is a Python script that allows you to read Helsingin Sanomat articles on the command line without seeing annoying ads or having to conform to the 
annoying 5 articles / week policy the site has.

Though mostly born out of frustration with all the unnecessary bells and whistles on the <a href="https://www.hs.fi">site</a>, this script also was a great learning opportunity for me. In addition to getting rid of the ads and limitations, I also wanted to code something where I could learn to integrate RSS feeds into Python code, as well as to get better at web scraping using <code>lxml</code> and XPath.

### Disclaimer
The copyright of all the articles belongs to Helsingin Sanomat / Sanoma Group, and no infringements of said copyrights are intentional. When using the script to read an article, a scraped copy of the text is downloaded temporarily and displayed on the screen. In other words, the script does not distribute the articles, but each user downloads them for their personal use.

### How to use
Using <code>hesari_adfree</code> is rather easy and intuitive once you get the script running. In order to do that, you should have <code>feedparser</code>, <code>collections</code>, <code>textwrap</code>, <code>lxml</code>, <code>requests</code>, <code>time</code>, <code>sys</code>, and <code>os</code> installed before running the script. 

Some of these are installed by default, but using <code>pip install package_name</code> should work on the missing ones.

### To-Do
As with most hobby projects, this script is a work in progress. Here are some future ideas I will implement and consider:
- When choosing an article, typing in <code>0</code> will actually return the last article because of Python's indexing functionality. This needs to be fixed ASAP. (lol :D)
- Implement "go back to previous view" -type functionality
- Some other formatting for article text, e.g. Markdown?
