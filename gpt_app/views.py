from django.shortcuts import render
import os
# Create your views here.
from django.shortcuts import render
import openai
openai.api_key = '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'
#os.environ.get('API_KEYS')
# Create your views here.

def index(request):
    arr=[]
    if request.method == 'POST':
        if request.POST.get('search') != '':
          input = request.POST.get('search')
          def generate_response(prompt):
            response = openai.Completion.create(
                #name = 'SolBot',
                engine="text-davinci-002",
                prompt=prompt,
                max_tokens=2048,
                n=1,
                stop=None,
                temperature=0.5
            )
            return response.choices[0].text
          
        user_input = input

        prompt = f"User: {user_input} Bot: "
        bot_response = generate_response(prompt)


       
        arr.append(bot_response)
        print("User: " + input)
        print("GPT: " + bot_response)
        context ={
            'results': arr,
            'question': input
        }
    if len(arr)>0:
        return render(request,'index.html',context)
    else:
       return render(request,'index.html')
