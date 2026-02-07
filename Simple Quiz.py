#Simple Quiz App – Ask users multiple-choice or true/false questions and keep track of scores
def quiz_app():
    score=0
    questions=[
        {"question":"Q1-->What is the value of 12÷4+3×2?",
         "option":['A.9','B.6','C.12','D.10'],
         "answer":'A'
        },
        {
             "question":"Q2-->6What is the square root of 144",
             "option":['A.9','B.13','C.12','D.10'],
             "answer":"C"
        },
        {
             "question":"Q3-->Which number is not a prime number?",
             "option":['A.4','B.5','C.6','D.8'],
             "answer":"B"
        },
        {
             "question":"Q4-->Who is known as the Father of the Nation in India?",
             "option":['A.Jawaharlal Nehru','B.Sardar Patel','C.Mahatma Gandhi','D.Subhas Chandra Bose'],
             "answer":"C"
        },
        {
             "question":"Q5-->What is the capital of Australia?",
             "option":['A Sydney','B Melbourne','C Canberra','D Perth'],
             "answer":"C"
        }
        ]
    
    for q in questions:
        print('\n'+q["question"])
        for opt in q["option"]:
         print(opt)
        answer=input("enter the answercin(A,B,C,D):").upper()  
        if answer==q['answer']:
            print("correct answer!!")
            score+=2
        else:
             print("incorrect!!") 
             score+=-1
    print("your score is:",score)

quiz_app()    