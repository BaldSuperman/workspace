
def application(envirom, start_response):
    start_response('200 OK',[('Content-Type', 'text/html')])
    return "hellow word"