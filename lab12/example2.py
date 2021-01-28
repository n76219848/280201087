class Employee:

    def __init__(self,name,salary):
        self.name= name
        self.salary = salary


    def get_name(self):
        return self.name
    
    def get_salary(self):
        return self.salary

    def set_name(self,name):
        self.name = name
    def set_salary(self,salary):
        self.salary = salary

    def display(self):
        print('The name of employee is',self.name)
        print('The salary of this employee is',self.salary)


class Company:

    def __init__(self,employee_list):
        
        self.employee_list=employee_list

    def get_employee_list(self):
        return self.employee_list

    def set_employee_list(self,employee_list):
        self.employee_list = employee_list


    def add(self,new_employee):
        if isinstance(new_employee,Employee):
            self.employee_list.append(new_employee)

    def display2(self):

        for i in self.employee_list:
            if isinstance(i,Employee):
                i.display()

    def av_salary(self):
        a = 0
        count=0
        for i in self.employee_list:
            a += i.get_salary()
            count+=1
        average = a/count
        return int(average)

            
person1 = Employee('aydan',3000)
person2 = Employee('fexri',4000)
person3 = Employee('elvin',6000)
Beko = Company([person1,person2])

Beko.add(person3)

print(Beko.av_salary())
        
              