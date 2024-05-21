package ArrayList.OtherTypes;

import java.util.ArrayList;
import java.util.Collection;
import java.util.Collections;

public class IntegerArray {
    public static void main(String[] args) {

        ArrayList<Integer> Numbers = new ArrayList<Integer>();
        Numbers.add(50);
        Numbers.add(30);
        Numbers.add(20);

        Numbers.add(40);

        Collections.sort(Numbers);    // Always print increasing order in integer Array
//        System.out.println(Numbers); // In String case, it prints alphabetically.....
        for (Integer i : Numbers){
            System.out.println(i);       // Print in the list
        }
    }
}
