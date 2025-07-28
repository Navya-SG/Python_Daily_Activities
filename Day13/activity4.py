previous_meter_reading = int(input("Enter previous reading:"))
current_meter_reading = int(input("Enter current reading:"))
reading = previous_meter_reading - current_meter_reading
if reading<=400:
    Bill = 4.80
elif reading<=500:
    Bill = 6.45
elif reading<=600:
    Bill = 8.55
elif reading<=800:
    Bill = 9.65  
elif reading<=1000:
    Bill = 10.70
else:
    Bill = 11.80 
print(f"Bill Amount: Rs.{reading*Bill}")