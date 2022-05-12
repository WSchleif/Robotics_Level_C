from bottle import route, run

@route('/')
def home():
    return '''
<!DOCTYPE html>
<html>
    <body>
    <p>Hello World!</p>
    </body>
</html>
'''

run(host='ip_address', port 8080)