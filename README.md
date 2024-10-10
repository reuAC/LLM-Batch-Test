# LLM-Batch-Test
[ 中文 | [English](https://github.com/reuAC/LLM-Batch-Test/blob/re_uAC/README_EN.md) | [日本語](https://github.com/reuAC/LLM-Batch-Test/blob/re_uAC/README_JP.md) ]

* runer.py  : 运行一次大模型。
* runer2.py : 运行一次大模型，并获取大模型的反馈。
* runer3.py : 循环运行大模型，可以进行连续对话，并获取大模型的反馈。
* web.py    : 创建一个web页面，可以与大模型进行连续对话、实时修改System Prompt，并获取大模型的反馈。
* make.py   : 运行时应带有参数，如`python make.py -qdir=问题存放文件夹 -output=输出的文件名.csv -n=每个问题问几次 &`它会遍历问题存放文件夹中所有以.txt结尾的文件，并将每行视为一个问题，输入给大模型。大模型会回答n次问题，最终将结果汇总到表格并输出。