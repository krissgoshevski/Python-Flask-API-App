# import app
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
#
# from flask_cors import CORS
#
#
# import secrets
# from flask_cors import CORS
#
#
# CORS(app)
#
# app.config['SECRET_KEY'] = secrets.token_hex(16)
#
# # Db configuration
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/flaskreact'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#
# db = SQLAlchemy(app)
# migrate = Migrate(app, db)
#
#
#
# # from flaskext.mysql import MySQL
# #
# # mysql = MySQL()
# #
# # # Configure the MySQL connection
# # app.config['MYSQL_DATABASE_USER'] = 'username'
# # app.config['MYSQL_DATABASE_PASSWORD'] = 'password'
# # app.config['MYSQL_DATABASE_DB'] = 'database'
# # app.config['MYSQL_DATABASE_HOST'] = 'localhost'
# #
# # mysql.init_app(app)
# #
# # # mysql = MySQL(app)
# #
# #
