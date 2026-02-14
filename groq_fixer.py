import os,requests
API="https://api.groq.com/openai/v1/chat/completions"
MODEL="llama3-70b-8192"
KEY=os.getenv("GROQ_API_KEY")

def patch(code,errors):
    prompt=f"Return unified diff only. Fix minimal.\nErrors:\n{errors}\nCode:\n{code}"
    r=requests.post(API,headers={"Authorization":f"Bearer {KEY}"},json={
        "model":MODEL,"temperature":0,
        "messages":[{"role":"user","content":prompt}]
    })
    return r.json()["choices"][0]["message"]["content"]