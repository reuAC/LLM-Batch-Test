from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

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

print("Chat with the model. Type 'exit' to end the conversation.")
while True:
    user_input = input("User: ")
    if user_input.lower() == "exit":
        break
    response = get_response(user_input)
    print(f"Assistant: {response}")

