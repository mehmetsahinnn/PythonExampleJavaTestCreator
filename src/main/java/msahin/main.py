import API_KEY
from function_file import *

openai.api_key = API_KEY.API_KEY


def main():
    input_filename = 'example_code'
    output_filename = 'test_output'

    unit_tests = read_from_file(input_filename)
    method_code = generate_method_from_tests(unit_tests, language="Java")

    class_code = f"""import org.springframework.http.HttpStatus;
    import org.springframework.http.ResponseEntity;

    public class Calculator {{
        private CustomerService customerService = new CustomerService();

        {method_code}
    }}
    """

    compile_returncode, compile_stdout, compile_stderr = compile_java_files()
    if compile_returncode != 0:
        print(f"Compilation failed:\n{compile_stderr}")
        return

    test_result, failures = run_java_tests()
    print(test_result)
    if failures:
        for failure in failures:
            print(failure)

    write_to_file(output_filename, class_code)
    print(f"Generated method written to {output_filename}:\n{method_code}")



if __name__ == "__main__":
    main()