package Operators;

public class WhileContinue {
    public static void main(String[] args) {
        int i = 0;
        while(i < 20){
            System.out.println(i);
            i++;
            if(i==12){
                continue;
            }
            System.out.println(i);
            i++;

        }
    }
}
