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
states_to_learn = []

# Game loop - runs until all states are guessed or user exits
while number_states_guessed <= 50:
    
    # Prompt user for a state name
    answer_state = screen.textinput(title=f"{number_states_guessed}/50 States correct", prompt="What's the state name? (Type exit to report)").lower() # User Choice
 
    # Check if the user's input is "exit" to quit the guessing game or current process
    if answer_state == "exit":
        # Iterate through each state in the DataFrame column 'state'
        for state in df.state:
            # Convert the state name to lowercase and check if it's not in the list of guessed states
            if not state.lower() in guessed_states:
                # If the state hasn't been guessed, append it to the list of states to learn
                states_to_learn.append(state)
                
                # Create a DataFrame from the list of states to learn with a single column titled 'States to learn'
                data = pandas.DataFrame(states_to_learn, columns=['States to learn'])
                
                # Adjust the DataFrame index to start from 1 for a more human-readable format
                data.index = range(1, len(data) + 1)
                
                # Save the DataFrame to a CSV file, with the index labeled as 'N' starting from 1
                data.to_csv("states_to_learn.csv", index_label="N")
        
        # Break out of the loop or exit the program after saving the CSV file
        break


    # Loop through all states in the dataframe
    for state in df.state: 
        if answer_state:  # Ensure there is an input to avoid error on NoneType
            if answer_state == state.lower(): # Compare states
                if answer_state in guessed_states: # Check if the state has already been guessed
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

                        # screen.exitonclick() # Close the game screen on click