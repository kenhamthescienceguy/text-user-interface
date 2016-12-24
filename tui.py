#TEXT USER INTERFACE PYTHON MODULE BY PATRYK NIEDZWIEDZINSKI


#--
i=0
report_counter=0
report_data=[]
catch=0
show=1
#--


def report(mode, function):
     if(mode==0):
          report_data[report_counter]=function
          report_counter+=1
     elif(mode==1):
          while(i<=report_counter):
               print(report_data[i])

def title(text, length, char):
    return_value="title("+text+", "+str(length)+", "+char+")"
    print((int((length-len(text))/2)*char)+text+(int((length-len(text))/2)*char))
    if(length==(int((length-len(text))/2)*char)+text+(int((length-len(text))/2)*char) ):
        return return_value + ": succes"
    else:
        return "something goes wrong with " + return_value
    fun=title(text,length,char)
    report(catch,fun)

def menu(number, text, length):
    return_value="menu("+number+", "+text+", "+str(length)+")"
    print("|" + str(number) + "." + text + ( (length-2-len(text))*" ")+"|")
    if(length==len("|"+str(number)+"."+text+((length-2-len(text))*" ")+"|")):
        return return_value + ": succes"
    else:
        return "something goes wrong with " + return_value
    fun=menu(number,text,length)
    report(catch,fun)

def line(char, length):
    return_value= "line(" + char + ", " + str(length) + ")"
    print(char*length)
    if(length==len(char*length)):
        return return_value + ": succes"
    else:
        return "something goes wrong with " + return_value
    fun=line(char,length)
    report(catch,fun)
