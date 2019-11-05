questions = ["what is the capital of France? ","what is the capital of England? ", "what is the capital of Germany? ","what is the capital of Russia? ","what is the capital of Spain? "]
answers = ["Paris","London","Berlin","Moscow","Madrid"]

def ask(score = 0, instance = 0):
    if instance < len(questions):
        user_input = str(input(questions[instance]))
        
        if user_input == answers[instance]:
            print("you're right and you now have %s points" %(str(score +1)))
            ask(score = score + 1, instance = instance + 1)
            
        else:
            print("you are wrong the correct answer was %s" %(answers[instance]))
            ask(score, instance = instance + 1)
            
    else:
        print("you got", score, "out of", len(questions))

ask()
