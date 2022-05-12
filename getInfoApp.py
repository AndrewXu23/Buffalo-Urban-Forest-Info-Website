# Application code
# build a routine to get information from csv into this python function
import csv
treeFile = "tree.csv"
#open the dataset file, building a emoty dictionary and put tree's population and ecosystem value into the results that show be showed
def get_Tree(content):
    result = {}
    result["x"] = []
    result["y"] = []
    with open(treeFile, newline='') as f:
        reader = csv.reader(f)
        input = content["name"];
        for record in reader:
          if str(record[1]) == str(input):
            result["class"] = record[0]
            result["number"] = record[2]
            result["value"] = record[3] 
    with open(treeFile, newline='') as f:
        reader = csv.reader(f)
        for temp in reader:
          if "class" in result and temp[0] == result["class"]:  
            result["x"].append(temp[2])
            result["y"].append(temp[3])
        print(result)    
    return result


