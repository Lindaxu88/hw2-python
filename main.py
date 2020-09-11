# Author: Yeman Xu ybx5148@psu.edu
# Collaborator: Jiahui Lan jzl6335@psu.edu
# Collaborator: Daniel Mikita djm6907@psu.edu
# Collaborator: Chenkuan Liao czl5899@psu.edu
# Section: 1
# Breakout: 8

def getGradePoint (str):
  if   str == "A":
    return 4.0
  elif str == "A-":
    return 3.67
  elif str == "B+":
    return 3.33
  elif str == "B":
    return 3.0
  elif str == "B-":
    return 2.67
  elif str == "C+":
   return 2.33
  elif str == "C":
    return 2.0
  elif str == "D":
    return 1.0
  else:
    return 0.0

if __name__ == "__main__":
  gradepoint=0
  credit=0
  for i in range(1,4):
    ingrade=input(f"Enter your course {i} letter grade: ")
    incredit=int(input(f"Enter your course {i} credit: "))
    gradepoint+=getGradePoint(ingrade)*incredit
    credit+=incredit
    print(f"Grade point for course {i} is: {getGradePoint(ingrade)}")
  print(f"Your GPA is: {gradepoint/credit}")