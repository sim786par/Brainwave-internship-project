import pymysql
db=pymysql.connect(host="localhost",user="root",passwd="simran786")
print("connected successfully")

cur=db.cursor()
cur.execute("create database if not exists library;")
cur.execute("use library;")
print(cur.fetchall())

cur.execute("create table if not exists book(book_code int(10) primary key,\
            book_name varchar(30),\
            subject varchar(30) ,\
            author varchar(20),\
            total_amount int(3));")
cur.execute("create table if not exists issue(issue_code int(5) primary key,\
            user_name varchar(30),\
            book_name varchar(30),\
            noof_book_taken int(2),\
            date_of_return date );")
cur.execute("create table if not exists signup(username varchar(30) not null,\
            password varchar(30)primary key)")


    
def book():
    name=input("enter book name")
    code=int(input("enter book code"))
    sub=input("enter subject")
    author=input("enter author name")
    no=int(input("enter no of books"))
    cur=db.cursor()
    s="insert into book value(%s,'%s','%s','%s',%s)"%(code,name,sub,author,no)
    cur.execute(s)
    db.commit()
    print(name ,"book added")

def issue():
    name=input("enter username")
    code=int(input("ener book code"))
    bname=input("enter book name")
    no=int(input("enter no of books issued"))
    date=input("date of return in YYYY-MM-DD formate")
    cur=db.cursor()
    c="insert into issue values(%s,'%s','%s',%s,'%s')"%(code,name,bname,no,date)
    cur.execute(c)
    db.commit()
    print("book issued")

        
while (True):
    print("***********************\n\t1.SIGN IN \n\t2.LOGIN\n\t3.EXIT\n******************************")
    x=int(input("enter your choice"))
    if x==1:
        uname=input("enter your username")
        pw=input("enter your password")
        verify=input("enter your password again")
        if verify==pw:
            cur=db.cursor()
            s="insert into signup values('%s','%s')"%(uname,pw)
            cur.execute(s)
            db.commit()
            print("signed in")
        else:
            print("wrong password\ntry again")

    elif x!=2:
        break


    else:
        username=input("USERNAME:")
        cur.execute("select password from signup where username='"+username+"'")
        t=cur.fetchall()
        if t is not None:
            pw=input("PASSWORD:")
            cur.execute("select password from signup where username='"+username+"'")
            
            x=cur.fetchall()
            o=x[0][0]
            if o!=pw:
                print("password is incorect")
                break
            elif o==pw:
                print("""
             LOGIN SUCCESSFULL
                              """)
    while (True):
        print("****************************\n\t1.AVAILABLE BOOKS\n\t2.ADD BOOK\n\t3.ISSUE BOOK\
              \n\t4.ISSUE DETAILS\n\t5.DELETE BOOK\n\t6.SEARCH BOOk\n\t7.FINE/DUE\n\t8.EXIT\n********************************")
        x=int(input("enter your choice"))
        if x==1:
            cur=db.cursor()
            cur.execute("select * from book;")
            t=cur.fetchall()
            print("book_code\tbook_name\t\t\t title\t\t\t Author\t\t\t amount_available")
            for i in t:
                print("{}\t\t{}\t\t{}\t\t\t{}\t\t{}".format(i[0],i[1],i[2],i[3],i[4]))
        elif x==2:
            book()
        elif x==3:
            issue()
        elif x==4:
            cur=db.cursor()
            cur.execute("select * from issue;")
            t=cur.fetchall()
            print("book_code\tuser_name\t\tbook_name\t\tno.of_books_taken\tdate_of_return")
            for i in t:
                print("{}\t\t{}\t\t\t{}\t\t\t{}\t\t{}".format(i[0],i[1],i[2],i[3],i[4]))

        elif x==5:
            bcode=int(input("enter book code"))
            c="delete from book where book_code = %s"%(bcode)
            cur.execute(c)
            db.commit()
            print(bcode,"deleted successfully")
        elif x==6:
            bcode=int(input("enter book code"))
            c="select * from book where book_code= %s"%(bcode)
            cur.execute(c)
            t=cur.fetchall()
            print("book_code\tbook_name\t\t subject\t\t Author\t\t amount_available")
            for i in t:
                print("{}\t\t{}\t\t{}\t\t{}\t\t{}".format(i[0],i[1],i[2],i[3],i[4]))

        elif x==7:
            name=input("enter username")
            cur.execute("select * from issue where user_name ='"+name+"'")
            t=cur.fetchall()
            print("book_code\tuser_name\t\tbook_name\t\tno.of_books_taken\tdate_of_return")
            for i in t:
                print("{}\t\t{}\t\t\t{}\t\t\t{}\t\t{}".format(i[0],i[1],i[2],i[3],i[4]))
            
            cur.execute("select * from issue where user_name ='"+name+"' and date_of_return < now()")
            s=cur.fetchall()
            print(s)
            l=[]
            a=list(s)
            
            if a == l:
                print("no due")
            else:
                print(" please submit fine ")

        else:
            break

    
