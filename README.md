# Higher_Lower
My version of the game Higher Lower.

NOTE: I'm explaining the details from the code as it appears, not in the order which I wrote it, just to clarify.

We start by importing from the gamedata file data, which is a list of dictionaries, that include each of the organizations or celebrities within the game.
Then we import, the random module, which we'll use later on, and the logos: vs and Higher Lower from the art file.
We proceed to the first function that we'll create, which I called format_data with the input of account; this function takes account information from dictionary data, 
separates it in variables, so it can return the information as a string.
Next, we create a second function called user_is_correct, that takes the guess from the user, as well as the follower count for accounts a and b.
Then, we create 2 variables called account_a and account_b, which will be taken from the data list with the random.choice function.
Later, we set the starting score as 0 with a variable, and start a while loop with the flag compare set to True, and we start by declaring that the account_a will be the 
account_b and establish an if statement to get accounts a and b to be different accounts.
Afterwards, we simply print the Higher Lower logo and an f string to declare that we are comparing the account a, using the format_data function.
Then, we print the VS logo followed by another f string stating the other account, also using the format_data function, after that we declare the variable of guess,
as the input for the user to choose between both accounts, and to make sure there are no errors, we use the lower function.
We establish the variables for follower count of each of the accounts, and use them as inputs along with user's guess, into an if statement that checks, if user is 
correct, utilizing the function user_is_correct, which checks if the follower count of a is greater than the other account and if user's guess was a, if so function 
returns True and also an elif in the opposite case.
Lastly, the if statement that uses user_is_correct function sums 1 to the current score, if user was correct, gives feedback to the user in the form of an f string, 
including the current score and should clear the screen for the next guess, otherwise the while loop ends turning compare to False, and gives feeedback to the user,
telling them they're wrong in the form of an f string followed by the final score.
