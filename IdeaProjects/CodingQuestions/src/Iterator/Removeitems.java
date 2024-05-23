package Iterator;

import java.util.ArrayList;
import java.util.Iterator;

public class Removeitems {
    public static void main(String[] args) {
        ArrayList<Integer> numbers = new ArrayList<Integer>();
        numbers.add(12);
        numbers.add(8);
        numbers.add(2);
        numbers.add(23);
        Iterator<Integer> it = numbers.iterator();
        while(it.hasNext()) {
            Integer i = it.next();
            if(i < 10) {
                it.remove(); // Removing the number which is less than 10/ We can also use less than..
            }
        }
        System.out.println(numbers);
    }
    }
