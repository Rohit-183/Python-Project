import random

print("Swagat aapka deviyon aur sajanoo")
print("To Kaun Banega Crorepati mein")

user_input1 = input("Enter your name: ")
print(f"Hamare saamne hai {user_input1} ji")
print("Toh chaliye hum Khel ka subhaarmbh karte hai")

rules = """
Aapke screen par ek, ek karke prashn puche jayenge uska aapko sahi jawab dena hai 
phele prashn se 14 prashn hai es khel mein jawab aako A/B/C/D mein he dena hai
"""

print(rules)

levels = ["Rs.5000", "Rs.10,000", "Rs.20,000", "Rs.40,000", "Rs.80,000", "Rs.1,60,000", "Rs.3,20,000", "Rs.6,40,000", "Rs.1,250,000",
          "Rs.2,500,000", "Rs.50,00,000", "Rs.1crore", "Rs.3crore", "Rs.7crore"]

questions = [
    "Current Railway Minister of India is",
    "What does not grow on a tree according to a popular Hindi saying?",
    "Which city is known as the Pink City in India?",
    "Who wrote India's National Anthem?",
    "How many religions are there in India?",
    "When is the National Hindi Diwas celebrated?",
    "How many states are there in India?",
    "Where is India Gate located?",
    "Who wrote Vande Mataram?",
    "Which one of the following places is famous for the Great Vishnu Temple?",
    "The largest Buddhist Monastery in India is located at",
    "Which of the following musical instruments is NOT of foreign origin?",
    "Who among the following was killed during 'Operation Bluestar' of 1984?",
    "Which former Indian President died as a result of a road accident?"
]

options = [
    ["A. Mamta Banarjee", "B. Ram Vilash", "C. Ashwini Vaishnaw", "D. Piyush Goyal"],
    ["A. Money", "B. Flowers", "C. Leaves", "D. Fruits"],
    ["A. Bangalore", "B. Mysore", "C. Jaipur", "D. Kochi"],
    ["A. Rabindranath Tagore", "B. Lal Bahadur Shastri", "C. Chetan Bhagat", "D. RK Narayan"],
    ["A. 6", "B. 7", "C. 8", "D. 9"],
    ["A. 13 September", "B. 14 September", "C. 14 July", "D. 15 August"],
    ["A. 28", "B. 29", "C. 31", "D. 30"],
    ["A. Agra", "B. Punjab", "C. Mumbai", "D. New Delhi"],
    ["A. Sarat Chandra Chattopadhyay", "B. Rabindranath Tagore", "C. Bankim Chandra Chatterjee",
     "D. Ishwar Chandra Vidyasagar"],
    ["A. Bordubar, Indonesia", "B. Bamiyan, Afghanistan", "C. Panja Sahib, Pakistan", "D. Ankorvat, Cambodia"],
    ["A. Sarnath, Uttar Pradesh", "B. Tawang, Arunachal Pradesh", "C. Dharmashala, Himachal Pradesh", "D. Gangtok, Sikkim"],
    ["A. Tabla", "B. Flute", "C. Sitar", "D. Violin"],
    ["A. Baba Santa Singh", "B. Haji Mastan", "C. Jarnail Singh Bhindrawale", "D. Homi Jehangir Bhabha"],
    ["A. Rajendra Prasad", "B. Faqruddin Ali Ahmed", "C. Giani Zail Singh", "D. R. Venkatraman"]
]

answers = ["C", "A", "C", "A", "A", "B", "A", "D", "C", "D", "B", "B", "C", "C"]

# Combine questions, options, and answers into a single list
questions_options_answers = list(zip(questions, options, answers))
# Shuffle the list
random.shuffle(questions_options_answers)

total_winning = 0

for i, level in enumerate(levels):
    question, options, answer = questions_options_answers[i]
    print(f"Aapke screen par {level} ka prashn")
    print(f"{i + 1}. {question}")
    for option in options:
        print(option)

    user_input2 = input("Enter your answer (A/B/C/D), or 'Q' to quit: ").upper()

    if user_input2 == 'Q':
        print("You chose to quit the game.")
        break

    if user_input2 == answer:
        print("Correct answer!")
        total_winning = level
    else:
        print("Wrong answer!")
        print(f"Correct answer was: {answer}")
        break

print(f"You won a total of {total_winning} money.")
