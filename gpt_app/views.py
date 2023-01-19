from django.shortcuts import render
import os
# Create your views here.
from django.shortcuts import render
import openai
openai.api_key = "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"
# Create your views here.
def index(request):
    arr=[]
    if request.method == 'POST':
        if request.POST.get('search') != '':
          name = request.POST.get('search')
          def generate_response(prompt):
            response = openai.Completion.create(
                engine="text-davinci-002",
                prompt=prompt,
                max_tokens=2048,
                n=1,
                stop=None,
                temperature=0.5
            )
            return response.choices[0].text
          
        user_input = name

        prompt = f"User: {user_input} Bot: "
        bot_response = generate_response(prompt)


       
        arr.append(bot_response)
        print("GPT: " + bot_response)
        context ={
            'results': arr,
            'question': name,
        }
    if len(arr)>0:
        return render(request,'index.html',context)
    else:
       return render(request,'index.html')