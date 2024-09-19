from gemini import Gemini
from dotenv import load_dotenv
import os
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

def create_prompt(role,task,topic,specific_question):
    prompt_description=f'''
<role>
{role}
</role>
<task>
{task}
</task>
<topic>
{topic}
</topic>
<specific_question>
{specific_question}
</specific_question>
        '''
    return prompt_description 

    
    

if __name__=="__main__":

    role = "especialista em filosofia e história da ciência"
    task = "explicar o pensamento de Descartes e sua influência para iniciantes em filosofia"
    topic = "René Descartes e o Método Cartesiano"
    specific_question = "Quem foi René Descartes e qual é o significado da frase 'Penso, logo existo'?"

    prompt = create_prompt(role, task, topic, specific_question)
    response= Gemini(prompt, GOOGLE_API_KEY).send_to_gemini()
    print("\nResposta do Gemini 1.5 Flash:")
    print(response)