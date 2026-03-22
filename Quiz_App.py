Answers = ["Asia", "Pakistan", "Sindh", "Badin", "Abidtown"]
questions = ["Continent" ,"Country" ,"Province" ,"City" ,"Area"]

correct = 0
 
for i in range(len(Answers)):
 q = input(f"In which {questions[i]} do you live : ")
 if(q == Answers[i]):
  print("Correct Answer")
  correct += 1
 else:
  print("Incorrect Answer")

if(correct >= 3):
      print("Pass")
else:
      print("Fail")