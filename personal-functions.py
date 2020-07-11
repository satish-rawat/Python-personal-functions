import os


def path_finder(folder_name=None, search_directory=os.getcwd(), file_type='csv'):
    if folder_name is None:
        file_path = []
        for r, d, f in os.walk(search_directory):
            for file in f:
                if file.endswith(file_type):
                    x = file_path.append(os.path.join(r, file))
        return file_path
    else:
        for r, d, f in os.walk(search_directory):
            for directory in d:
                if directory == folder_name:
                    path = os.path.join(r, directory)
                    return f"Folder Found {path}"
                else:
                    pass
            return "Folder not found"