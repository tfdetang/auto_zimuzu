try:
    from FlaskApp.FlaskApp import app
except:
    import sys

    sys.path.append('..')
    from FlaskApp import app
from flask import render_template
import feedparser


@app.route('/<tvId>/<downloadType>/feeds')
def get_url(tvId, downloadType):
    base_url = 'http://diaodiaode.me/rss/feed/'
    feeds = feedparser.parse(base_url+str(tvId))
    title = feeds['feed']['title']
    items = []
    for i in feeds['entries']:
        try:
            items.append({'title':i['title'], 'link':i[downloadType]})
        except:
            pass
    return render_template('rss_template.html', title=title, items=items)



