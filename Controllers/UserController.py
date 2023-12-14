# # user_controller.py
# from flask import Flask, render_template
#
# class UserController:
#     def __init__(self):
#         self.app = Flask(__name__)
#
#         @self.app.route('/users')
#         def get_users():
#             # Dummy data, replace with real data from the database
#             users = [
#                 {'username': 'user1', 'email': 'user1@example.com'},
#                 {'username': 'user2', 'email': 'user2@example.com'},
#                 {'username': 'user3', 'email': 'user3@example.com'},
#             ]
#             return render_template('users.html', users=users)
#
# if __name__ == '__main__':
#     controller = UserController()
#     controller.app.run(debug=True)
