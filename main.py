import os, zipfile
from os.path import abspath

__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"


def clean_cache():
    directory = "cache"
    if not os.path.exists(directory):
        os.makedirs(directory)
    for file in os.listdir(directory):
        os.remove(directory + f"/{file}")


def cache_zip(zip_file, dir_path):
    clean_cache()
    zipfile.ZipFile(zip_file).extractall(dir_path)


def cached_files():
    directory = "cache"
    abs_path = os.path.abspath(directory)
    abs_list = []
    for file in os.listdir(directory):
        abs_list.append(f"{abs_path}\{file}")
    return abs_list


def find_password(cache_listdir):
    for file in cache_listdir:
        with open(file) as my_file:
            datafile = my_file.readlines()
            for line in datafile:
                if "password" in line:
                    return line[line.find(" ") + 1 : line.find(r'"\"')]


if __name__ == "__main__":
    clean_cache()
    cache_zip("data.zip", "cache")
    cached_files()
    find_password(cached_files())