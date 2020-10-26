gpa=float(input("Enter your GPA"))
num=int(input("Enter the number of lectures"))

if gpa<2.0 and num<47:
  print("Not enough number of lectures and lessons")
elif gpa<2.0 and num>47:
  print("Not enough gpa !")
elif gpa>=2.0 and num<47:
  print("Not enough number of lectures")
else:
  print("Graduated")
