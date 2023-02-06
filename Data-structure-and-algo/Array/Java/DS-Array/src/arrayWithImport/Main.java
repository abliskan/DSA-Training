package arrayWithImport;

import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        // System.out.println("Hello world!");
        // Get the Array
        int intArr[] = { 10, 20, 15, 22, 35 };

        // To print the elements in one line
        System.out.println("Integer Array: " + Arrays.toString(intArr));
        System.out.println("\nNew Arrays by copyOf:\n");
        // used Arrays.copyOf() method from java.util.Arrays
        System.out.println("Integer Array: " + Arrays.toString(Arrays.copyOf(intArr, 10)));
    }
}