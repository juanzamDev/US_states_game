import turtle
import pandas
import time

screen  = turtle.Screen()
screen.title("U.S States Game")

image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

# load CSV file
df = pandas.read_csv("50_states.csv")

# Set count states
guessed_states = []
number_states_guessed = 0

while number_states_guessed < 51:
    
    answer_state = screen.textinput(title=f"{number_states_guessed}/50 States correct", prompt="What's the state name?") # User Choice

    for state in df.state: 
        if answer_state:  # Ensure there is an input to avoid error on NoneType
            lower_answer = answer_state.lower() # Lowercase user answer
            if lower_answer == state.lower(): # Compare states
                if lower_answer in guessed_states:
                    
                    message_turtle = turtle.Turtle()
                    message_turtle.hideturtle()  # Hide the turtle icon
                    message_turtle.penup()  # Prevent drawing lines
                    message_turtle.goto(0, 0)  # Position the turtle at the center of the screen

                    # Write the message
                    message_turtle.write("You should try with a different state", align="center", font=("Arial", 16, "normal"))

                    # Wait for 2 seconds
                    time.sleep(1)

                    # Clear the message
                    message_turtle.clear()
                
                else:
                    
                    guessed_states.append(state.lower())
                    number_states_guessed += 1 
                    # Append Cordinates in list
                    row = df[df.state == state]
                    x_value = int(row.x)
                    y_value = int(row.y)
                    x_y_value = [x_value, y_value]

                    # Show State in turtle
                    state_name_turtle = turtle.Turtle() 
                    state_name_turtle.hideturtle()  # Hide the turtle icon
                    state_name_turtle.penup()  # Prevent drawing lines
                    state_name_turtle.goto(*x_y_value)  # Move turtle to the correct coordinates
                    state_name_turtle.write(state)  # Write the state name at the location

                  

                    if len(guessed_states) == 50:
                     
                        message_turtle = turtle.Turtle()
                        message_turtle.hideturtle()  # Hide the turtle icon
                        message_turtle.penup()  # Prevent drawing lines
                        message_turtle.goto(0, 0)  # Position the turtle at the center of the screen

                        # Establece el color del texto a dorado
                        message_turtle.color("gold")


                        # Write the messageala
                        message_turtle.write("Congratulations, you're the smartest person in the world!", align="center", font=("Nunito", 16, "bold"))


                        screen.exitonclick()
                


               
                
                
              
