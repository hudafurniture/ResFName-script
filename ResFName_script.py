#--------------------------------
#This script injects the project name to all STK files in the project
#NOTE 1: There need to be a variable PROJECT_NAME in the STK
#NOTE 2: If there is any value inside PROJECT_NAME variable this script will override it
#--------------------------------

import os

filePath = os.getcwd()
projectName =os.path.basename(filePath)
stk_directory = 'stk/'
count = 0

match_string = "NAAM=PROJECT_NAME"
new_text = "NAAM=PROJECT_NAME\nDEFAULT="+projectName
new_text_if_exists = "DEFAULT="+projectName

def replaceText(f):
    global count
    exist = False
    strToReplace=''
    with open(f, 'r') as file:
        filedata = file.read()
        filedata_arr= filedata.split('\n')
        for i in range(len(filedata_arr)):
            if match_string in filedata_arr[i]:
                count+=1   
                strToReplace = filedata_arr[i]
                if i<len(filedata_arr)-1:
                    if "DEFAULT=" in filedata_arr[i+1]:
                        exist=True
                        strToReplace = filedata_arr[i+1]
                break  
                        
      
    if exist==True:            
        filedata = filedata.replace(strToReplace, new_text_if_exists)  
    else:
        filedata = filedata.replace(strToReplace, new_text)  
        
    with open(f, 'w') as file:
      file.write(filedata)
     
      
for filename in os.listdir(stk_directory):
    f = os.path.join(stk_directory, filename)
    if os.path.isfile(f):
        if f.endswith('.STK'):
            replaceText(f)


print("Script finished with no errors! Project name '"+projectName+"' was modified to " + str(count) + " STK files")
