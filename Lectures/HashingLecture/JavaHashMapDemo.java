import java.util.HashMap;

public class JavaHashMapDemo {
    public static void main(String[] args) {
        String s = args[0];
        int hash = 0;
        for (int i = 0; i < s.length(); i++) {
            hash = s.charAt(i) + 31*hash;
        }
        System.out.println(hash);
        System.out.println(s.hashCode());
    }
}





