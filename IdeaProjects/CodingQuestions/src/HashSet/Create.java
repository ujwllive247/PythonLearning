package HashSet;

import java.util.HashSet;

public class Create {
    public static void main(String[] args) {
        HashSet<String> animal = new HashSet<String>();
         animal.add("Tiger");
        animal.add("Tiger");
        animal.add("Lion");
        animal.add("Giraffe");
        System.out.println(animal);  // In HashSet , it only print unique value....
        System.out.println(animal.contains("Lion"));
        System.out.println(animal.size());  // Size of the hashSet contains only unique value..


    }
}
