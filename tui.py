#TEXT USER INTERFACE MODULE BY PATRYK NIEDZWIEDZINSKI

def TITLE(TEXT, LENGTH, CHAR):
	print((int((LENGTH-len(TEXT))/2)*CHAR)+TEXT+(int((LENGTH-len(TEXT))/2)*CHAR))
def MENU(NUMBER, TEXT, LENGTH):
	print("|"+str(NUMBER)+"."+TEXT+((LENGTH-2-len(TEXT))*" ")+"|")