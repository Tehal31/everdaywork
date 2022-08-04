
d = {}

size = int(input("Enter total students for maths: "))
for i in range(size):
    
    dict_name = input("Enter the name of student: ")
    d[dict_name] = {}
    mathsmarks = input("Enter marks: ")
  
    d[dict_name][" mathsmarks"] = mathsmarks
   
    



t = {}

size = int(input("Enter total students for english: "))
for i in range(size):
    
    dict_name = input("Enter the name of student: ")
    d[dict_name] = {}
    englishmarks = input("Enter marks: ")
  
    d[dict_name][" englishmarks"] = englishmarks
   
    


m = {}

size = int(input("Enter total students for science: "))
for i in range(size):
    
    dict_name = input("Enter the name of student: ")
    d[dict_name] = {}
    sciencemarks = input("Enter marks: ")
  
    d[dict_name][" sciencemarks"] = sciencemarks
    
avgDictd = {}
for k,v in d.iteritems():
    # v is the list of grades for student k
    avgDictd[k] = sum(v)/ float(len(v))
   
    
avgDictt= {}
for k,v in t.iteritems():
    # v is the list of grades for student k
    avgDictt[k] = sum(v)/ float(len(v))
    
avgDictm= {}
for k,v in m.iteritems():
    # v is the list of grades for student k
    avgDictm[k] = sum(v)/ float(len(v))
      