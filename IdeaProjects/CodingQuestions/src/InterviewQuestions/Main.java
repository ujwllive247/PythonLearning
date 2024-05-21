package InterviewQuestions;

import java.util.Scanner;

public class Main {

    public static void reverseWords(char[] sentence) {
        // Reverse entire sentence
        reverse(sentence, 0, sentence.length-1);

        int start = 0;
        for(int end=0; end<sentence.length; end++) {
            if(sentence[end] == ' ') {
                // Reverse current word
                reverse(sentence, start, end-1);
                start = end + 1;
            }
        }

        // Reverse last word
        reverse(sentence, start, sentence.length-1);
    }

    public static void reverse(char[] arr, int i, int j) {
        while(i < j) {
            char temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
            i++;
            j--;
        }
    }



    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a sentence: ");
        String input = scanner.nextLine();

        char[] sentence = input.toCharArray();
        reverseWords(sentence);

        System.out.println(new String(sentence));
    }
}

