#I declare that my work contains no examples of misconduct, such as plagarism, or collusion
# Student ID : 20210381(IIT)/18671238(UoW)
# Date : 08/12/2021


def progression_outcomes():
    while True:
        try:
            Pass = int(input("Please enter your credits at pass: "))
            if Pass not in range(0,121,20):
                print("Out of range")
                print()
                Pass = int(input("Please enter your credits at pass: "))
            Defer = int(input("Please enter your credits at defer: "))
            if Defer not in range(0,121,20):
                print("Out of range")
                print()
                Defer = int(input("Please enter your credits at pass: "))
            Fail = int(input("Please enter your credits at fail: "))
            if Fail not in range(0,121,20):
                print("Out of range")
                print()
                Fail = int(input("Please enter your credits at pass: "))
            if(Pass + Defer + Fail != 120):
                print("Total incorrect")
                print()
                continue
            if (Pass == 120) and (Defer == 0) and (Fail == 0):
                print("Progress")
                print()
            if (Pass == 100) and (Defer == 20 or Defer == 0) and (Fail == 20 or Fail== 0):
                print("Progress (module trailer) ")
                print()
            if (Pass == 0 or Pass == 20 or Pass == 40 or Pass == 60 or Pass == 80) and (Defer == 0 or Defer == 20 or Defer == 40 or Defer == 60 or Defer == 80 or Defer == 100 or Defer == 120) and (Fail == 0 or Fail == 20 or Fail == 40 or Fail == 60):
                print("module retriever ")
                print()
            if (Pass == 0 or Pass == 20 or Pass == 40) and (Defer == 0 or Defer == 20 or Defer == 40) and (Fail == 80 or Fail == 100 or Fail == 120):
                print("Exclude")
                print()
        except ValueError:
            print("Integer required")
            print()
progression_outcomes()


