import csv


def write_into_cvs(info_list):
    with open('student_info.cvs','a',newline='') as cvs_file:
        writer=csv.writer(cvs_file)

        if cvs_file.tell()==0:
            writer.writerow(['name','age','contact','email'])
        writer.writerow(info_list)


if __name__=='__main__':

    student_num=1
    cond=True
    while cond:
        student_info=input("enter student info of student number {} in the following format(name age contact email): ")
        print("entered info: "+student_info)

        student_info_list=student_info.split(' ')
        print("entered split info: "+str(student_info_list))
        print("\nThe entered info is:\nname: {}\nage: {}\ncontact: {}\nemail: {}".format(student_info_list[0],student_info_list[1],student_info_list[2],student_info_list[3]))
        check=input("Is the entered info correct? yes/no: ")
        if check=="yes":
            write_into_cvs(student_info_list)
            cond_check = input("enter yes/no if you want to enter info of another student")
            if cond_check == "yes":
                cond = True
                student_num+=1
            elif cond_check == "no":
                cond = False
        elif check=="no":
            print("\nplease reenter the info")

