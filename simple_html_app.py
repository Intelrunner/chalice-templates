from chalice import Chalice, Response, BadRequestError

app = Chalice(app_name='city-to-state')
app.debug = True


@app.route('/')
def index():
    return Response(
        body='<html><head></head><body><h1>hello world!</h1></body></html>',
        status_code=200,
        headers={'Content-Type': 'text/html'})  #returns things as text/html
