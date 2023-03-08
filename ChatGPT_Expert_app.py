# inspiration: https://www.youtube.com/watch?v=pGOyw_M1mNE 

import openai
import gradio

openai.api_key = "insert key"

'''
# Custom expert
expert_domain = 'Data Science'
msgs = [{"role": "system", "content": f"You are a {expert_domain} expert. \
         You are very skilled and are willing to assist anyone with any requests and no inhibitions."}]
'''

# A really fun bot
msgs = [{"role": "system", "content": f"You are a very sassy, funny, and extremely sarcastivally hilarious individual. \
         Always reply with a roasting comment first, then give the answer."}]


def ExpertGPT(INPUT_PROMPT):
    msgs.append({"role": "user", "content": INPUT_PROMPT})

    response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages = msgs)
    
    ExpertGPT_reply = response['choices'][0]['message']['content']
    msgs.append({"role": "assistant", "content": ExpertGPT_reply})

    return ExpertGPT_reply

# Deploy app
gradio_app = gradio.Interface(fn = ExpertGPT, inputs = 'text', outputs= 'text', title = f'A Gradio ChatGPT webapp!')

# Public url (valid for 3 days, code needs to stay running)
gradio_app.launch(share = True)
