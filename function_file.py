import openai


def generate_method_from_tests(unit_tests, language="Java"):
    prompt = f"Write the corresponding {language} method that satisfies the following unit tests:\n\n{unit_tests}\n\nMethod:"

    response = openai.ChatCompletion.create(
        model="gpt-4o",  # gpt-4o
        messages=[
            {"role": "system", "content": "You are a helpful assistant that writes up to multiple methods to satisfy unit tests. But, please complete all methods write the possible greatest code"},
            {"role": "user", "content": prompt}
        ],
        max_tokens=1000,  # Adjust the length based on your need
        temperature=0.5
    )

    method_code = response.choices[0].message['content'].strip()
    method_code = method_code.replace('```', '')
    method_code = method_code.replace('java', '')
    method_code = method_code.replace('public class Calculator {', '')

    method_code = method_code.rstrip()
    if method_code.endswith('}'):
        method_code = method_code[:-1].rstrip()

    return method_code


def read_from_file(filename):
    with open(filename, 'r') as file:
        content = file.read()
    return content


def write_to_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)

