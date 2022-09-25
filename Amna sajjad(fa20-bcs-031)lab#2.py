Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 07:18:10) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # Activity 1 
 # Solution: 
 myList1=[] 
 print("Enter objects of first list...") 
 for i in range(5): 
     val=input("enter a value:") 
     n=int(val) 
     myList1.append(n) 
  
 myList2=[] 
 print("Enter objects of second list...") 
 for i in range(5): 
     val=input("Enter a avlue") 
     n=int(val) 
     myList2.append(n) 
  
 list3=myList1+myList2 
 print(list3) 
  
 #Activity 2:
 #Solution 
  
 def isPaindrome(word): 
     temp=word[::-1] 
     if temp.capitalize()==word.capitalize(): 
         return True 
     else: 
         return False 
  
 print(isPaindrome("deed")) 
  
  
 #Activity 3: 
 #Solution: 
 a = [[1, 0, 0], [0, 1, 0], [0, 0, 1] ] 
 b = [[1, 2, 3], [4, 5, 6], [7, 8, 9] ] 
 c=[] 
 for indrow in range (3): 
     c.append([]) 
     for indcol in range (3): 
         c[indrow].append(0) 
         for indaux in range (3): 
             c[indrow][indcol] +=a[indrow][indaux] * b[indcol][indaux] 
  
 print(c) 
  
 #Activity 4:
  
 def perimeter(listing): 
     leng=len(listing) 
     perimeter=0; 
     for i in range(0,leng-1): 
         dist=(((listing[i][0]-listing[i+1][0])**2)+ 
               ((listing[i][1]-listing[i+1][1])*2))*0.5 
         perimeter=perimeter+dist 
     perimeter=perimeter + (((listing[0][0]-listing[leng-1][0])**2) 
                            +((listing[0][1]-listing[leng-1][1])*2))*0.5 
     return perimeter 
  
 L = [1,3],(2,7),(3,9),(-1,8) 
 print(perimeter(L)) 
  
  
 #Activity 5: 
 #Solution: 
  
 #functiopn defined 
 def symmDiff(a,b): 
     e=set()  #empty set 
     for i in a: #for loop used to access in a 
         if i not in b: 
             e.add(i) 
     for i in b: #for loop used to access in b 
         if i not in a: 
             e.add(i) 
     return e 
 set1={0,1,2,4,5} 
 set2={4,5,7,8,9} 
 print(symmDiff(set1,set2)) 
 #verification using inbuilt function 
 print(set1.symmetric_difference(set2)) 
 print(set2.symmetric_difference(set1)) 
 print(set1^set2) 
 print(set2^set1) 
  
  #Activity 6:  
 #Solution: 
  
 sample={("amna","khan"):"0246585468445",("saqib","kh"):"02238238849", 
         ("nimy","ai"):"0246585468445",} 
 firstName=input("enter first name") 
 lastname=input("enter last name") 
  
 searchTuple= (firstName,  lastname) 
 if searchTuple in sample: 
     print(sample[searchTuple]) 
 else: 
     print("name not found")
     print("name not found")
