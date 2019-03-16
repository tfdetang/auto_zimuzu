from flask import Flask, render_template
import feedparser

app = Flask(__name__)


@app.route('/<tvId>/<downloadType>/feeds')
def get_url(tvId, downloadType):
    base_url = 'http://diaodiaode.me/rss/feed/'
    feeds = feedparser.parse(base_url+str(tvId))
    title = feeds['feed']['title']
    items = []
    for i in feeds['entries']:
        try:
            items.append({'title': i['title'], 'link': i[downloadType]})
        except:
            pass
    return render_template('rss_template.html', title=title, items=items)


if __name__ == '__main__':
    app.run(debug=True)
