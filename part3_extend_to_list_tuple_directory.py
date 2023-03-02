#I declare that my work contains no examples of misconduct, such as plagarism, or collusion
# Student ID : 20210381(IIT)/18671238(UoW)
# Date : 08/12/2021

def progression_outcomes():
    No_of_progresses = 0
    No_of_trailers = 0
    No_of_retrievers = 0
    No_of_excluded = 0
    list_pass = []
    list_defer = []
    list_fail = []
    while True:
        try:
            Pass = int(input("Please enter your credits at pass: "))
            list_pass.append(Pass)
            if Pass not in range(0,121,20):
                print("Out of range")
                Pass = int(input("Please enter your credits at pass: "))
            Defer = int(input("Please enter your credits at defer: "))
            list_defer.append(Defer)
            if Defer not in range(0,121,20):
                print("Out of range")
                Defer = int(input("Please enter your credits at pass: "))
            Fail = int(input("Please enter your credits at fail: "))
            list_fail.append(Fail)
            if Fail not in range(0,121,20):
                print("Out of range")
                Fail = int(input("Please enter your credits at pass: "))
            if(Pass + Defer + Fail != 120):
                print("Total incorrect")
                continue
            if (Pass == 120) and (Defer == 0) and (Fail == 0):
                print("Progress")
                print()
                No_of_progresses = No_of_progresses + 1
                Total = No_of_progresses + No_of_trailers + No_of_retrievers + No_of_excluded
            if (Pass == 100) and (Defer == 20 or Defer == 0) and (Fail == 20 or Fail== 0):
                print("Progress (module trailer) ")
                print()
                No_of_trailers = No_of_trailers + 1
                Total = No_of_progresses + No_of_trailers + No_of_retrievers + No_of_excluded
            if (Pass == 0 or Pass == 20 or Pass == 40 or Pass == 60 or Pass == 80) and (Defer == 0 or Defer == 20 or Defer == 40 or Defer == 60 or Defer == 80 or Defer == 100 or Defer == 120) and (Fail == 0 or Fail == 20 or Fail == 40 or Fail == 60):
                print("module retriever ")
                print()
                No_of_retrievers = No_of_retrievers + 1
                Total = No_of_progresses + No_of_trailers + No_of_retrievers + No_of_excluded
            if (Pass == 0 or Pass == 20 or Pass == 40) and (Defer == 0 or Defer == 20 or Defer == 40) and (Fail == 80 or Fail == 100 or Fail == 120):
                print("Exclude")
                print()
                No_of_excluded = No_of_excluded + 1
                Total = No_of_progresses + No_of_trailers + No_of_retrievers + No_of_excluded
            print("Would you like to enter another data set?")
            Add_another_data_set = input("Enter 'y' for yes or 'q' to quit and view results: ")
            print()
            if (Add_another_data_set == 'q'):
                break
        except ValueError:
            print("Integer required")
    def Histograms(No_of_progresses,No_of_trailers,No_of_retrievers,No_of_excluded,Total):
        
        print("-------------------------------------------------------------")
        print("Horizontal Histogram")
        print("Progress",No_of_progresses, " : ", "*" * No_of_progresses)
        print("Trailer",No_of_trailers, " : ", "*" * No_of_trailers )
        print("Retriever",No_of_retrievers, " : " , "*" * No_of_retrievers)
        print("Excluded",No_of_excluded, " : ", "*" * No_of_excluded)
        print(Total, " outcomes in total")
        print("-------------------------------------------------------------")
        print("Vertical Histogram")
        print("Progress",No_of_progresses,"","Trailer",No_of_trailers,"","Retriever",No_of_retrievers,"","Excluded",No_of_excluded)

        x="*"
        y=""
        print_progress = False
        print_trailer = False
        print_retriever = False
        print_excluded = False
        while True:
            if No_of_progresses > 0:
                print(f"{x:<13}",end='')
                print_progress = True
                No_of_progresses = No_of_progresses - 1
            else:
               print_progress = False
                
            if No_of_trailers > 0 and (No_of_progresses==0 and print_progress==False):
                print(f"{y:<12}",x,end='')
                print_trailer = True
                No_of_trailers = No_of_trailers - 1
                       
            elif No_of_trailers > 0 and (No_of_progresses==0 and print_progress==True):
                print(f"{x:<12}",end='')
                print_trailer = True
                No_of_trailers = No_of_trailers - 1
                
            elif (No_of_trailers!=0):
                print(f"{x:<10}",end='')
                print_trailer = True
                No_of_trailers = No_of_trailers - 1
            else:
                print_trailer = False
                
            if (No_of_retrievers > 0) and (No_of_progresses == 0 and print_progress==True) and (No_of_trailers == 0 and print_trailer==True):
                print(f"{x:<12}",end='')
                print_retriever = True
                No_of_retrievers = No_of_retrievers - 1

            elif (No_of_retrievers > 0) and (No_of_progresses == 0 and print_progress==False) and (No_of_trailers == 0 and print_trailer==False):
                print(f"{y:<24}",x,end='')
                print_retriever = True
                No_of_retrievers = No_of_retrievers - 1
                
            elif (No_of_retrievers > 0) and (No_of_progresses == 0 and print_progress==False) and (No_of_trailers == 0 and print_trailer==True):
                print(f"{y:<10}",x,end='')
                print_retriever = True
                No_of_retrievers = No_of_retrievers - 1
                
            elif(No_of_retrievers > 0) and (No_of_progresses > 0)and (No_of_trailers == 0):
                print("\t",x,end=' ')
                print_retriever = True
                No_of_retrievers = No_of_retrievers - 1
                
            elif (No_of_retrievers > 0) and (No_of_progresses == 0 and print_progress==False)and (No_of_trailers > 0):
                print(f"{y:<12}",x,end='')
                print_retriever = True
                No_of_retrievers = No_of_retrievers - 1

            elif (No_of_retrievers > 0) and (No_of_progresses > 0)and (No_of_trailers > 0):
                print(f"{x:<12}",end='')
                print_retriever = True
                No_of_retrievers = No_of_retrievers - 1
                
            elif (No_of_retrievers!=0):
                print(f"{x:<12}",end='')
                print_retriever = True
                No_of_retrievers = No_of_retrievers - 1
            else:
                print_retriever = False
                             
            if (No_of_excluded > 0) and (No_of_progresses == 0 and print_progress==True) and (No_of_trailers == 0 and print_trailer==True) and (No_of_retrievers==0 and print_retriever==True):
                print(f"{y:<2}",x,end='')
                print_excluded = True
                No_of_excluded = No_of_excluded - 1

            elif (No_of_excluded > 0) and (No_of_progresses == 0 and print_progress==False) and (No_of_trailers == 0 and print_trailer==False) and (No_of_retrievers==0 and print_retriever==False):
                print(f"{y:<34}",x,end='')
                print_excluded = True
                No_of_excluded = No_of_excluded - 1    

            elif (No_of_excluded > 0) and (No_of_progresses == 0 and print_progress==False)and (No_of_trailers > 0) and (No_of_retrievers >0):
                print(f"{y:<2}",x,end='')
                print_excluded = True
                No_of_excluded = No_of_excluded - 1
                
            elif (No_of_excluded > 0) and (No_of_progresses == 0 and print_progress==False)and (No_of_trailers == 0 and print_trailer==False) and (No_of_retrievers==0 and print_retriever==True):
                print(f"{y:<2}",x,end='')
                print_excluded = True
                No_of_excluded = No_of_excluded - 1

            elif (No_of_excluded > 0) and (No_of_progresses ==0 and print_progress==True)and (No_of_trailers == 0 and print_trailer==False) and (No_of_retrievers==0 and print_retriever==False):
                print(f"{y:<22}",x,end='')
                print_excluded = True
                No_of_excluded = No_of_excluded - 1
                
            elif (No_of_excluded > 0) and (No_of_progresses ==0 and print_progress==True)and (No_of_trailers == 0 and print_trailer==True) and (No_of_retrievers==0 and print_retriever==False):
                print(f"{y:<12}",x,end='')
                print_excluded = True
                No_of_excluded = No_of_excluded - 1
                
            elif (No_of_excluded!=0):
                print(f"{y:<2}",x,end='')
                print_excluded = True
                No_of_excluded = No_of_excluded - 1

            print("")
            if (No_of_progresses==0) and (No_of_trailers==0) and (No_of_retrievers==0) and (No_of_excluded==0) :
                break
        print(Total, " outcomes in total")
    Histograms(No_of_progresses,No_of_trailers,No_of_retrievers,No_of_excluded,Total)
    def list_tuple_directory(list_pass,list_defer,list_fail):
        print("-------------------------------------------------------------")
        print("List/Tuple/Directory")
        Num_of_items=len(list_pass)
        for x in range(Num_of_items):
            if list_pass[x]==120:
                print("Progress -",list_pass[x],list_defer[x],list_fail[x])
                continue
            if (list_pass[x]==100) and (list_defer[x]==0 or list_defer[x]==20)and (list_fail[x]==0 or list_fail[x]==20):
                print("Progress (Module trailer) -",list_pass[x],list_defer[x],list_fail[x])
                continue
            if (list_pass[x]==0)or (list_fail[x]==20)or (list_fail[x]==40)or (list_fail[x]==60):
                print("Module retriever -",list_pass[x],list_defer[x],list_fail[x])
                continue
            if (list_fail[x]==80)or (list_fail[x]==100)or (list_fail[x]==120):
                print("Exclude -",list_pass[x],list_defer[x],list_fail[x])            
    list_tuple_directory(list_pass,list_defer,list_fail)    
progression_outcomes()

