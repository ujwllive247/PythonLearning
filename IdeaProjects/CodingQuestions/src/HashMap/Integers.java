package HashMap;

import java.util.HashMap;

public class Integers {
    public static void main(String[] args) {
        HashMap<String , Integer> People = new HashMap<String , Integer>();
        People.put("John", 32);
        People.put("Abrahim", 35);
        People.put("Akshay", 37);
        People.put("Alok", 38);

        for (String i : People.keySet()){
            System.out.println(" Name :" + i + "  " + "Age  : "  + People.get(i));
        }
//        System.out.println(People);

    }
}
