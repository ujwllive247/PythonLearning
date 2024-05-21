package Threading;

public class RunThread {
    public static void main(String[] args) {
        Fruits thread = new Fruits();
        thread.start();
        System.out.println("This code is outside of the thread");
    }
    public void run() {
        System.out.println("This code is running in a thread");
    }
}
