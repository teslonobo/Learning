# Escape Characters
'''\' 	Single Quote 	
   \\ 	Backslash 	
   \n 	New Line 	
   \r 	Carriage Return 	
   \t 	Tab 	
   \b 	Backspace 	
   \f 	Form Feed 	
   \ooo Octal value 	
   \xhh Hex value '''

# This will cause an error
txt = "We are the so-called "Vikings" from the north."
# comment line 13 out

txt = "We are the so-called \"Vikings\" from the north."

# String Slicing
g = "Good day, sir!"
print(g[0:2])

# Slice from the start
print(g[:4])

# Slice to the end
print(g[5:])

# Negative indexing
print(g[-4:-2])