#TEXT USER INTERFACE PYTHON MODULE BY PATRYK NIEDZWIEDZINSKI

REPORT_COUNTER=0
REPORT_DATA=[]
CATCH=0
SHOW=1

def REPORT(MODE, FUCTION):
     if(MODE==0):
          REPORT_DATA[REPORT_COUNTER]=FUNCTION
          REPORT_COUNTER+=1
     elif(MODE==1):
          while(i<=REPORT_COUNTER):
               print(REPORT_DATA[i])

def TITLE(TEXT, LENGTH, CHAR):
     return_value="TITLE("+TEXT+", "+LENGTH+", "+CHAR+")"
     print((int((LENGTH-len(TEXT))/2)*CHAR)+TEXT+(int((LENGTH-len(TEXT))/2)*CHAR))
     if(LENGTH==(int((LENGTH-len(TEXT))/2)*CHAR)+TEXT+(int((LENGTH-len(TEXT))/2)*CHAR) ):
          return return_value + ": SUCCES"
     else:
          return "Something goes wrong with " + return_value

def MENU(NUMBER, TEXT, LENGTH):
	return_value="MENU("+NUMBER+", "+TEXT+", "+LENGTH+")"
     print("|"+str(NUMBER)+"."+TEXT+((LENGTH-2-len(TEXT))*" ")+"|")
     if(LENGTH==len("|"+str(NUMBER)+"."+TEXT+((LENGTH-2-len(TEXT))*" ")+"|") )
          return return_value + ": SUCCES"
     else:
          return "Something goes wrong with " + return_value

def LINE(CHAR, LENGTH):
     return_value="LINE(”+CHAR+", "+LENGTH")”
     print(CHAR*LENGTH)
