from api import app
from api import get_members,get_member,create_member,update_member,delete_member
from api import get_circulars,get_circular

@app.route('/test')
def test():
    return "Hello TEST!"




if __name__ == '__main__':

    app.run(host='0.0.0.0',port=5010)
