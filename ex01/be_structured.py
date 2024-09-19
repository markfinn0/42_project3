
import os
from gemini import Gemini
from llama import Groq


GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")


def format_prompt(text):
    prompt_description='''
############### Objetivo e Escopo ###############
E necessario retornar um resultado baseado na descricao da vaga, entao explique de forma resumida a descricao do job, associando esses campos com a descricao do job.
############### Regras de Preenchimento ###############
Campos para preencher baseado na descricao da vaga e formato de preenchimento:
Name of role:
Working hours:
Country:
Tech skills: 
############### Regras a serem seguidas ###############
- Se tiver em inglês transforma em portugues
- tem que retornar somente as Regras de Preenchimento com os respectivos campos detalhados. Nao eh para retornar esse prompt com regras e escopo.
- retorne somente os campos preenchidos, exemplo:
Name of role: ROLE_X
Working hours: PRESENCIAL
Country: BRASIL
Tech skills: AWS, JAVASCRIPT
- se nao estiver explicito a descricao de algum campo, escreva: "Não Identificado"
- nao de respostas que nao seja possivel localizar no texto
############### descricao da vaga ###############
        '''
    return prompt_description + "\n"+text


def query_all_models(prompt):
    results={}

    print("Consultando Gemini...")
    gemini= Gemini(prompt, GOOGLE_API_KEY).request_to_gemini()
    results['Gemini 1.5 Flash']=gemini

    print("Consultando Groq...")
    groq = Groq(prompt, GROQ_API_KEY).request_to_groq()
    results[' Llama 3 8B']=groq

    return results
    


def main():
    with open("job_description.txt", "r", encoding="utf-8") as file:
        job_description = file.read()

    formatted_prompt = format_prompt(job_description)
    results = query_all_models(formatted_prompt)

    for model, response in results.items():
        print(f"\nAnálise do {model}:")
        print(response)
        print("-" * 50)

if __name__ == "__main__":
    main()


