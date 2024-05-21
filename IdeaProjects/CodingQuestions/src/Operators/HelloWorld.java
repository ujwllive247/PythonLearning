package Operators;

import java.util.Scanner;

public class HelloWorld {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter you string ");
        String word = scanner.next();
        for (int i = 0; i < 5; i++) {

            if (i==2){
                continue;
            }
            System.out.println(word);

        }

    }


}
