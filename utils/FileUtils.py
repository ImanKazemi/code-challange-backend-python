import sys


class FileUtils:
    """Class contaions methods for working with files """

    @staticmethod
    def load_txt_file_from_path(file_path):
        """ load a text file from a path"""

        try:
            file_ext = file_path.split(".")[-1]
            if file_ext != 'txt':
                sys.exit(-1)
            else:
                with open(file_path) as file:
                    data = file.readlines()

                return data
        except:
            sys.exit(-1)
