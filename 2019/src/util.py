import os


def read_input(file_name: str) -> str:
    file_path = os.path.join(os.path.dirname(__file__), '../resource/' + file_name)
    with open(file_path) as fp:
        line = fp.readline()
        while line:
            yield line
            line = fp.readline()