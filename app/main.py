from api import app

@app.route('/test')
def test():
    return "Hello TEST!"

@app.route('/')
def hello():
    return "Hello world!"

@app.route('/circular')
def rootn():
    return app.send_static_file('circular.html')

@app.route('/test-view-circular')
def test_view_circular():
    return app.send_static_file('test_view_circular.html')

@app.route('/test-view-circular2')
def test_view_circular2():
    return app.send_static_file('test_view_circular2.html')


if __name__ == '__main__':

    app.run(host='0.0.0.0',port=5010)
