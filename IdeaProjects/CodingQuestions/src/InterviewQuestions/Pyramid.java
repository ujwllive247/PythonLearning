package InterviewQuestions;

import java.util.Scanner;

public class Pyramid {
    public static void main(String[] args) {
//        int rows = 25; // Number of rows in the pyramid

        Scanner scanner = new Scanner(System.in);
        System.out.println("Print the number");
        int num = scanner.nextInt();


        for (int i = 1; i <= num; i++) {
            // Print spaces before the stars
            for (int j = 1; j <= num - i; j++) {
                System.out.print(" ");
            }

            // Print stars
            for (int k = 1; k <= 2 * i - 1; k++) {
                System.out.print("*");
            }

            // Move to the next line
            System.out.println();

        }
}}
