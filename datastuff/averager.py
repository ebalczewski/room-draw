'''Don't have github installed on the computer I'm working on, so going to run/catch bugs on this code at like 8:45pm Monday.-Emily'''

'''Returns the average of the draw order for a room.'''
def average(list):
  sum=0.0
  for item in list:
    sum+=float(item)
  return int(sum/len(list)) 

'''Returns the standard deviation of the draw order for a room.'''  
def stdev(list):
  avg=average(list)
  sum=0.0
  for item in list:
    sum+=(float(item)-avg)**(2)
  return int((sum/len(list))**(0.5))
  
'''Opens roomdata.csv. Sorts information into a dictionary. Calls avg, stdev functions. Writes to roomCalcs.csv.'''
def main():  
  file = open('roomdata.csv','r')
  
  '''Woot dictionaries. Sherri would be proud.'''
  d={}
  newtext=''
  
  lines = file.readlines()[1:]
  for line in lines:
    values = line.split(",") #creating a list of RM Name, Term, Draw Number, Draw Order per line
    name = values[0]
  
    if name not in d:
      d[name] = [values[3]]
    else:
      d[name].append(values[3])
    
  file.close()
  
  '''Data is way more fun when sorted!'''
  #d.sorted()
  stuff=d.items()
  sorted_stuff=sorted(stuff, key=lambda room:room[0])
  
  '''Writing name, average, standard deviation to new file.'''
  for item in sorted_stuff:
    newline=item[0]+ "," + str(average(item[1])) +"," + str(stdev(item[1])) + "\n"
    newtext+=newline
  
  print newtext
  file = open("roomCalcs.csv","w")
  file.write(newtext)
  file.close()
  
if __name__ == "__main__":
  main()
