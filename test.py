import base64
import os

import openai
from dotenv import load_dotenv

# 如果存在环境变量的文件，则加载配置到环境变量
if os.path.exists(".env"):
    load_dotenv(".env")

openai.api_key = os.getenv("OPENAI_API_KEY")

openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Completion.create(
  model="ada:ft-personal-2023-02-16-09-23-59",
  prompt="Company: Reliable accountants Ltd\nProduct: Personal Tax help\nAd:Best advice in town!\nSupported:",
  temperature=0.5,
  max_tokens=1,
  top_p=1.0,
  frequency_penalty=0.5,
  presence_penalty=0.0
)

# response = openai.Completion.create(
#   model="text-davinci-003",
#   prompt="You: What have you been up to?\nFriend: Watching old movies.\nYou: Did you watch anything interesting?\nFriend:",
#   temperature=0.5,
#   max_tokens=60,
#   top_p=1.0,
#   frequency_penalty=0.5,
#   presence_penalty=0.0
#   # stop=["You:"]
# )

# response = openai.Completion.create(
#   model="code-davinci-002",
#   prompt="### Postgres SQL tables, with their properties:\n#\n# Employee(id, name, department_id)\n# Department(id, name, address)\n# Salary_Payments(id, employee_id, amount, date)\n#\n### A query to list the names of the departments which employed more than 10 employees in the last 3 months\nSELECT",
#   temperature=0,
#   max_tokens=150,
#   top_p=1.0,
#   frequency_penalty=0.0,
#   presence_penalty=0.0
# )
print(response.choices[0].text)

# if __name__ == '__main__':
#     print('start')
#     response = openai.Completion.create(
#         model='ada',
#         prompt='Company: Reliable accountants Ltd\nProduct: Personal Tax help\nAd:Best advice in town!\nSupported:',
#         max_tokens=1)
#     str = response.choices[0].text
#     print(str)

