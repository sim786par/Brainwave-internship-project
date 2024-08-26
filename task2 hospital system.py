import pymysql
db=pymysql.connect(host="localhost",user="root",passwd="simran786")

cur=db.cursor()
cur.execute("create database if not exists hospital;")
cur.execute("use hospital;")

cur.execute("create table if not exists patient(p_id int(3) primary key,p_name varchar(30),\
             p_age int(3),doc_assign varchar(30),reg_on date,discharge date);")
cur.execute("create table if not exists doctor(d_id int(3) primary key,name varchar(30),\
              department varchar(30),fees int(10),month_salary int(10));")
cur.execute("create table if not exists user(username varchar(20) ,password varchar(20) primary key);")

print("*************************** WELCOME TO SAVE HUMAN HOSPITAL*************************")

def pas():
      l,u,p,d=0,0,0,0
      uname=input("USERNAME: ")
      while (True):
            print("password must be greater than 7 digit and contain number,alphabet and special character")
            s=input("PASSWORD: ")
            if (len(s) >= 8):
                  for i in s:
                        if (i.islower()):
                              l+=1
                        if (i.isupper()):
                              u+=1
                        if (i.isdigit()):
                              d+=1
                        if (i=="$" or i=="@" or i=="#" or i=="&"):
                              p+=1
            if(l>=1 and u>=1 and p>=1 and d>=1 and l+u+p+d==len(s)):
                  print("valid password")
                  cur=db.cursor()
                  r="insert into user values('%s','%s')"%(uname,s)
                  cur.execute(r)
                  db.commit()
                  print("""
                            REGISTERED SUCCESSFULLY  """)
                  break
            else:
                  print("invalid ")
                  
while (True):
      print("""
                      1.REGISTER
                      2.LOGIN
                      3.EXIT
                                              """)
      x=int(input("enter your choice"))
      if x==1:
            pas()
      elif x==2:
            username=input("USERNAME: ")
            cur.execute("select password from user where username='"+username+"'")
            t=cur.fetchall()
            if t is not None:
                  y=1
                  while y>0:
                        pw=input("PASSWORD: ")
                        cur.execute("select password from user where username='"+username+"'")
                        x=cur.fetchall()
                        o=x[0][0]
                        
                        if o==pw:
                              y=0
                              print("""
                         LOGIN SUCCESSFULL
                                          """)
                        else :
                              print("password is incorect")
                              y+=1
                  
            while (True):
                  print("""

                            1.ADMINISTRATION
                            2.PATIENT
                            3.SIGN OUT
                                                     """)
                  a=int(input("enter your role"))
                  if a==1:
                        print("""
                                   1.DISPLAY DETAILS OF DOCTOR
                                   2.ADD A NEW DOCTOR 
                                   3.REMOVE A DOCTOR 
                                   4.EXIT                       """)
                        b=int(input("enter your choice"))
                        if b==1:
                              cur.execute("select * from doctor;")
                              r=cur.fetchall()
                              print("|D_ID |\t DOCTOR NAME |\tDEPARTMENT \t|\t FEES|\t MONTHLY SALARY|") 
                              for i in r:
                                    print("|{}\t|{}\t\t|{}\t\t|{}\t|{}\t|".format(i[0],i[1],i[2],i[3],i[4]))

                        if b==2:
                              did=int(input("enter doctor id"))
                              name=input("enter doctor name")
                              dep=input("enter department")
                              fee=int(input("enter fees taken"))
                              sal=int(input("enter monthly salary"))
                              s="insert into doctor values(%s,'%s','%s',%s,%s)"%(did,name,dep,fee,sal)
                              cur.execute(s)
                              db.commit()
                              print("""
                                                DETAILS ADDED """)

                        if b==3:
                              name=input("enter name of the doctor that need to delete")
                              s="delete from doctor where name = '%s'"%(name)
                              cur.execute(s)
                              db.commit()
                              print("""
                                                 DELETE SUCCESSFULLY """)

                        if b==4:
                              break
                  if a==2:
                        print("""
                                    1.PATIENT DETAILS
                                    2.ADD PATIENT
                                    3.DISCHARGE PATIENT
                                    4.TREATMENT DETAILS
                                    5.EXIT
                                                            """)
                        c=int(input("enter your choice"))
                        if c==1:
                              name=input("enter name of patient")
                              cur.execute("select * from patient where p_name ='%s'"%(name))
                              r=cur.fetchall()
                              print("| P_ID | PATIENT NAME \t| AGE | DOCTOR ASSIGNED |ENTRY DATE |DISCHARGE DATE |")
                              for i in r:
                                    print("|{}\t|{}\t\t|{}\t|{}\t\t|{}\t|{}\t|".format(i[0],i[1],i[2],i[3],i[4],i[5]))


                        if c==2:
                              pid=int(input("enter patient id"))
                              name=input("enter name of patient")
                              age=int(input("enter age"))
                              doc=input("enter doctor assigned")
                              en=input("enter entry date ")
                              dis=input("enter discharge date")
                              s="insert into patient values(%s,'%s',%s,'%s','%s','%s')"%(pid,name,age,doc,en,dis)
                              cur.execute(s)
                              db.commit()
                              print("""
                                           PATIENT ADDED """)

                        if c==3:
                              name=input("enter name of discharing patient")
                              s="delete from patient where p_name = '%s'"%(name)
                              cur.execute(s)
                              db.commit()
                              print("""
                                            PATIENT DISCHARGED""")
                        if c==4:
                              pid=int(input("enter patient id"))
                              s="select p_id,p_name,reg_on,discharge,name,department,fees from patient,doctor\
                                 where p_id = d_id and p_id = %s"%(pid)
                              cur.execute(s)
                              r=cur.fetchall()
                  
                              print("| P_ID | PATIENT NAME \t| ENTRY DATE | DISCHARGE DATE | DOCTOR ASSIGNED \t| DEPARTMENT\
      | FEES |")
                              for i in r:
                                    print("|{}\t|{}\t\t|{}\t|{}\t|{}\t\t|{}\t\t|{}\t|".format(i[0],i[1],i[2],i[3],i[4],i[5],i[6]))
                              
                        if c==5:
                              break
                              
                  

                  if a==3:
                        break
      else:
            break

      
            
