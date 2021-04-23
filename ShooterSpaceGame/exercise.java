import java.util.Scanner;

public class exercise{
    public static void main(String[] args) {
        Scanner input = new Scanner( System.in );
        int numSelect = 0;
        while( !(numSelect>=2 && numSelect<=9) ) { System.out.println("Digite un número entre 2 y 9:"); numSelect = input.nextInt(); }
        for ( int i = 0; i <= 10; i++ ) { System.out.println(numSelect+" x "+i+" = "+multiply(numSelect,i)); }
    }
    public static int multiply(int num,int multiplyNum){ return num*multiplyNum; }
}