package ExceptionHandling;

public class OutOfBound {
    public static void main(String[] args) {
        int [] num = {20,25,30,40};
        System.out.println(num[8]);

        // This programme throw error   "ArrayIndexOutOfBoundsException"
        // Because, index number 10 not present in this array.....
    }
}
