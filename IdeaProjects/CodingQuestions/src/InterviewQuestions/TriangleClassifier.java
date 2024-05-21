package InterviewQuestions;

public class TriangleClassifier {
    public static void main(String[] args) {
        int a = 5;
        int b = 4;
        int c = 4;
        if(a==b && b==c && c==a){
            System.out.println("This is Equilateral Traingle");}
        else if (a==b || a ==c || b==c) {
            System.out.println("This is Isoselus Traingle");

        }
        else {
            System.out.println("Scalen Traingle");


    }
    }
}
