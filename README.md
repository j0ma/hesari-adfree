# hesari-adfree

### Introduction 
<code>hesari_adfree.py</code> is a Python script that allows you to read Helsingin Sanomat articles on the command line without seeing 
annoying ads or having to conform to the 5 articles / week policy that the site enforces.

Though mostly born out of frustration with all the distracting features on the <a href="https://www.hs.fi">Helsingin Sanomat website</a>, this script 
was also a great learning opportunity for me. In addition to getting rid of the ads and limitations, I also wanted to code something where I could learn to integrate RSS feeds into Python code, as well as to get better at web scraping using <code>lxml</code> and XPath.

### Disclaimer
The copyright of all the articles belongs to Helsingin Sanomat / Sanoma Group, and no infringements of said copyrights are intentional. When using the script to 
read an article, a scraped copy of the text is downloaded temporarily and displayed on the screen. In other words, the script does not distribute the articles, but 
each user downloads them for their personal use, which is allowed according to the <a href="https://www.hs.fi/kayttoehdot/">Terms & Conditions</a> of HS.

### How to use

Using <code>hesari_adfree.py</code> is rather easy and intuitive once you get the script running.

The main hurdle are the required libraries not included in Python's stdlib: <code>feedparser</code>, <code>requests</code>, and <code>lxml</code>. 
To install these (using <code>pip</code>), please run <code>install_dependencies.py</code> before attempting to run <code>hesari_adfree.py</code>.


### To-Do
As with most hobby projects, this script is a work in progress. Here are some future ideas I will implement and consider:
- <code>nyt.fi</code> XPath needs fixing. It's tied to the name of the article, so another easy fix.
- ~~Implement "go back to previous view" -type functionality~~
- Some other formatting for article text, e.g. Markdown?
