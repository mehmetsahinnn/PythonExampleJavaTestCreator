import API_KEY
from function_file import *

openai.api_key = API_KEY.API_KEY


def main():
    input_filename = 'example_code'
    output_filename = 'test_output'

    unit_tests = read_from_file(input_filename)
    method_code = generate_method_from_tests(unit_tests, language="Java")

    class_code = f"""
        {method_code}
    }}
    """
    write_to_file(output_filename, class_code)
    print(f"Generated method written to {output_filename}:\n{method_code}")



if __name__ == "__main__":
    main()
