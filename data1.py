import json


data1 = {


    'name':'OJ Simpson',
    'age':30,
    'city':'New York, NY',
    'interests':['Traveling','Football','Golf','Running','Videogames','History'],
    'is_student': True

}


with open('data1.json','w') as json_file:
                                                                #Opens (or creates) a file named data1.json
                                                                #'w' mode means write — if the file already exists, it gets overwritten
                                                                #as json_file means you can now refer to that open file object with the name json_file
                                                                #with makes sure the file is properly closed when you’re done (cleaner than manually calling close())

    json.dump(data1, json_file, indent=4)                       #This line converts your Python dictionary (data1) to JSON format and writes it to the file you just opened.
                                                                #dump = write Python data into a JSON file
                                                                #indent=4 = pretty formatting (4 spaces for indentation)
print("You have succefully written to data1.json")