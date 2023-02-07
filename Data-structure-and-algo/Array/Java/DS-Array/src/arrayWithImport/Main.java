package arrayWithImport;

import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static String[] insertX(int n, String arr[], String x, int pos) {
        int i;
        // create a new array of size n+1
        String newarr[] = new String[n + 1];

        // insert the elements from
        // the old array into the new array
        // insert all elements till pos
        // then insert x at pos
        // then insert rest of the elements
        for (i = 0; i < n + 1; i++) {
            if (i < pos - 1)
                newarr[i] = arr[i];
            else if (i == pos - 1)
                newarr[i] = x;
            else
                newarr[i] = arr[i - 1];
        }
        return newarr;
    }

    public static void main(String[] args) {
        /*
        // System.out.println("Hello world!");
        // Get the Array
        int intArr[] = { 10, 20, 15, 22, 35 };

        // To print the elements in one line
        System.out.println("Integer Array: " + Arrays.toString(intArr));
        System.out.println("\nNew Arrays by copyOf:\n");
        // used Arrays.copyOf() method from java.util.Arrays
        System.out.println("Integer Array: " + Arrays.toString(Arrays.copyOf(intArr, 10)));

        // Array - Append
        int txt1;
        String newTxt;

        // Get user input to intialize array size
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter no. of elements you want in array:");
        txt1 = sc.nextInt();
        String arr[] = new String[txt1+1];

        // Get user input to intialize array default value
        for (int i=0; i < txt1+1; i++) {
            arr[i] = sc.nextLine();
        }

        // Copy previous array to new array + 1 index
        String arrNew[] = Arrays.copyOf(arr, arr.length+1);

        // Get user input to insert new value
        Scanner sc1 = new Scanner(System.in);
        System.out.print("Enter new value:");
        newTxt = sc1.next();
        arrNew[arr.length] = newTxt;

        // Display inside array
        System.out.print("After inserting:");
        for(int i = 0; i < arrNew.length; i++) {
            System.out.print(arrNew[i]+",");
        }
        System.out.print(arrNew[txt1+1]);
        */
        // Array - Insertion
        int dumpInt, pos;
        String dumpTxt;

        Scanner s = new Scanner(System.in);
        System.out.print("Enter no. of elements you want in array:");
        dumpInt = s.nextInt(); // .nextInt = 	it is used to scan the next token of the input as an integer
        String a[] = new String[dumpInt+1];

        // Get user input to intialize array default value
        System.out.println("Enter all the elements:");
        for(int i = 0; i < dumpInt+1; i++) {
            a[i] = s.nextLine();
        }

        // Get user input to set position for new value
        System.out.print("Enter the position where you want to insert element:");
        pos = s.nextInt();

        // Get user input for new value
        System.out.print("Enter the element you want to insert:");
        dumpTxt = s.next();

        a = insertX(dumpInt, a, dumpTxt, pos);

        // Display inside array
        System.out.print("After inserting:");
        for(int i = 0; i < a.length; i++) {
            System.out.print(a[i]+",");
        }
        System.out.print(a[dumpInt+1]);
    }
}