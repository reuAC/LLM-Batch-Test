# LLM-Batch-Test
[ [中文](https://github.com/reuAC/LLM-Batch-Test/blob/reuAC/README_EN.md) | English | [日本語](https://github.com/reuAC/LLM-Batch-Test/blob/reuAC/README_JP.md) ]

* runer.py  : Run the large model once.
* runer2.py : Run the large model once and obtain feedback from the model.
* runer3.py : Continuously run the large model in a loop, allowing for ongoing conversation, and receive feedback from the model.
* web.py    : Create a web page to enable continuous conversation with the large model, modify the System Prompt in real-time, and receive feedback from the model.
* make.py   : Should be run with parameters, such as `python make.py -qdir=question_folder -output=output_filename.csv -n=number_of_times_to_ask_each_question &`.It will go through all .txt files in the question folder, treating each line as a question and passing it to the model.The model will answer each question n times, and the results will be aggregated into a spreadsheet for output.