a=[[ " "  for i in range(10)] for i in range(10)]
for i in range(10):
  for j in range(10):
      print(a[i][j],end="")
      print()
      if(j==0 or j==a):
          a[i][j] = "*"
      elif(i==j and i<5):
          a[i][j]= "*"
      elif((i+j==8)and i<5):
          a[i][j] = "*"
          for i in range(10):
              for j in range(10):
                  print(a[i][j], end=" ")
                  print()
         
         
         
          
     