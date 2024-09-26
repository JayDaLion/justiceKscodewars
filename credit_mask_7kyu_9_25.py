"""write function 'maskify' to change all but last 4 characters to #

sens_info = input("masking: 'Whats The Number mean mason?' ")
def maskify(s):
    if len(s) <= 4:
        return s
    return "#" * (len(s) - 4) + s[-4:]
masked_info = maskify(sens_info)
print (masked_info)""" 

#bonus timeeeee 8kyu
salaries = int(input("Whats the emplyee's Salary?: "))
bonuses = input("Bonus deserved? 'Yes' or 'No'").lower()
def bonus_time(salaries,bonuses):
    
    if bonuses == "yes":
        return  salaries * 10
    elif bonuses == "no":
        return salaries 
    
final_salary = bonus_time(salaries, bonuses)
print("Final salary:", final_salary)

