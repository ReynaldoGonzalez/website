from flask_frozen import Freezer
from myapp import app

freezer = Freezer(app, with_static_files=True)

if __name__ == '__main__':
    freezer.freeze()
