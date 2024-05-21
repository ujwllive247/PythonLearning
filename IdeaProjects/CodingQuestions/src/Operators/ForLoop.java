package Operators;

import java.util.Scanner;

public class ForLoop {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter the number");
        int num = scanner.nextInt();

        for ( num = num; num < 10; num++) {
            System.out.println(num);

        }
    }
}
