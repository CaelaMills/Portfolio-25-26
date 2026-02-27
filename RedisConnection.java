package org.example;

import redis.clients.jedis.Jedis;

import java.util.Date;

/**
 * This class provides methods for storing, retrieving, updating, and deleting customer data in Redis.
 * It utilizes the hset method for setting hash field values and the hget method for retrieving hash field values.
 * The del method is used to delete the customer data.
 */
public class RedisConnection {

    /**
     * Main method demonstrating CRUD operations on customer data in Redis.
     *
     * @param args Command-line arguments (not used in this program).
     */
    public static void main(String[] args) {
        Jedis jedis = new Jedis("localhost", 6379); // Connect to Redis server

        // Store customer data in Redis
        Customer customer = new Customer("ccm5669@psu.edu", "Nike", "Caela Mills", new Date(), 85.0, "Footlocker");
        String customerKey = "customer:" + customer.getCustomerEmail();
        storeCustomerData(jedis, customerKey, customer);

        // Retrieve and print customer data from Redis
        retrieveAndPrintCustomerData(jedis, customerKey);

        // Update customer data in Redis
        updateCustomerData(jedis, customerKey, "seller", "DSW"); // Because instead of getting shoes from Footlocker, you could get them from DSW

        // Retrieve and print updated customer data from Redis
        retrieveAndPrintCustomerData(jedis, customerKey);

        // Delete customer data from Redis
        deleteCustomerData(jedis, customerKey);

        jedis.close();
    }

    /**
     * Stores customer data in Redis using the hset method.
     *
     * @param jedis       Jedis instance for Redis connection.
     * @param customerKey Key to uniquely identify the customer in Redis.
     * @param customer    Customer object containing data to be stored.
     */
    private static void storeCustomerData(Jedis jedis, String customerKey, Customer customer) {
        jedis.hset(customerKey, "email", customer.getCustomerEmail());
        jedis.hset(customerKey, "productBrought", customer.getProductBrought());
        jedis.hset(customerKey, "customerName", customer.getCustomerName());
        jedis.hset(customerKey, "transactionDate", String.valueOf(customer.getTransactionDate().getTime()));
        jedis.hset(customerKey, "amount", String.valueOf(customer.getAmount()));
        jedis.hset(customerKey, "seller", customer.getSeller());

        System.out.println("Stored Customer Data in Redis: " + customerKey);
    }

    /**
     * Retrieves and prints customer data from Redis using the hget method.
     *
     * @param jedis       Jedis instance for Redis connection.
     * @param customerKey Key to uniquely identify the customer in Redis.
     */
    private static void retrieveAndPrintCustomerData(Jedis jedis, String customerKey) {
        String retrievedEmail = jedis.hget(customerKey, "email");
        String retrievedProduct = jedis.hget(customerKey, "productBrought");
        String retrievedName = jedis.hget(customerKey, "customerName");
        String retrievedTransactionDate = jedis.hget(customerKey, "transactionDate");
        String retrievedAmount = jedis.hget(customerKey, "amount");
        String retrievedSeller = jedis.hget(customerKey, "seller");

        System.out.println("Retrieved Customer Data from Redis:");
        System.out.println("Email: " + retrievedEmail);
        System.out.println("Product Brought: " + retrievedProduct);
        System.out.println("Customer Name: " + retrievedName);
        System.out.println("Transaction Date: " + new Date(Long.parseLong(retrievedTransactionDate)));
        System.out.println("Amount: " + Double.parseDouble(retrievedAmount));
        System.out.println("Seller: " + retrievedSeller);
        System.out.println();
    }

    /**
     * Updates customer data in Redis using the hset method.
     *
     * @param jedis       Jedis instance for Redis connection.
     * @param customerKey Key to uniquely identify the customer in Redis.
     * @param field       Field to be updated (e.g., "seller").
     * @param updatedValue Updated value for the specified field.
     */
    private static void updateCustomerData(Jedis jedis, String customerKey, String field, String updatedValue) {
        jedis.hset(customerKey, field, updatedValue);
        System.out.println("Updated Customer Data in Redis:");
        System.out.println("Updated " + field + ": " + updatedValue);
    }

    /**
     * Deletes customer data from Redis using the del method.
     *
     * @param jedis       Jedis instance for Redis connection.
     * @param customerKey Key to uniquely identify the customer in Redis.
     */
    private static void deleteCustomerData(Jedis jedis, String customerKey) {
        jedis.del(customerKey);
        System.out.println("Deleted Customer Data from Redis: " + customerKey);
    }
}
