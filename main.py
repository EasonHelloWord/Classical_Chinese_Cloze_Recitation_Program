# 定义输入文本
input_text = open("input_text.txt", "r",encoding="utf-8").read()

import re

# 正则表达式匹配括号中的内容
pattern = r'(\w+)(\（(.*?)\）)'

lift_index_list = list(re.finditer(pattern, input_text))
task = list(input_text[:])

for lift_index in lift_index_list:# 输出题目
    # print(task[lift_index.span(3)[0]:lift_index.span(3)[1]])
    task[lift_index.span(3)[0]:lift_index.span(3)[1]] = ["_"]*(lift_index.span(3)[1]-lift_index.span(3)[0])
task = "".join(task)
open("task.txt","w",encoding="utf-8").write(task)

print()
answer = ""
for lift_index in lift_index_list: # 输出答案
    answer += f"{lift_index.group(0)}{"\n"}"
open("answer.txt", "w", encoding="utf-8").write(answer)