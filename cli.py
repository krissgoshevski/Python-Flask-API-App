# # cli.py
# import click
# import os
#
# @click.command()
# @click.argument('controller_name')
# def create_controller(controller_name):
#     controller_directory = os.path.join('controllers', controller_name.lower())
#     os.makedirs(controller_directory)
#     controller_file = os.path.join(controller_directory, f"{controller_name.lower()}_controller.py")
#
#     with open(controller_file, 'w') as file:
#         file.write(f"# {controller_name.lower()}_controller.py\n\n"
#                    "def hello_world():\n"
#                    "    return 'Hello from your new controller!'\n")
#
#     click.echo(f"Controller '{controller_name}' created successfully.")
#
# if __name__ == '__main__':
#     create_controller()
