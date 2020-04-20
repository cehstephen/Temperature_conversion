print("A simple code to convert the temperature from degree celcius to Ferenheight")
print("Enter the temperature in degree Celcius.")

try:
    user_temp_input = float(input("Temperature: "))

    """ The formular for the conversion is: F = C* 9/5 +32 """
    calculated_result = user_temp_input * 9/5 + 32

    print("The temperature is: " + str(calculated_result))
    """ If you want, you can use the following method:
        print(f"The temperature is:", calculated_result)    
    """     
except ValueError:
    print("Error processing... Please enter only numbers.")

except:
    print("Opps... Something went wrong... try again later.")

