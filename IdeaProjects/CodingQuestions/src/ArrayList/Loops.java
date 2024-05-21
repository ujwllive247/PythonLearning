package ArrayList;

import java.util.ArrayList;

public class Loops {
    public static void main(String[] args) {

        ArrayList<String> BankName = new ArrayList<String>();
        BankName.add("State Bank");
        BankName.add("ICIC");
        BankName.add("HDFC");
        for (int i = 0; i < BankName.size(); i++) {
            System.out.println(BankName.get(i));

            // Using for loop, we can print the array in list..

        }
    }
}
