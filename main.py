def armstrong(number):

  for selnum in range (number):
    armno=0
    numofdigits=len(str(selnum))
    
    for seldigit in str(selnum):
      armno+=int(seldigit)**numofdigits
    if (armno==selnum):
       print (f'{selnum} is an Armstrong number') 
  return



armstrong(10000)