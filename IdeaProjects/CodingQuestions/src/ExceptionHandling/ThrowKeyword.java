package ExceptionHandling;

public class ThrowKeyword {
    static void checkAge (int age){
        if (age >18){
            System.out.println("Access granted..You are able to cast the vote");
        }else {
//            System.out.println("Access denied...You are not eligible now");
            throw new ArithmeticException("Access denied...You are not eligible now");
        }

    }

    public static void main(String[] args) {
        checkAge(18);
    }
}
