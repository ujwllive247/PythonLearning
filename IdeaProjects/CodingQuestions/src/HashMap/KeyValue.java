package HashMap;

import java.util.HashMap;

public class KeyValue {
    public static void main(String[] args) {
        HashMap<String , String> City = new HashMap<String , String>();
        City.put("England" , "London");
        City.put("Berlin" , "Tokyo");
        City.put("LiverPool" , "Lansdown");
        for (String i : City.keySet()){
            System.out.println("Key :" + i + " -----"+ "Value : " + City.get(i));
        }
    }
}
