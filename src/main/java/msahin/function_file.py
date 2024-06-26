import glob
import subprocess

import jpype
import openai


def generate_method_from_tests(unit_tests, language="Java"):
    prompt = f"Write the corresponding {language} method that satisfies the following unit tests:\n\n{unit_tests}\n\nMethod:"

    response = openai.ChatCompletion.create(
        model="gpt-4o",  # gpt-4o
        messages=[
            {"role": "system", "content": "You are a helpful assistant that writes up to multiple methods to satisfy unit tests. But, please complete all methods write the possible greatest code"},
            {"role": "user", "content": prompt}
        ],
        max_tokens=500,  # Adjust the length based on your need
        temperature=0.2
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


def run_java_tests():
    jpype.startJVM(
        jpype.getDefaultJVMPath(),
        "-ea",
        f"-Djava.class.path=.:junit-4.13.2.jar:hamcrest-core-1.3.jar:spring-web-6.1.10.jar:spring-core-5.3.9.jar"
    )

    JUnitCore = jpype.JClass('org.junit.runner.JUnitCore')
    CalculatorTest = jpype.JClass('CalculatorTest')

    result = JUnitCore.runClasses(CalculatorTest)

    failures = []
    if result.wasSuccessful():
        test_result = "All tests passed!"
    else:
        for failure in result.getFailures():
            failures.append(failure.toString())
        test_result = f"Tests failed with {len(failures)} failures."

    jpype.shutdownJVM()

    return test_result, failures


def compile_java_files():
    process = subprocess.run([
        "java", "-cp", ".:junit-4.13.2.jar:hamcrest-core-1.3.jar:spring-web-6.1.10.jar:spring-core-5.3.9.jar",
        "CalculatorTest.java"
    ], capture_output=True, text=True)
    return process.returncode, process.stdout, process.stderr
