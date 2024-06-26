import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;

public class Calculator {
    private CustomerService customerService = new CustomerService();
    

        To satisfy the given unit tests, we need to implement the methods `filterOrderByDate` and `filterOrderByUser` in the `ElasticOrderService` class. We also need to assume the existence of an `OrderDocumentRepository` that provides methods to fetch orders based on date and username. Below is the implementation of these methods:


import .time.LocalDateTime;
import .util.*;
import .util.stream.Collectors;

public class ElasticOrderService {

    private final OrderDocumentRepository orderDocumentRepository;

    public ElasticOrderService(OrderDocumentRepository orderDocumentRepository) {
        this.orderDocumentRepository = orderDocumentRepository;
    }

    public Map<Long, List<OrderDocument>> filterOrderByDate(LocalDateTime startDate, LocalDateTime endDate) {
        List<OrderDocument> orders = orderDocumentRepository.findOrdersByDateBetween(startDate, endDate);

        return orders.stream()
                .collect(Collectors.groupingBy(OrderDocument::getUserId));
    }

    public Map<Long, List<OrderDocument>> filterOrderByUser(String username, LocalDateTime startDate, LocalDateTime endDate) {
        List<OrderDocument> orders = orderDocumentRepository.findUserByUsername(username);

        List<OrderDocument> filteredOrders = orders.stream()
                .filter(order -> !order.getOrderDate().isBefore(startDate) && !order.getOrderDate().isAfter(endDate))
                .collect(Collectors.toList());

        return filteredOrders.stream()
                .collect(Collectors.groupingBy(OrderDocument::getUserId));
    }
}


### Explanation:
1. **filterOrderByDate Method:**
   - This method takes a `startDate` and `endDate` and retrieves the orders from `orderDocumentRepository` that fall within these dates.
   - It then groups these orders by `userId` using Java Streams and `Collectors.groupingBy`.

2. **filterOrderByUser Method:**
   - This method takes a `username`, `startDate`, and `endDate`.
   - It retrieves all orders for the given `username` from `orderDocumentRepository`.
   - It filters these orders to include only those where the `orderDate` falls within the specified date range.
   - Finally, it groups the filtered orders by `userId` using Java Streams and `Collectors.groupingBy`.

### Assumptions:
- `OrderDocument` is a class with properties such as `id`, `username`, `userId`,
    }
    

}