package ArrayList;

import java.util.ArrayList;

public class AccessItems {
    public static void main(String[] args) {
        ArrayList<String> Students = new ArrayList<String>();  // Create Array List
        Students.add("Himanshu"); // Adding items
        Students.add("Ujjwal");
        Students.add("Alok");
        Students.add("Abhishek");
        Students.set(2,"JaiPrakash");

        System.out.println(Students.get(2));   // Fetching the value Array item by index number.
    }
}
