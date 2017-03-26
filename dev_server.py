import os

os.environ['FLASK_DEBUG'] = '1'

from autoapp import app

if __name__ == '__main__':
    app.run()
