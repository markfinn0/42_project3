import requests

class Gemini:
    def __init__(self, prompt: str, api_key: str) -> None:
        self.prompt = prompt
        self.api_key = api_key

    def treatment_request(self, response: requests.Response) -> str:
        text = "No text found"
        try:
            data = response.json()
            if 'candidates' in data and len(data['candidates']) > 0:
                text = data['candidates'][0]['content']['parts'][0]['text']
        except ValueError:
            print("Erro ao processar a resposta JSON.")
        return text

    def request_to_gemini(self) -> str:
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={self.api_key}"
        payload = {
            "contents": [{
                "parts": [{"text": self.prompt}]
            }]
        }
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.post(url, headers=headers, json=payload)
        
        return self.treatment_request(response)

