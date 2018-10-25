# text-user-interface

#Manual

Defined functions:

1. title(text, char, length) - Draw header/title of interface
	-text - title
	-char - char, which will be used to draw a line
	-length - width of interface

	Example:

	Code:		tui.title("Fancy", "=", 15)

	Output:		=====Fancy=====



2. menu(number, text, length) - draw menu option
	-number - number in menu to choose
	-text - text of menu option
	-length - width of interface

	Example:

	Code:		tui.menu(1, "Doit!", 15)

	Output:		|1. Doit!     |



3. line(char, length) - draw single line of char
	-char - char, which will be used to draw a line
	-length - width of interface

	Example:

	Code:		tui.line("#", 15)

	Output:		###############
