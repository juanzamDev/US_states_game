import turtle
import pandas
import time

# Set up the turtle screen
screen  = turtle.Screen()
screen.title("U.S States Game")

# Load the map image
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# load CSV file
df = pandas.read_csv("50_states.csv")

# Set count variables
guessed_states = []
number_states_guessed = 0

# Game loop - runs until all states are guessed or user exits
while number_states_guessed < 51:
    
    # Prompt user for a state name
    answer_state = screen.textinput(title=f"{number_states_guessed}/50 States correct", prompt="What's the state name?") # User Choice

    # Loop through all states in the dataframe
    for state in df.state: 
        if answer_state:  # Ensure there is an input to avoid error on NoneType
            lower_answer = answer_state.lower() # Lowercase user answer
            if lower_answer == state.lower(): # Compare states
                if lower_answer in guessed_states: # Check if the state has already been guessed
                    # Display message if state has already been guessed
                    message_turtle = turtle.Turtle()
                    message_turtle = turtle.Turtle()
                    message_turtle.hideturtle()  # Hide the turtle icon
                    message_turtle.penup()  # Prevent drawing lines
                    message_turtle.goto(0, 0)  # Position the turtle at the center of the screen

                    # Write the message
                    message_turtle.write("You should try with a different state", align="center", font=("Arial", 16, "normal"))

                    time.sleep(1) # Wait for 1 seconds
                    message_turtle.clear() # Clear the message
                
                else:
                    # Add new guess to guessed states and increment counter
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

                    # Check if all states have been guessed
                    if len(guessed_states) == 50:
                     
                        # Display completion message
                        message_turtle = turtle.Turtle()
                        message_turtle.hideturtle()  # Hide the turtle icon
                        message_turtle.penup()  # Prevent drawing lines
                        message_turtle.goto(0, 0)  # Position the turtle at the center of the screen
                        message_turtle.color("gold") # Set the text color to gold

                        # Write the message
                        message_turtle.write("Congratulations, you're the smartest person in the world!", align="center", font=("Nunito", 16, "bold"))

                        screen.exitonclick() # Close the game screen on click
                


               
                
                
              
