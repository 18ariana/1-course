from bottle import (
    route, run, template, request, redirect
)
from scrapper import get_news
from db import News, session, save
from bayes import NaiveBayesClassifier

@route("/")
@route("/news")
def news_list():
    s = session()
    rows = s.query(News).filter(News.label == None).all()
    return template('news_template', rows=rows)


@route("/add_label/")
def add_label(label="good", id=1):
    s = session()
    label = request.query.label
    id = request.query.id
    row = s.query(News).filter(News.id == id).one()
    row.label = label
    s.commit()
    redirect("/news")


@route("/update")
def update_news():
    news = get_news("https://news.ycombinator.com/newest", 3)
    save(news)
    redirect("/news")


@route("/classify")
def classify_news():
    s = session
    news_with_labels = s.query(News).filter(News.title not in x_title and News.lable != None ).all
    extra_lab = [ row.label for row in news_with_labels ]
    extra_title = [row.title for row in news_with_labels]
    classifier.fit(extra_lab, extra_title)
    news_wout_lab = s.query(News).filter(News.lable == None).all
    x = [row.title for row in news_wout_lab]
    labels = classifier.predict(x)
    for i in range (len(news_wout_lab)):
        news_wout_lab[i].label = labels[i]
    s.commit()
    news_classified = s.query(News).fiter(News.label == 'good').all
    return template('news_template', rows = news_classified)


if __name__ == "__main__":
    s = session()
    classifier = NaiveBayesClassifier()
    news_with_labels = s.query(News).filter(News.label != None).all()
    x_title = [row.title for row in news_with_labels]
    y_lable = [row.label for row in news_with_labels]
    classifier.fit(x_title, y_lable)
    run(host="localhost", port=8080)
