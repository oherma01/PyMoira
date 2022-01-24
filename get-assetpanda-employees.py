from mit_moira import Moira
import csv 

# Initialize Moira client with X.509 certificate and private key file
moira = Moira("OUTFILE.cert", "OUTFILE.pem")

def getlist (listname):

    print(Moira.list_exists(moira, listname))

def getlistmembers (listname):

    return Moira.list_members(moira,listname, type='USER', recurse=True, max_results=1000)

def getlistmemberinfo (username):

    #populate user fields
    members = Moira.list_user_info(moira,username)
    return [members["first"] + " " + members["last"], members["mitid"],"",members["userName"]+'@mit.edu',"","","","","","","",""]

def getbulklistmemmberinfo(users):

    arr = []

    for user in users:

        arr.append(getlistmemberinfo(user))

    return arr

def getlistattributes (listname):

    print(Moira.list_attributes(moira, listname))

"""
Output CSV
"""

    
# field names 
fields = ['Name', 'Employee ID', 'Job Title', 'Email', 'Phone', 'Status', 'Jamf Pro ID', 'SCCM ID', 'Images', 'Documents'] 

# data rows of csv file 

userlist = getlistmembers("archall")
rows = getbulklistmemmberinfo(userlist)
    
print(rows)

# name of csv file 
filename = "assetpanda-employees.csv"
    
# writing to csv file 
with open(filename, 'w') as csvfile: 
    
    # creating a csv writer object 
    csvwriter = csv.writer(csvfile) 
        
    # writing the fields 
    csvwriter.writerow(fields) 
        
    # writing the data rows 
    csvwriter.writerows(rows)

