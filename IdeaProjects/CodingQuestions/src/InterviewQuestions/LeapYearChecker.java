package InterviewQuestions;

public class LeapYearChecker {
    public static void main(String[] args) {
        int Year = 2024;

        boolean isLeapYear = false;
        int year = 2001;
        if ((year % 4 == 0 && year % 100 != 0) || (year % 400 == 0)) {
            isLeapYear = true;
        }

        if (isLeapYear) {
            System.out.println(year + " is a leap year.");
        } else {
            System.out.println(year + " is not a leap year.");
        }
    }
}





