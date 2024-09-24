

while True:
        Grade_Calculator = float(round, 2(input("Please enter your score: ")))
        if len(Grade) <= 90:
           print("You have an A!")
           print("Congratulations!")

        elif len(Grade) <= 80:
           print("You have an B!")
           print("Congratulations!")

        elif len(Grade) <= 70:
           print("You have an C!")
           print("You are passing.")
                 
        elif len(Grade) <= 60:
           print("You have an D!")
           print("Needs improvement.")

        elif len(Grade) <= 50:
           print("You have an F.")
           print("You have are failing this course")
           print("Please reach out to your instructor for opportunities for improvement.")
        
        else:
            Grade = input("Please enter your score: ")



        