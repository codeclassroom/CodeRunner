import static java.lang.Math.pow;

// program to print a given pattern

class Main {
	public static void main (String[] args) {
		int p;
		for (int i = 1; i <= 10; i++) {
			p = (int) (pow (i, 2));
			System.out.print (p + " ");
			if (i == 4 || i == 7 || i == 9) System.out.println ();
		}
	}
}