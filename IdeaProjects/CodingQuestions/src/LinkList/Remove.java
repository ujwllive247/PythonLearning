package LinkList;

import java.util.LinkedList;

public class Remove {
    public static void main(String[] args) {
        LinkedList<String> cars = new LinkedList<String>();
        cars.add("Volvo");
        cars.add("BMW");
        cars.add("Ford");

        // Use addFirst() to add the item to the beginning
        cars.addFirst("Mazda");  // Adding the value
        cars.addLast("Punch");
        cars.removeLast();  // removeFirst is also present in this features.
        System.out.println(cars);

    }
}
