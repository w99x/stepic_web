def wsgi_application(environ, start_response):     
    query = environ['QUERY_STRING']
    body = query.replace('&','\n')
    status = '200 OK'
    headers = [('Content-Type', 'text/plain')]
    start_response(status, headers )     
    return [ str.encode(body) ]