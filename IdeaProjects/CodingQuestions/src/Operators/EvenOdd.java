package Operators;

import java.util.Scanner;

public class EvenOdd {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter the number, I can tell you the even/odd");
        int num = scanner.nextInt();
//        int x = 7;
        if (num%2 == 0){
            System.out.println("This is even");
        }
        else{
            System.out.println("This is Odd");
        }
    }



}
