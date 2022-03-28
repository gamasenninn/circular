import os,sys
from api import app
from flask import send_file

@app.route('/test')
def test():
    return "Hello TEST!"

@app.route('/')
def hello():
    return app.send_static_file('circular.html')

@app.route('/circular')
def rootn():
    return app.send_static_file('circular.html')

@app.route('/images/<no>')
def images(no):
    fpath= f'./data/images/{no}'
    no_image = f'./data/images/0.png'
    #if os.path.isfile(fpath+'.png'):
    #    return send_file(fpath+'png')
    if os.path.isfile(fpath+'.jpg'):
        return send_file(fpath+'.jpg')
    else:
        return send_file(no_image)





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
