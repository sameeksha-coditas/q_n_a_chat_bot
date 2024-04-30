from langchain_community.llms import Ollama

# Initialize the LLM
llm = Ollama(base_url='http://localhost:11434', model='llama3')

# Define a function to repeatedly ask a question until a valid response is received
def ask_question(question_text, validation_function):
    while True:
        response = input(question_text)
        if validation_function(response):
            return response
        else:
            print("Invalid response. Please try again.")

# Validation functions
def is_non_empty_string(s):
     # Check if s is an instance of str and not an integer
    if isinstance(s, str) and not s.isdigit():
        # Check if s is not empty after stripping whitespace
        return bool(s.strip())
    return False

def is_valid_gender(gender):
    return gender.lower() in ["male", "female", "other"]

def is_valid_age(age):
    return age.isdigit() and 0 <= int(age) <= 120

# Main function to run the bot
def run_bot():
    print("Hello! I'm here to ask you a few questions.")
    
    name = ask_question("What is your name? ", is_non_empty_string)
    gender = ask_question("What is your gender (male, female, other)? ", is_valid_gender)
    age = ask_question("How old are you? ", is_valid_age)
    
    print(f"Thank you, {name}. You have stated that you are a {age}-year-old {gender}.")
    
    # After predefined questions, allow the user to ask their own questions
    more_questions = input("Would you like to ask me any questions? (yes/no) ")
    if more_questions.lower() == 'yes':
        while True:
            user_question = input("What would you like to ask? ")
            if user_question.lower() in ['exit', 'quit', 'no']:
                print("Goodbye!")
                break
            # Use LLM model to process the question
            response = llm.invoke(user_question)
            print("Answer:", response)

if __name__ == "__main__":
    run_bot()
