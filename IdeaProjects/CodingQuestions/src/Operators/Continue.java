package Operators;

public class Continue {
    public static void main(String[] args) {
        for (int i = 0; i < 10; i++) {
            if (i == 4) {
                continue;  // Skip the value of i at the continue point

            }
            System.out.println(i);

        }
    }
}
