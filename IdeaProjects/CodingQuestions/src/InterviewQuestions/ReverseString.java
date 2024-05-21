package InterviewQuestions;

public class ReverseString {
    public static void main(String[] args) {
        String name = "Ujjwal";
        String reverseName = "";

        for (int i = 0; i <name.length() ; i++) {
            reverseName = name.charAt(i) + reverseName;

        }

        System.out.println("The reverse of this string is "+ reverseName);
    }
}
