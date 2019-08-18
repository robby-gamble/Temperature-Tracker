temperature_array = []

#This function uses the .append method to add a temperature to the end of the temperature_array.
def A(temperature_array):
    print("What temperature would you like to add.")
    float_temperature = float(input())
    temperature_array.append(float_temperature)
    return temperature_array


#This function uses the .insert method to update the number at a given position. It then uses the .pop method to remove the original temperature.
def E(temperature_array):
    print("Edit reading at which position?")
    position = int(input())
    print("What should the value be at this position?")
    new_value = float(input())
    temperature_array.insert(position - 1, new_value)
    temperature_array.pop(position)
    return temperature_array

#This function prints the temperatures in a structured way. ex: Temperature 1:72.

def P(temperature_array):
    int_i = 0
    while int_i < len(temperature_array):
        print("Temperature " + str(int_i + 1) + ":", temperature_array[int_i])
        int_i += 1
    return


#This function uses the .pop method to remove a value at a selected position.

def R(temperature_array):
    print("Remove reading at which position?")
    position = int(input())
    temperature_array.pop(position-1)
    return temperature_array



def run():
    temperature_array = []

    print("What should the program do?\n[A]dd a reading.\n[E]dit a reading.\n[P]rint existing readings.\n[R]emove a reading.\n[Q]uit.")
    user_input = input()

    while user_input!= str ("Q"):
        if user_input == str ("A"):
            A(temperature_array)
        elif user_input == str ("E"):
            E(temperature_array)
        elif user_input == str ("P"):
            P(temperature_array)
        elif user_input == str ("R"):
            R(temperature_array)

        print("What should the program do?\n[A]dd a reading.\n[E]dit a reading.\n[P]rint existing readings.\n[R]emove a reading.\n[Q]uit.")
        user_input = input()
    print("Goodbye!")



if __name__ == "__main__":
    run()
