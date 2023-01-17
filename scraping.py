#from bottle import route, run, template, redirect, request
from requests import get
from bs4 import BeautifulSoup
# @route("/")
# def index():
#     number1 = get_number1()
#     number2 = get_number1()

#     return template("index", out1=number1, out2=number1)

def get_number1():
    out1=0
    url = ' https://www.amazon.co.jp/s?k=アニメ&rh=n%3A4217521051&__mk_ja_JP=カタカナ&ref=nb_sb_noss'
    response = get(url)
    print(response)
    soup = BeautifulSoup(response.text, "html.parser")
    elems = soup.select("span.a-size-base-plus.a-color-base.a-text-normal")
    for elem in elems:
        out1 = elem.getText()
        print(out1)
    return out1
get_number1()

# def get_number2():
#     url = 'https://crowdworks.jp/public/employees/14218'
#     response = get(url)
#     soup = BeautifulSoup(response.text, "html.parser")
#     elems = soup.select('span.score.feedbacks')
#     for elem in elems:
#         out2 = elem.getText()
#     return out2
# @route('/')
# def hello():
#     return template('view/view')

#run(host='localhost', port=8000, debug=True)
# run(host="localhost", port=1029, debug=True, reloader=True)