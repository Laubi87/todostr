FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """ Read a text file and return a list of
    to-do items.
    """
    with open(filepath, "r") as file_local:
        user_todos_local = file_local.readlines()
    return user_todos_local


def write_todos(user_todos_arg, filepath=FILEPATH):
    """ Write the to-do items list in the text file. """
    with open(filepath, "w") as file_local:
        file_local.writelines(user_todos_arg)


if __name__ == "__main__":
    print("Hello")
