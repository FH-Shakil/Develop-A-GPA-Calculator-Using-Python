def calculate_grade(marks):
  

  total_marks = sum(marks)

  average_marks = total_marks / len(marks)



  grade = None

  if 0 <= average_marks <= 40:
    grade = 'F'

  elif 41 <= average_marks <= 60:
    grade = 'D'

  elif 61 <= average_marks <= 70:
    grade = 'C'

  elif 71 <= average_marks <= 80:
    grade = 'B'

  elif 81 <= average_marks <= 90:
    grade = 'A'

  elif 91 <= average_marks <= 100:
    grade = 'A+'

  else:
    print("Invalid marks entered. Please enter marks between 0 and 100.")
  return total_marks, average_marks, grade

def main():
  
  subjects = ["Bangla", "English", "Math", "Science"]

  marks = []

  for subject in subjects:

    while True:
      try:

        marks.append(int(input(f"Enter marks for {subject}: ")))

        if not 0 <= marks[-1] <= 100:
          
          print("Invalid marks entered. Please enter marks between 0 and 100.")
        else:
          
          break

      except ValueError:

        print("Invalid input. Please enter an integer.")

  total_marks, average_marks, grade = calculate_grade(marks)

  print(f"Total marks: {total_marks}")

  print(f"Average marks: {average_marks:.2f}")

  print(f"Grade: {grade}")

if __name__ == "__main__":
  
  main()
