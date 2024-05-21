package HashMap;

import java.util.HashMap;

public class ForEach {
    public static void main(String[] args) {
        HashMap<String , String> City = new HashMap<String , String>();
        City.put("England" , "London");
        City.put("Berlin" , "Tokyo");
        City.put("LiverPool" , "Lansdown");
//        for (String i : City.keySet()){  // To print the key......
//            System.out.println(City);
        for (String i : City.values()){         // To print the value......
            System.out.println(i);
        }
    }
}
