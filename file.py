from requests import post
from json import dumps,loads


response = post(
    url="http://localhost:11434/api/generate",
    data=dumps(
        dict(
            model="llama3.2",
            prompt="hi stupid boring ollama",
            stream=False
        )
    )
)
if response.ok:
    payload=loads(response.text)
    print(payload['response'])
print("done")
