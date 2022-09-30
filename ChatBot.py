import json

DATA="ChatBotData.json"
def load_data(filepath):
    try:
        with open("projects\ChatBotData.json", "r") as f :
            data=json.load(f)
            return data
    except:
        return {}
data=load_data(DATA)

while(True):
    def Bot_output():
        Final_output=None
    
        User_Input=(input("Hi ! how can i help you ? : ")).lower()

        list=[]
        #we will be ignoring some words from the list.
        ignore_words=["is" ,"was","are","?","!"]
        #to convert the input into list
        list=(User_Input).split()
        #lets check if the list has the words to be ignored 
        for word in list:
            if word in ignore_words:
                list.remove(word)
        #lets store the keys from json fie to this list 
        abc = []
        for key in data.keys():
            abc.append(key)
        if len(list) >=4:
            for sentence in abc:
                words = sentence.split()
                if (list[0] in words and list[1] in words and (list[2] in data or list[4] in data)):
                    Final_output=data[sentence]
                    print(Final_output)
        elif len(list)==3:
            for sentence in abc:
                words = sentence.split()
                if (list[0] in words and list[1] in words or list[2] in words):
                    Final_output=data[sentence]
                    print(Final_output)
        elif len(list)==2:
            for sentence in abc:
                words = sentence.split()
                if (list[0] in words and list[1] in words):
                   
                    Final_output=data[sentence]
                    print(Final_output)
        elif len(list)==1:
            for sentence in abc:
                words = sentence.split()
                if len(words)==1:
                    if (list[0] in words):
                        Final_output=data[sentence]
                        print(Final_output)
        if Final_output is None:
            print("Sorry I am not able to undetsand you :(")

    def Working():
        Bot_output()   

    Working()



