package HashSet;

import java.util.HashSet;

public class Loops {
    public static void main(String[] args) {
        HashSet<String> animal = new HashSet<String>();
        animal.add("Tiger");
        animal.add("Tiger");
        animal.add("Lion");
        animal.add("Giraffe");

        for (String i : animal){
            System.out.println(i);
        }

    }

}
