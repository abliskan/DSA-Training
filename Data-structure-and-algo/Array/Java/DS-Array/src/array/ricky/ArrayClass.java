package array.ricky;

public class ArrayClass {
    public int id;
    public String name;

    // Constructor
    public ArrayClass(int id, String name) {
        this.id = id;
        this.name = name;
    }

    // Used to display the student data
    public void display() {
        System.out.println("- Student id is: " + id + "\n" + "- Student name is: " + name);
        System.out.println();
    }
}
