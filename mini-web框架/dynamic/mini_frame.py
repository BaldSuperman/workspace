
def index():
    with open(r"D:/demo/index.html") as f:
        content = f.read()
    return content

def login():
    return "这是login"
def application(env, start_response):
    start_response('200 OK',[('Content-Type', 'text/html;charset=utf-8')])
    file_name = env["PATH_INFO"]
    if file_name == "/index.py":
        return index()
    elif file_name =="/login.py":
        return  login()
    else:
        return "hellow word,我"