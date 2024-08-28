#!/usr/bin/env python3
'''Task 0: Basic Flask app'''

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    """This function returns the rendered template for the index.html page.

    Returns:
        The rendered template for the index.html page.
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run()

# #!/usr/bin/env python3
# '''Task 0: Basic Flask app'''

# from flask import Flask, render_template

# app = Flask(__name__)


# @app.route('/')
# def hello():
#     """html"""
#     return render_template('0-index.html')


# if __name__ == "__main__":
#     app.run()
