from flask import Flask, request, render_template, jsonify
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

app = Flask(__name__)

device = "cuda"
model = AutoModelForCausalLM.from_pretrained(
    "Qwen2-7B-Instruct",
    torch_dtype="auto",
    device_map="auto"
)
tokenizer = AutoTokenizer.from_pretrained("Qwen2-7B-Instruct")

messages = [
    {"role": "system", "content": "You are a helpful assistant."}
]

def get_response(user_input):
    messages.append({"role": "user", "content": user_input})
    
    text = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True
    )
    
    model_inputs = tokenizer([text], return_tensors="pt").to(device)
    
    generated_ids = model.generate(
        model_inputs.input_ids,
        max_new_tokens=512
    )
    
    generated_ids = [
        output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
    ]
    response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
    
    messages.append({"role": "assistant", "content": response})
    
    return response

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    if user_input:
        response = get_response(user_input)
        return jsonify({"response": response})
    return jsonify({"response": "No input received"})

@app.route('/reset', methods=['POST'])
def reset():
    global messages
    messages = [{"role": "system", "content": "You are a helpful assistant."}]
    return jsonify({"response": "Chat reset successfully."})

@app.route('/set_system_prompt', methods=['POST'])
def set_system_prompt():
    global messages
    system_prompt = request.json.get('system_prompt')
    if system_prompt:
        messages = [{"role": "system", "content": system_prompt}]
        return jsonify({"response": f"System prompt set to: {system_prompt}"})
    return jsonify({"response": "No system prompt provided."})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

