# helloflask 구동 되게 만드는 파일
# helloflask 모듈을 대표하는 파일이다
# 따라서 start_helloflask.py에서 from helloflask.__init__ import app으로 안 가고
# 바로 from helloflask import app 이라 쓸 수 있다

# 주의! 함수명은 중복 안 된다

from flask import Flask , g, request, Response, make_response
from datetime import datetime, date
# Flask : 대문자로 시작함, class!

app = Flask(__name__) # Flask 함수 생성, __name__ == App name
app.debug = True # debug mode on, 상세한 error를 보여준다


###############################################################################################################

def ymd(fmt):
    def trans(date_str):
        return datetime.strptime(date_str, fmt)
    return trans

@app.route('/dt')
def dt():
    datestr = request.values.get('date', date.today(), type=ymd('%Y-%m-%d'))
                             # parametername # default # type(현재 함수가 붙었음 , ymd 함수는 위에 정의되어 있음)
    
    return "우리나라 시간 형식: " + str(datestr)

# date 값을 줬을 때
# http://localhost:5000/dt?date=2020-01-01
# 우리나라 시간 형식: 2020-01-01 00:00:00

# date 값을 주지 않았을 때
# http://localhost:5000/dt
# 우리나라 시간 형식: 2020-08-14

###############################################################################################################
# app.config['SERVER_NAME'] = 'localhost:5000'

# @app.route("/sd")
# def helloworld_local():
#     return "Hellow Local.com!"

# # http://localhost:5000/sd
# # Hellow Local.com!


# @app.route("/sd", subdomain="g")
# def helloworld_g():
#     return "Hello G.Local.com!!!"

# http://g.localhost:5000/sd
# Hello G.Local.com!!!




###############################################################################################################
@app.route('/rp')
def rp():
    # q = request.args.get('q') #(1)
    q = request.args.getlist('q') #(2)
    return "q= %s" % str(q)

#(1)
# http://127.0.0.1:5000/rp?q=123 -> 접속
# q= 123 이라고 출력 됨
#(2)
# http://127.0.0.1:5000/rp?q=hiyoung -> 접속
# q= ['hiyoung'] getlist를 사용하니까 리스트 형태로 출력이 된다
# http://127.0.0.1:5000/rp?q=left%20n%20right&q=%EC%95%A0%EB%82%80%EB%8B%A4&q=%EB%A7%8C%EC%84%B8%EB%A5%B4 -> 접속
# q= ['left n right', '애낀다', '만세르'] 출력


###############################################################################################################
@app.route('/test_wsgi')
def wsgi_test(): # 이것은 실행할 함수
    def application(environ, start_response): # environ == flask의 환경변수들을 담고 있는 놈
        body = 'The request method was %s' % environ['REQUEST_METHOD']
        headers = [ ('Content-Type', 'text/plain'),
                    ('Content-Length', str(len(body))) ] # header의 key:value 에서 value 값은 항상 스트링이 되어야 한다
        start_response('200 OK', headers) # 200 OK == 200 == OK
        return [body]
    
    return make_response(application) # 여기 들어간 application은 사용할 함수

# 함수 속의 함수 == inner function
# http://localhost:5000/test_wsgi 접속, 
# The request method was GET 출력




###############################################################################################################
@app.route('/res1')
def res1():
    custom_res = Response("Custom Response", 200, {'test' : 'ttt'}) 
    return make_response(custom_res)

# start_helloflask.py 실행 후 localhost:5000/res1 접속
# Custom Response 출력
# 200 : /res1으로 접속후, 크롬메뉴-도구더보기-개발자도구-network 탭-res1의 status : 200
# windows hosts파일 위치 : C:\windows\system32\drivers\etc\hosts
# test: ttt는 Response Headers에 위치해있음, 저것은 header임을 알 수 있다
# header == 편지봉투의 뒷쪽에 적혀 있는 것,,?
# header에서 test를 읽어 오면 ttt라는 값이 나온다
# 은밀하게 어떤 정보를 보내고 싶을 때, 저기 200 뒤에 자리에 보내면 된다

# maek_response == Response 객체를 가지고 응답, stream으로 내려보낸다
# stream == 시냇물에 종이배를 하나씩 띄우는 것
# 아래처럼 그냥 string 형태로 보내도 되긴 하지만, 큰 파일이나 큰 데이터를 내보낼 때는 
# 서버, 클라이언트를 가볍게 하기 위해서 make_response를 사용한다



'''
@app.before_request # request 처리하기 전에 니가 한 번 실행해줘, 어떤 요청이 들어와도 befor_request를 탄다
def before_request():
    print("before_request!!!")
    g.str = "한글"  # g == Flask의 객체, 전역변수, global의 g / g : Application Context, 내 서버에 접속하는 사람들이 모두 공유하는 것
                    # 모든 사람들이 str 값은 "한글"이라는 두 글자를 가진다
                    # login 정보와 같은 것들은 Session Context에 속한다
                    # g : 접속자수 같은 것에 사용한다
                    # 서버 사용자들을 한꺼번에 control 하고 싶을 때, g를 사용한다
'''

@app.route("/gg") # route 아무것도 안 줬을 때, / 하나만 준다

def helloworld2():
    return "Hello Flask World!" + getattr(g, 'str', '111') # str에 '한글'이라는 값이 없으면 default로 '111'을 사용한다

# start_helloflask.py를 실행하고 localhost:5000/gg 로 접속하니까
# Hello Flask World!한글 이라고 웹에 출력이 된다



@app.route("/")
def helloworld():
    return "Hello Flask World!!" # request에 대한 response, 응답, 내보내는 것




 