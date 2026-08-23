import pandas as pd

roll_last_two = input("Enter last two digits of roll number: ")

d1 = int(roll_last_two[0])

d2 = int(roll_last_two[1])

categories = ["account", "general", "billing"]

fixed_entries = [

    {

        "question": "what is the annual fee",

        "answer": "The annual fee is charged once every year.",

        "keywords": "fee cost price charge",

        "category": "billing"

    },

    {

        "question": "how to reset password",

        "answer": "Go to login and click on forgot password.",

        "keywords": "password reset login",

        "category": "account"

    },

    {

        "question": "what are your working hours",

        "answer": "We are open from 9 AM to 6 PM.",

        "keywords": "hours timing open time",

        "category": "general"

    },

    {

        "question": "how can i pay the fee",

        "answer": "You can pay the fee using UPI, card or online banking.",

        "keywords": "pay payment upi fee",

        "category": "billing"

    }

]


personalized_entries = []

for d in [d1, d2]:

    category = categories[d % 3]

    if category == "account":

        question = "how can i update my account details"

        answer = "You can update your account details from the account settings."

        keywords = "account update details profile"

    elif category == "general":

        question = "where can i get general information"

        answer = "General information is available on the help page."

        keywords = "general information help"

    else:

        question = "how can i check my billing details"

        answer = "You can check your billing details from the billing section."

        keywords = "billing payment fee invoice"

    personalized_entries.append({

        "question": question,

        "answer": answer,

        "keywords": keywords,

        "category": category

    })


entries = fixed_entries + personalized_entries

df = pd.DataFrame(entries)

print("\nQ1: Final 6-row DataFrame")

print(df)
