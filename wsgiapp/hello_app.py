def wsgi_application(environ, start_response):     
    # бизнес-логика      
    query = environ['QUERY_STRING']
    body = ""
    for q in query:
        body += '\n'.join([q + '=' + i for i in query[q]]) + '\n'
    status = '200 OK'
    headers = [('Content-Type', 'text/plain')]
    start_response(status, headers )     
    return [ str.encode(body) ]