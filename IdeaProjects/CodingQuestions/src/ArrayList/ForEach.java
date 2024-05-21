package ArrayList;

import java.util.ArrayList;

public class ForEach {
    public static void main(String[] args) {
        ArrayList<String> BankName = new ArrayList<String>();
        BankName.add("State Bank");
        BankName.add("ICIC");
        BankName.add("HDFC");
        for (String i : BankName){
            System.out.println(i);       // We print the Array in list using for each loop..
        }
    }
}
