package HashMap;

import java.util.HashMap;

public class GetItems {
    public static void main(String[] args) {
        HashMap<String , String> City = new HashMap<String , String>();
        City.put("England" , "London");
        City.put("Berlin" , "Tokyo");
        City.put("LiverPool" , "Lansdown");
        System.out.println(City.get("Berlin"));
        System.out.println(City.size());

    }
}
