import re

def index():
    with open(r"D:/demo/index.html") as f:
        content = f.read()
    my_stock_info = "哈哈哈哈"
    # 吧index中的这里替换为my_stock_info
    content = re.sub(r"这里", my_stock_info, content)
    return content
def login():
    return "这是login"

URL_FUNC_DICT = {
    "/index.py": index,
    "/login.py": login
}
def application(env, start_response):
    start_response('200 OK',[('Content-Type', 'text/html;charset=utf-8')])
    file_name = env["PATH_INFO"]
    '''if file_name == "/index.py":
        return index()
    elif file_name =="/login.py":
        return  login()
    else:
        return "hellow word,我"
    '''
    func = URL_FUNC_DICT(file_name)
    return func()