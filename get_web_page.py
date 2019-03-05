"""
this file is to get web page and save it to a file,
we use requests.get() function to get a Response object following with
serializing it to a file with the given name
"""

import requests
import pickle
import os.path


def main():
    url, file_name = input("Input url: \n").split()
    response = requests.get(url)
    if os.path.exists(file_name) & os.path.isfile(file_name):
        # todo: there is already a file named file_name
        opt = input("File already exists, replace it? [Y/n]")
        if opt == 'Y' or 'y':
            pass
        elif opt == 'N' or 'n':
            print("Download failed: File exists already")
            exit(1)
        else:
            print("Download failed: Bad argument")
            exit(1)
    with open(file_name, 'wb+') as fp:
        pickle.dump(response, fp, pickle.HIGHEST_PROTOCOL)
    with open(file_name, 'rb') as fp:
        open_response = pickle.load(fp)
        if response == open_response:
            print('Success')
        r = open_response.text
    return

if __name__ == "__main__":
    main()
