import hashlib
import pickle
import os
import json

db="hash.json"

class MF:
  def database(self):
   if not os.path.exists(db) or os.path.getsize(db)==0:
    return {}

   else:
    with open(db,"r") as f:
     database=json.load(f)
    return database

  def save_data(self,data):
   with open(db,"w") as f:
    json.dump(data,f,indent=4)

  def fingerprint(self,file):
   return hashlib.sha256(file.read()).hexdigest()


  def save_fingerprint(self,path):
   if not os.path.exists(path) or os.path.getsize==0:
    print("this file not exists or empty")
   elif path in self.database():
    print("this flie saved")
   else:
    database=self.database()
    with open(path,"rb") as f:
     hash=self.fingerprint(f)
    database[path]={
              "sha256":hash,
              "size":os.path.getsize(path)}
    self.save_data(database)
    print("{√} SAVED FINGERPRINT")


  def check(self,path):
   if not os.path.exists(path):
    print("{×} FILE NOT EXISTS")
   else:
    database=self.database()
    if path in database:
     with open(path,"rb") as f:
      if database[path]["sha256"]==self.fingerprint(f):
       print("{•} file has NO Change")
      else:
       print("{×} file has some change")
    else:
     print("{×} NOT EXISTS")


  def check_all(self):
   not_change=0
   change=0
   database=self.database()
   for path in database:
    with open(path,"rb") as f:
     hash=self.fingerprint(f)
     if(hash==database[path]["sha256"]):
      print(path , "IS NOT CHANGE")
      not_change+=1
     else:
      print(path, "IS CHANGE")
      change+=1
   print("\n")
   print("==========================================")
   print("CHANGE:", change)
   print("NOT CHANGE :", not_change)

  def save_folder_files(self,folder):
   if not os.path.exists(folder) or not os.path.isdir(folder):
    print("THIS folder not exists")
   else:
    for file in os.listdir(folder):
     if os.path.isfile(os.path.join(folder,file)):
      self.save_fingerprint(os.path.join(folder,file))


  def main(self):
   while True:
    print("""


       ####₹₹₹₹₹₹₹₹₹₹₹₹₹₹₹₹₹₹₹₹₹₹₹₹₹₹₹₹₹₹
       #         omp                    #
       ####₹₹₹₹₹₹₹₹₹₹######₹₹₹₹₹₹₹₹₹₹₹₹₹#   

""")
   
    print("1.save file fingerprint")
    print("2.check fingerprint")
    print("3.exit")
    x=input("enter : ")
    if(x=="3"):
     break
    elif(x=="1"):
     file=input("enter file path : ")
     if(file.lower().strip() == "folder"):
      folder=input("enter Folder path : ")
      self.save_folder_files(folder)
     else:
      self.save_fingerprint(file)
    elif(x=="2"):
     file=input(" enter file path :")
     if(file.lower().strip() == "all"):
      self.check_all()
     else:
      self.check(file)
    else:
     print("wrong sentace")

if __name__ =="__main__":
 ok=MF()
 ok.main()
