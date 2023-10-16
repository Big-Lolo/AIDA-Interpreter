import json
from difflib import get_close_matches
from incorporations.functions import extract_alarm_information, set_alarm  ##Funcion para sacar el argumento de tiempode una oración.
import asyncio


def load_knowledge_base(file_path:str) -> dict:
    with open(file_path, 'r') as file:
        data:dict = json.load(file)
    return data


def save_knowledge_base(file_path:str, data: dict):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)

def find_best_match(user_question: str, questions: list[str]) -> str| None:
    matches: list = get_close_matches(user_question, questions, n=1, cutoff=0.6)
    return matches[0] if matches else None


def get_answer_for_question(question: str, knowledge_base: dict) -> str | None:
    for q in knowledge_base["questions"]:
        if q["question"] == question:
            return q["answer"], (q["function"] if q["function"] else None)
        
async def chat_bot():
    knowledge_base: dict = load_knowledge_base('knowledge_base.json')

    while True:
        user_input: str = input(f'{knowledge_base["systemInfo"]["user_name"]}: ')

        if user_input.lower() == 'quit':
            break

        best_match: str | None = find_best_match(user_input, [q["question"] for q in knowledge_base["questions"]])

        if best_match:
            answer, function = get_answer_for_question(best_match, knowledge_base)
            print(f'{knowledge_base["systemInfo"]["name_bot"]}: {answer}')
            if function != None and function != "None":
                await eval(function + f"({knowledge_base})")
             
        else:
            print(f'{knowledge_base["systemInfo"]["name_bot"]}: I don\'t know the answer. Can you teach me=?')
            new_answer: str = input('Type the answer or "skip" to skip: ')

            if new_answer.lower() != 'skip':
                knowledge_base["questions"].append({"question": user_input, "answer": new_answer, "function":"None"})
                save_knowledge_base('knowledge_base.json', knowledge_base)
                print(f'{knowledge_base["systemInfo"]["name_bot"]}: Thank you! I learned a new response!')





if __name__ == '__main__':
    asyncio.run(chat_bot())