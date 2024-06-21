import function_file

input_filename = 'example_code'
output_filename = 'test_output'

example_file_code = function_file.read_file(input_filename)
test_code = function_file.generate_test_code(example_file_code, language="Java")
function_file.write_file(output_filename, test_code)
print(f"Test code written to {output_filename}:\n{test_code}")


