package array.ricky;

import java.util.*;

public class Main {
    public static void main(String[] args) {
        /*
        // System.out.println("Hello world!");

        // Array - Declaring object
        ArrayClass[] arr;
        // Allocating memory for 2 objects of type student
        arr = new ArrayClass[2];
        // Initializing the first element of the array
        arr[0] = new ArrayClass(1701289270, "Nanda"); // Direct into constructor in ArrayClass
        arr[1] = new ArrayClass(1701289219, "Nindi");
        // Displaying the student data
        System.out.println("Student data in student arr 0: ");
        arr[0].display();

        System.out.println("Student data in student arr 1: ");
        arr[1].display();

        // Array - Append
        int i;

        String arr1[] = {"apple", "banana", "cherry"};

        // Get user input with help if Java Scanner
        System.out.print("Enter a string: ");
        Scanner sc = new Scanner(System.in); // System.in is a standard input stream
        String str = sc.nextLine(); // nextLine = advances this scanner past the current line.

        String arrNew[] = new String[arr1.length + 1];
        for(i = 0; i < arr1.length; i++) {
            arrNew[i] = arr1[i];
        }
        arrNew[i] = str;

        //print new array
        for(String s: arrNew) {
            System.out.println(s);
        }

        // Array - Insertion
        int dumpInt1, dumpInt2, pos;

        Scanner s = new Scanner(System.in);
        System.out.print("Enter no. of elements you want in array:");
        dumpInt1 = s.nextInt(); // .nextInt = 	it is used to scan the next token of the input as an integer
        int a[] = new int[dumpInt1+1];

        // Get user input to intialize array default value
        System.out.println("Enter all the elements:");
        for(int i = 0; i < dumpInt1; i++) {
            a[i] = s.nextInt();
        }

        // Get user input to set position for new value
        System.out.print("Enter the position where you want to insert element:");
        pos = s.nextInt();

        // Get user input for new value
        System.out.print("Enter the element you want to insert:");
        dumpInt2 = s.nextInt();
        for(int i = (dumpInt1-1); i >= (pos-1); i--) {
            a[i+1] = a[i];
        }
        a[pos-1] = dumpInt2;

        // Final output display array
        System.out.print("After inserting:");
        for(int i = 0; i < dumpInt1; i++) {
            System.out.print(a[i]+",");
        }
        System.out.print(a[dumpInt1]);
        */
        // Array - Pop

        // Array - Remove
        int[] arr = {3,1,6,5,2,8,4};
        int[] newArr = null;
        int elementToBeDeleted = 5;

        System.out.println("Original Array is: "+Arrays.toString(arr));

        for (int i = 0; i < arr.length-1; i++) {
            if(arr[i] == elementToBeDeleted){
                newArr = new int[arr.length - 1];
                for(int index = 0; index < i; index++){
                    newArr[index] = arr[index];
                }
                for(int j = i; j < arr.length - 1; j++){
                    newArr[j] = arr[j+1];
                }
                break;
            }
        }
        System.out.println("New Array after deleting element = "+elementToBeDeleted+" and shifting: "+ Arrays.toString(newArr));
    }
}