import os


def create_folders(path, num_folders=20):
    """
    Create a base folder and populate it with a number of subfolders.

    :param path: path of the base folder to create
    :type path: str
    :param num_folders: number of subfolders to create inside the base folder
    :type num_folders: int
    :return: the base folder path
    :rtype: str
    """
    if not os.path.exists(path):
        os.makedirs(path)

    for i in range(num_folders):
        inner_path = os.path.join(path, "dir_" + str(i))
        if not os.path.exists(inner_path):
            os.makedirs(inner_path)

    return path


def read_text_file(file_path):
    """
    Read and return the content of a text file.

    :param file_path: path of the file to read
    :type file_path: str
    :raise FileNotFoundError: if the file does not exist
    :return: the content of the file
    :rtype: str
    """
    with open(file_path, "r") as file:
        return file.read()


def write_text_file(file_path, content, mode="w"):
    """
    Write content to a text file.

    :param file_path: path of the file to write to
    :type file_path: str
    :param content: text content to write
    :type content: str
    :param mode: file mode to open with ("w" to overwrite, "a" to append)
    :type mode: str
    :return: None
    :rtype: None
    """
    with open(file_path, mode) as file:
        file.write(content)
