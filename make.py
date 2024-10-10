import os
import csv
import argparse
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

parser = argparse.ArgumentParser(description="Generate responses to questions using a language model")
parser.add_argument('-qdir', '--questions_dir', type=str, required=True, help="Directory containing the question files")
parser.add_argument('-output', '--output_csv', type=str, required=True, help="Output CSV file")
parser.add_argument('-n', '--n_responses', type=int, required=True, help="Number of responses to generate per question")
args = parser.parse_args()

device = "cuda" if torch.cuda.is_available() else "cpu"
model = AutoModelForCausalLM.from_pretrained(
    "Qwen2-7B-Instruct",
    torch_dtype="auto",
    device_map="auto"
)
tokenizer = AutoTokenizer.from_pretrained("Qwen2-7B-Instruct")

def generate_response(prompt, n=1, max_new_tokens=512):
    messages = [
        {"role": "system", "content": "【重要】你是ABC医院的智能医生。【重要】你只需要简单解答用户所说的症状，并给出应该前往的医院科室。"},
        {"role": "user", "content": prompt}
    ]
    text = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True
    )
    model_inputs = tokenizer([text], return_tensors="pt").to(device)
    responses = []
    for _ in range(n):
        generated_ids = model.generate(
            model_inputs.input_ids,
            max_new_tokens=max_new_tokens
        )
        generated_ids = [
            output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
        ]
        response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
        responses.append(response)
    return responses

questions_dir = args.questions_dir
output_csv = args.output_csv
n_responses = args.n_responses

question_files = [f for f in os.listdir(questions_dir) if f.endswith('.txt')]

with open(output_csv, mode='w', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)
    header = ["Question"] + [f"Response{i+1}" for i in range(n_responses)]
    csv_writer.writerow(header)

    for question_file in question_files:
        question_file_path = os.path.join(questions_dir, question_file)
        with open(question_file_path, 'r', encoding='utf-8') as file:
            questions = file.readlines()
        
        for question in questions:
            question = question.strip()
            if question:
                responses = generate_response(question, n=n_responses)
                csv_writer.writerow([question] + responses)

print(f"Responses have been written to {output_csv}")

