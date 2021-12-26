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

@app.route('/test-view-crud3')
def test_view_crud3():
    return app.send_static_file('test_view_crud3.html')

@app.route('/test-view-crud4')
def test_view_crud4():
    return app.send_static_file('test_view_crud4.html')

@app.route('/test-view-crud5')
def test_view_crud5():
    return app.send_static_file('test_view_crud5.html')

@app.route('/test-view-circular')
def test_view_circular():
    return app.send_static_file('test_view_circular.html')

@app.route('/test-view-circular2')
def test_view_circular2():
    return app.send_static_file('test_view_circular2.html')

@app.route('/test-view-circular3')
def test_view_circular3():
    return app.send_static_file('test_view_circular3.html')

@app.route('/test-view-circular4')
def test_view_circular4():
    return app.send_static_file('test_view_circular4.html')

@app.route('/test-view-circular5')
def test_view_circular5():
    return app.send_static_file('test_view_circular5.html')

@app.route('/test-view-circular6')
def test_view_circular6():
    return app.send_static_file('test_view_circular6.html')

@app.route('/test-view-circular7')
def test_view_circular7():
    return app.send_static_file('test_view_circular7.html')


if __name__ == '__main__':

    app.run(host='0.0.0.0',port=5010)
