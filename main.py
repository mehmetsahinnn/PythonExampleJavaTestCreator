import API_KEY
from function_file import *

openai.api_key = API_KEY.API_KEY


def main():
    input_filename = 'example_code'
    output_filename = 'Code.java'

    unit_tests = read_from_file(input_filename)
    method_code = generate_method_from_tests(unit_tests, language="Java")

    # Add necessary imports and mock definitions
    class_code = f"""
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;

class Customer {{
    private String email;
    private String password;

    // Getters and Setters
    public String getEmail() {{
        return email;
    }}

    public void setEmail(String email) {{
        this.email = email;
    }}

    public String getPassword() {{
        return password;
    }}

    public void setPassword(String password) {{
        this.password = password;
    }}
}}

class CustomerService {{
    public Customer findByEmail(String email) {{
        // Mock implementation
        return new Customer();
    }}
}}

public class Calculator {{
    private CustomerService customerService = new CustomerService();

    {method_code}
}}
"""
    write_to_file(output_filename, class_code)
    print(f"Generated method written to {output_filename}:\n{method_code}")

    # Compile Java files
    compile_returncode, compile_stdout, compile_stderr = compile_java_files()
    if compile_returncode != 0:
        print(f"Compilation failed:\n{compile_stderr}")
        return

    # Run tests
    test_returncode, test_stdout, test_stderr = run_tests()
    if test_returncode != 0:
        print(f"Tests failed:\n{test_stderr}")
    else:
        print(f"Tests passed:\n{test_stdout}")


if __name__ == "__main__":
    main()