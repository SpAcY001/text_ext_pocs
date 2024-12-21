import requests

API_URL = "https://api-inference.huggingface.co/models/jinhybr/OCR-Donut-CORD"
# API_TOKEN="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"
headers = {"Authorization": "Bearer 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"}

def query(filename):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.post(API_URL, headers=headers, data=data)
    return response.json()

output = query("c:\\Users\\SESA737860\\Downloads\\receipt-template-vector-22560714.jpg")
print(output)
with open('write_json.txt', 'w', encoding = "utf-8") as outfile:
    # for line in text:
    outfile.write(str(output))
    outfile.close()