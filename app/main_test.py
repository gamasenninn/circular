from api import app

@app.route('/test')
def test():
    return "Hello TEST!"

@app.route('/')
def hello():
    return "Hello world!"

@app.route('/test-view-r')
def test_view_r():
    return app.send_static_file('test_view_r.html')

@app.route('/test-view-crud')
def test_view_crud():
    return app.send_static_file('test_view_crud.html')

@app.route('/test-view-crud2')
def test_view_crud2():
    return app.send_static_file('test_view_crud2.html')


if __name__ == '__main__':

    app.run(host='0.0.0.0',port=5010)
