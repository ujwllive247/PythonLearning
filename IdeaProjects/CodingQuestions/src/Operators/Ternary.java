package Operators;

public class Ternary {
    public static void main(String[] args) {
//        int time = 20;
//        if (time < 18) {
//            System.out.println("Good day.");
//        } else {
//            System.out.println("Good evening.");
//        }

        // Instead of this, We can write .......
        int time = 20;
        String result = (time < 15) ? "Good Day " : "Good Evening";
        System.out.println(result);
    }
}
