package ArrayList;

import java.util.ArrayList;

public class ChangeItems {
    public static void main(String[] args) {
        ArrayList<String> Students = new ArrayList<String>();  // Create Array List
        Students.add("Himanshu"); // Adding items
        Students.add("Ujjwal");
        Students.add("Alok");
        Students.add("Abhishek");
        Students.set(0,"Arjun");   // Changing the item using set key.........
        Students.set(1,"Praveen");
        Students.set(2,"Rohit");

//        Students.remove(1);    // For removing the items..........

//        Students.clear();    //  Output  --      Empty Array.........





        System.out.println(Students.size());
    }

}
