#Function With Outputs

def formated_name(name1,name2):
  formated_name1 = name1.title()
  formated_name2 = name2.title()
  return f" {formated_name1} and {formated_name2} are siblings"

print(formated_name("raj","rohit"))


# @nd way


def formated_name(name1,name2):
  formated_name1 = name1.title()
  formated_name2 = name2.title()
  return f" {formated_name1} and {formated_name2} are siblings"

myname = input("Enter ur Name \n")
sibname = input("Enter ur sibling's Name \n")

print(formated_name(myname,sibname))
