import threading 
#Threading allows python to execute other code while waiting; this is easily simulated with the sleep function.
#this is for python 3.0 and above version
#for python 2.0 version use import thread
from threading import*
import time

dict={}
#'dict' is the dictionary in which we store data in key value pair 

#for create operation 
#use syntax "create(key_name,value,timeout_value)"
#timeout is optional you can continue by passing two arguments without timeout

def create(key,value,timeout=0):
    if key in dict:
        print("Alert message: this key already presented") 
        #error message: if key already present it display when key is already presented
    else:
        if(key.isalpha()):
        #else it check if the key is alphabets or not 
            if len(dict)<(1024*1020*954) and value<=(16*1000):
                #constraints for file size less than 1GB(1024 * 1024 * (954 bytes) = 1.0003415 gigabytes)
                # and JasonObject value less than 16KB (16 * 1000 bytes =16 kilobyte)
                if timeout==0:
                # if we not given the time out values it default value zero is taken
                    l=[value,timeout]
                else:
                    l=[value,time.time()+timeout]
                if len(key)<=32:
                    #constraints for input key_name capped at 32 characters only
                    dict[key]=l
                    print("message: key-value pair successfully added")
                else:
                    print("error: input key_name capped at 32 characters only")
            else:
                print("error: Memory limit exceeded!! ")
                #error message:diplayed when memory us exceeded limit
        else:
            print("error: Invalind key_name!! key_name must contain only alphabets and no special characters or numbers")
            #error message:Invalind key_name!! key_name must contain only alphabets and no special characters or numbers

#for read operation

            
#use syntax "read(key_name)"
            
def read(key):
    if key not in dict:
        print("error: given key does not presented in datastore. Please enter a valid key") 
        #error message: key not presented
    else:
        b=dict[key]
        if b[1]!=0:
            if time.time()<b[1]:
            #comparing the present time with expiry time
                stri=str(key)+":"+str(b[0]) 
                #to return the value in the format of JasonObject i.e.,"key_name:value"
                return stri
            else:
                print("error: time-to-live of",key,"has expired") 
                #error message:Time expired 
        else:
        #if time is optional else is execute
            stri=str(key)+":"+str(b[0])
            
            return stri
            #display key:value pair

#for delete operation
#use syntax "delete(key_name)"

def delete(key):
    if key not in dict:
        print("error: given key does not exist in database. Please enter a valid key") 
        #error message:key not presented in datastore
    else:
        b=dict[key]
        if b[1]!=0:
            if time.time()<b[1]: 
            #comparing the current time with expiry time
                del dict[key]
                print("key is successfully deleted")
            else:
                print("error: time-to-live of",key,"has expired") 
                # message: time to live of key-value has expired
        else:
            del dict[key]
            print("key is successfully deleted")

#I have an additional operation of update in order to change the value of key before its expiry time if provided

#for modify operation 
#use syntax "modify(key_name,new_value)"

def update(key,value):
    b=dict[key]
    if b[1]!=0:
        if time.time()<b[1]:
            if key not in dict:
                print("error: given key does not exist in datastore. Please enter a valid key") #error message6
            else:
                lists=[]
                lists.append(value)
                lists.append(b[1])
                dict[key]=l
        else:
            print("error: time-to-live of",key,"has expired") #error message5
    else:
        if key not in dict:
            print("error: given key does not exist in datastore. Please enter a valid key") #error message6
        else:
            lists=[]
            lists.append(value)
            lists.append(b[1])
            dict[key]=l
