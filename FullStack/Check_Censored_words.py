import urllib.request

def read_text():
        quotes = open(r"C:\Users\Intel\Google Drive\Udacity\Full Stack\AbdoulCoverLetter.txt")
        contents_of_files = quotes.read()
        print(contents_of_files)
        quotes.close()
        check_profanity(contents_of_files)
        

def check_profanity(text_to_check):
    connection = urllib.request.urlopen("http://www.wdylike.appspot.com/?" + urllib.parse.urlencode([('q', text_to_check)]))
    output = connection.read()
    #print(output)
    connection.close()
    if b"true" in output:
            print("Profanity Alert!!!")
    elif b"false" in output:
            print("No profanity found")
    else:
            print("Unable to scan the file. ")
read_text()
