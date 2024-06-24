import subprocess

import openai


def generate_method_from_tests(unit_tests, language="Java"):
    prompt = f"Write the corresponding {language} method that satisfies the following unit tests:\n\n{unit_tests}\n\nMethod:"

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # gpt-4o
        messages=[
            {"role": "system", "content": "You are a helpful assistant that writes methods to satisfy unit tests."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=300,  # Adjust the length based on your need
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


def compile_java_files():
    process = subprocess.run([
        "javac", "-cp", ".:spring-web-6.1.10.jar:spring-core-5.3.9.jar", "*.java"
    ], capture_output=True, text=True)
    return process.returncode, process.stdout, process.stderr


def run_tests():
    process = subprocess.run([
        "java", "-cp", ".:junit-4.13.2.jar:hamcrest-core-1.3.jar:spring-web-6.1.10.jar:spring-core-5.3.9.jar",
        "org.junit.runner.JUnitCore", "CalculatorTest"
    ], capture_output=True, text=True)
    return process.returncode, process.stdout, process.stderr

