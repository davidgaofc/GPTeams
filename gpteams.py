from openai import OpenAI
import math
import os
import re
import sys

client = OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    api_key="",
)

class gpteam():
    def __init__(self, number_of_workers, work_dir, question_file):
        self.worker_count = number_of_workers
        self.worker_dir= work_dir
        self.question_file = question_file

    def master_answer(self, prompt):
        pretext = "Take the following solutions to a function, and combine them into one function, taking the best parts of each. You may ignore solutions if they are incorrect."
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": pretext + "\n\n" + prompt}
            ]
        )
        print("master answered")
        return completion.choices[0].message.content
        # return "master answer\n" + prompt

    def worker_answer(self, prompt):
        pretext = "Complete the function marked with TODO in the following code. Be sure to capture your solution in a code block (```python ... ```)"
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": pretext + "\n\n" + prompt}
            ]
        )
        print("worker answered")
        return completion.choices[0].message.content
        # prompt = "here is my solution"
        # return "formatting junk" + "\n```python\n"+ prompt + "\n```\n" + "formatting junk"

    def parse_file(self, file):
        with open(file, "r") as f:
            prompt = f.read()
        sections = prompt.split("\n\n")
        splitable = []
        primary = []
        for i in sections:
            if("import" in i):
                pass
            elif("TODO" in i):
                primary.append(i+"\n\n")
            else:
                splitable.append(i+"\n\n")

        return primary, splitable

    def designate_work(self, worker_id):
        task, splitable = self.parse_file(self.question_file)

        total_length = len(splitable)
        base_segment_length = total_length // self.worker_count


        overlap = max(1, min(math.ceil(base_segment_length / 2), total_length // (2 * self.worker_count)))

        start = worker_id * base_segment_length - (overlap if worker_id > 0 else 0)
        end = start + base_segment_length + (overlap if worker_id < self.worker_count - 1 else 0)

        if worker_id == self.worker_count - 1:
            end = total_length

        start = max(start, 0)
        end = min(end, total_length)

        worker_context = splitable[start:end]
        worker_context.append(task[0])

        return " ".join(worker_context)

    def split_work(self):
        for i in range(self.worker_count):
            worker_prompt = self.designate_work(i)

            temp = self.worker_answer(worker_prompt)

            with open(f"{self.worker_dir}/worker{i}.py", "w") as f:
                f.write(temp)


    def clean_worker_output(self):
        final = []
        for file in os.listdir(self.worker_dir):
            with open(f"{self.worker_dir}/{file}", "r") as f:
                response = f.read()
                code_pattern = r"`(.*?)`"
                matches = re.findall(code_pattern, response, re.DOTALL)
                python_code = matches[1].strip() if matches else None
                if(python_code):
                    cleaned = python_code.replace("python", "")
                    final.append(cleaned)
        return final

    def merge_workers(self):
        my_results = self.clean_worker_output()
        candidates = "\n\n\n".join(my_results)
        with open(f"{self.worker_dir}/master.py", "w") as f:
            f.write(self.master_answer(candidates))

    question_file = "questions/question_test.py"
    worker_dir = "output/question1"
    worker_count = 0