package LinkList;

import java.util.LinkedList;

public class GetItems {
    public static void main(String[] args) {
        LinkedList<String> cars = new LinkedList<String>();
        cars.add("Volvo");
        cars.add("BMW");
        cars.add("Ford");

        // Use addFirst() to add the item to the beginning
        cars.addFirst("Mazda");  // Adding the value
        cars.addLast("Punch");
//        cars.getFirst();
        System.out.println(cars.getFirst());

    }
}
