package msahin;

import org.python.jline.internal.InputStreamReader;
import org.python.util.PythonInterpreter;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class Main {
    public static void main(String[] args) {
        try (PythonInterpreter pyInterp = new PythonInterpreter()) {
            pyInterp.execfile("C:\\Users\\LENOVO\\OneDrive\\Masaüstü\\JythonTest\\src\\main\\java\\msahin\\main.py");
        } catch (Exception e) {
            e.printStackTrace();
        }

        String methodCode = readMethodFromFile();

        if (methodCode != null) {
            String javaClassContent = generateJavaClassWithMethod(methodCode);
            writeToFile("GeneratedMethod.java", javaClassContent);
            compileAndRunTests();
        }
    }

    private static String readMethodFromFile() {
        StringBuilder content = new StringBuilder();
        try (BufferedReader br = new BufferedReader(new FileReader("C:\\Users\\LENOVO\\OneDrive\\Masaüstü\\JythonTest\\src\\main\\java\\msahin\\test_output"))) {
            String line;
            while ((line = br.readLine()) != null) {
                content.append(line).append("\n");
            }
        } catch (IOException e) {
            e.printStackTrace();
            return null;
        }
        return content.toString();
    }

    private static String generateJavaClassWithMethod(String methodCode) {
        return "import org.springframework.http.HttpStatus;\n" +
                "import org.springframework.http.ResponseEntity;\n\n" +
                "public class GeneratedMethod {\n" +
                "    private CustomerService customerService = new CustomerService();\n" +
                "    \n" +
                methodCode + "\n" +
                "}";
    }

    private static void writeToFile(String filePath, String content) {
        try (java.io.FileWriter writer = new java.io.FileWriter(filePath)) {
            writer.write(content);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private static void compileAndRunTests() {
        try {
            Process compileProcess = Runtime.getRuntime().exec("javac -cp .;junit-4.13.2.jar;spring-web-6.1.10.jar;spring-core-5.3.9.jar GeneratedCalculator.java CalculatorTest.java");
            compileProcess.waitFor();

            Process runTestsProcess = Runtime.getRuntime().exec("java -cp .;junit-4.13.2.jar;hamcrest-core-1.3.jar;spring-web-6.1.10.jar;spring-core-5.3.9.jar org.junit.runner.JUnitCore CalculatorTest");
            BufferedReader reader = new BufferedReader(new InputStreamReader(runTestsProcess.getInputStream()));
            String line;
            while ((line = reader.readLine()) != null) {
                System.out.println(line);
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
