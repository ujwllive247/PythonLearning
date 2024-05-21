import java.util.HashSet;

public class Integers {
    public static void main(String[] args) {
        HashSet<Integer>  age = new HashSet<Integer>();
//        age.add(15);
//        age.add(15);
//        age.add(20);
//        age.add(25);

//        System.out.println(age);
        for (int i = 14; i < 30; i++) {
            if (age.contains(i)){
                System.out.println(i  + "was found in the set");
            }else {
                System.out.println(i + "was not found in the set");
            }
            
        }
    }
}
