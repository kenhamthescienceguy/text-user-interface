#TEXT USER INTERFACE PYTHON MODULE BY PATRYK NIEDZWIEDZINSKI


#--
i=0
report_counter=0
report_data=[]
catch=0
show=1
#--


def report(mode, function):
     global report_counter
     global report_data
     global i
     if(mode==0):
          report_data.append(function)
          report_counter+=1
     elif(mode==1):
          while(i<report_counter):
               print(report_data[i])
               i+=1

#DRAW TITLE/HEADER
def title(text, length, char):
    return_value="title('"+text+"', "+str(length)+", '"+char+"')"
    print((int((length-len(text))/2)*char)+text+(int((length-len(text))/2)*char))
    if(length==len((int((length-len(text))/2)*char)+text+(int((length-len(text))/2)*char))):
        return_value=return_value + ": succes"
        report(catch,return_value)
    else:
        return_value="something goes wrong with " + return_value
        report(catch,return_value)

#DRAW MENU OPTION
def menu(number, text, length):
    return_value="menu("+number+", '"+text+"', "+str(length)+")"
    print("|" + str(number) + "." + text + ( (length-2-len(text))*" ")+"|")
    if(length==len("|"+str(number)+"."+text+((length-2-len(text))*" ")+"|")):
        return_value=return_value + ": succes"
        report(catch,return_value)
    else:
        return_value="something goes wrong with " + return_value
        report(catch,return_value)

#DRAW A LINE OF CHAR
def line(char, length):
    return_value= "line('" + char + "', " + str(length) + ")"
    print(char*length)
    if(length==len(char*length)):
        return_value=return_value + ": succes"
        report(catch,return_value)
    else:
        return_value="something goes wrong with " + return_value
        report(catch,return_value)
