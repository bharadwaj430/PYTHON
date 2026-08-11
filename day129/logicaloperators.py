# and --- returns true if both statements are true---combine statements
# or ---- returns True if one of the statements is true ---- combine statements 
# not --- reverses the result  ,returns false if the result is true---reverse result

age = 25
is_student = False
has_discount_code = True

if (age < 18 or age > 65) and not is_student or has_discount_code:
  print("Discount applies!")  #Discount applies!


