import requests

API_KEY = input("Please enter your API ID : ")
CONTENT_SRC = input("Hello I'm Anil, I can help you to upload your pdisk files."
                    "\nPlease enter or paste the magnet or direct link url here : ")
LINK_TYPE = input("Please enter the what link you are entered here 'magnet/link' : ")
FILE_NAME = input("Please enter the file name : ")
status = True

def user(header):
    res = requests.post("http://linkapi.net/open/create_item", headers=header, params=header)
    if res.status_code == 200:
        print(res.text)

def switch(choice):
    if choice == 1:
        CONTENT_SRC = input("Hello I'm Anil, I can help you to upload your pdisk files."
                            "\nPlease enter or paste the magnet or direct link url here : ")
        LINK_TYPE = input("Please enter the what link you are entered here 'magnet/link' : ")
        FILE_NAME = input("Please enter the file name : ")
        header = {
            'api_key': API_KEY,
            'content_src': CONTENT_SRC,
            'link_type': LINK_TYPE,
            'title': FILE_NAME,
        }
        user(header)
    elif choice == 2:
        exit()
    else:
        print("Please select the valid option :-(")

header = {
    'api_key': API_KEY,
    'content_src': CONTENT_SRC,
    'link_type': LINK_TYPE,
    'title': FILE_NAME,
}

if __name__ == '__main__':
    user(header)
    while status==True:
        choice = input("\n1.Upload file\n"
              "2.Close\nPlease select the options :")

        switch(int(choice))
