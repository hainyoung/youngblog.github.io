# web application 구동시키기위한 파일
# helloflask 폴더 안에 있어도, 밖에 있어도 상관 없다

from helloflask import app # __iinit__.py의 app

app.run(host='127.0.0.1') # == 127.0.0.1 == local host의 ip == 나 자신의 서버


'''
실행시키고 난 후 터미널의 출력

 * Serving Flask app "helloflask" (lazy loading) # lazy : 바로 로딩하진 않겠다, 천천히 필요할 때 올리겠다(IT, software 용어)
 * Environment: production # Environment는 development, production 버전 2가지가 있다, default == production / development == debut mode on, production은 off(서비스 제공중이므로)
   WARNING: This is a development server. Do not use it in a production development.
   Use a production WSGI server instead. # webserver gateway interface == WSGI
 * Debug mode: off
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit) # 서버포트 5000 없이 url을 만들고 싶다면 80 포트를 사용하면 된다
'''