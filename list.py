from datetime import datetime
import sqlite3




#-----------------------------------------------------------------------------------------------------------------------
# _____               _______              ____                _____   ______ 
# |  __ \      /\     |__   __|     /\     |  _ \      /\      / ____| |  ____|
#| |  | |    /  \       | |       /  \    | |_) |    /  \    | (___   | |__   
#| |  | |   / /\ \      | |      / /\ \   |  _ <    / /\ \    \___ \  |  __|  
#| |__| |  / ____ \     | |     / ____ \  | |_) |  / ____ \   ____) | | |____ 
#|_____/  /_/    \_\    |_|    /_/    \_\ |____/  /_/    \_\ |_____/  |______|
#
#Use this portion of the code to setup the env / db
#
#We will create the 
#    Database , 
#    inside which there will be a table with values (thread_id , uid , reminder ,date_time) and some junk demo values
#--------------------------------------------------------------------------------------------------------------------------


def setup_db():
    connection = sqlite3.connect('reminders.db')
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE reminders (
    thread_id TEXT PRIMARY KEY,
    uid TEXT,
    reminder TEXT,
    date_time TEXT
);
''')

    connection.commit()
    connection.close()

def insert_into_db(thread_id , uid , reminder , date_time):
    command = """
INSERT INTO reminders (thread_id, uid, reminder, date_time)
VALUES
    ('{}', '{}', '{}', '{}')
    """.format(thread_id,uid,reminder,date_time)
    runcommands(command)

def runcommands(command):
    connection = sqlite3.connect('reminders.db')
    cursor = connection.cursor()
    cursor.execute(command)

    connection.commit()
    connection.close()

#----------------------------------------------------------------------
#  _____  ____      _______ ____      _      _____  _____ _______ 
# |  __ \|  _ \    |__   __/ __ \    | |    |_   _|/ ____|__   __|
# | |  | | |_) |      | | | |  | |   | |      | | | (___    | |   
# | |  | |  _ <       | | | |  | |   | |      | |  \___ \   | |   
# | |__| | |_) |      | | | |__| |   | |____ _| |_ ____) |  | |   
# |_____/|____/       |_|  \____/    |______|_____|_____/   |_|   
#                                                                 
#    We have the functions to convert the Database into list 
#        COPYING 
#        SORTING
#-----------------------------------------------------------------------




def copy():
    list = []
    connection = sqlite3.connect("reminders.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM reminders")
    rows = cursor.fetchall()
    for i in rows:
        list.append(i)
    return sort(list)


def sort (list):
    for i in range(len(list)):
        for j in range (0, ( len(list)-1) ):
            if (list[j][3] > list[j+1][3]):
                list[j] , list[j+1] = list[j+1],list[j]
    return list
    

    

#---------------------------------------------------------------------------
#  _______ ________   _________    _______ ____        _____  ____   
# |__   __|  ____\ \ / /__   __|  |__   __/ __ \      |  __ \|  _ \  
#    | |  | |__   \ V /   | |        | | | |  | |     | |  | | |_) | 
#    | |  |  __|   > <    | |        | | | |  | |     | |  | |  _ <  
#    | |  | |____ / . \   | |        | | | |__| |     | |__| | |_) | 
#    |_|  |______/_/ \_\  |_|        |_|  \____/      |_____/|____/  
# 
# 
#   This is where we convert a string into a date time format 
#       INPUT :  YYYY-MM-DD-HH-MM-SS
#       OUTPUT : Object of datetime function (which is what we use inside the database)
# 
# 
# 
# 
#    
#----------------------------------------------------------------------------




def modify_reminder(thread_id , uid , reminder): #Or maybe modify this according to how the AI parses it
    
    #uid = input("Enter uid")
    #reminder = input("Enter the contenT of reminder")
    date = input("Enter the date and time of reminder (YYYY-MM-DD-HH-MM-SS) : ")
    date = date.split("-")
    date = datetime(int(date[0]),int(date[1]),int(date[2]),int(date[3]),int(date[4]),int(date[5]))
    insert_into_db(thread_id , uid, reminder, str(date))




    
        

        
    








def schedule(datetime):
    pass