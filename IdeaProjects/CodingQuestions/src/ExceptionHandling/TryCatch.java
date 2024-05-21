package ExceptionHandling;

public class TryCatch {
    public static void main(String[] args) {
        try {
            int [] num = {20,25,30,40};
            System.out.println(num[10]);  // 10 not exits in the array that's why it throw predifined exception.
        }catch (Exception e){
            System.out.println("Something went Wrong");
        }finally {
            System.out.println("Try Catch is finished");
        }
    }
}
