package Operators;

public class LogicOperator {
    public static void main(String[] args) {
        int x = 5;
        int y = 3;

        // And Operator ____Both condition should be true
        System.out.println(x > y && y <x);

        // OR Operator ______ either of the one condition should be true.....
        System.out.println(x > y  || y > x);

        // NOT Equal To.........
        System.out.println(!(x > y && y <x));
    }
}
