# Write a Python function to get a new string where "Is" has been added to the front. If the given string already begins with "ls" then return the string unchanged
def srtadd(srt):
  if(srt[0:1]=="Is"):
    return(srt)
  else:
    return("Is "+srt)


x=input()
print(srtadd(x))

