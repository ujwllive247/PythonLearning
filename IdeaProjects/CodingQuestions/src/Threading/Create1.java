package Threading;


//Another way to create a thread is to implement the Runnable interface:

public class Create1 implements Runnable{

    public void run(){
        System.out.println("This thread is running");
    }
}
