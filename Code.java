
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;

class Customer {
    private String email;
    private String password;

    // Getters and Setters
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
}

class CustomerService {
    public Customer findByEmail(String email) {
        // Mock implementation
        return new Customer();
    }
}

public class Calculator {
    private CustomerService customerService = new CustomerService();

    
public class Calculator {
    
    public ResponseEntity<?> login(Customer customer) {
        if (customer.getEmail().equals("test@example.com") && customer.getPassword().equals("password")) {
            return ResponseEntity.ok("Login successful");
        } else {
            return ResponseEntity.status(HttpStatus.UNAUTHORIZED).body("Invalid credentials");
        }
    }
}

}
