package InterviewQuestions;

import java.util.Scanner;

public class AddToNumbers {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter your first number");
        int number1 = scanner.nextInt();
        System.out.println("Enter Second number");
        int number2 = scanner.nextInt();

        int sum = number1+number2;
        System.out.println("The sum of these numbers are " +sum);
    }
}
