package LinkList;

import java.util.LinkedList;

public class Main {
    public static void main(String[] args) {
        LinkedList<String> cars = new LinkedList<String>();
        cars.add("Volvo");
        cars.add("BMW");
        cars.add("Ford");

        // Use addFirst() to add the item to the beginning
        cars.addFirst("Mazda");  // Adding the value
        cars.addLast("Punch");

        System.out.println(cars);

//        System.out.println(cars.getLast());
    }
}
