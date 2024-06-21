import os
import openai

openai.api_key = os.getenv("API_KEY")


def generate_test_code(example_file_code, language="Java"):
    prompt = f"Write the corresponding unit test code in {language} for the following {language} function:\n\n{example_file_code}\n\nTest code:"

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # gpt-4o
        messages=[
            {"role": "system", "content": "You are a Java Programming Language Master"
                                          "that writes unit tests for all cases with 100 years of experience."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=300,
        temperature=0.1
    )

    test_code = response.choices[0].message['content'].strip()
    return test_code


def read_file(filename):
    with open(filename, 'r') as file:
        content = file.read()
    return content


def write_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)
