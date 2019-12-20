import java.util.Scanner;
class Loan extends Exception {
String name;
double salary;
void getInfo () {
Scanner input = new Scanner (System.in);
name = input.nextLine ();
salary = input.nextDouble ();
}
void checkEligibility () throws Loan {
if (salary < 70000) throw new Loan ();
else System.out.println (name + " is eligible for loan!");
}
public String toString () {
return "Not eligible for loan!";
}
}
class Main {
public static void main(String[] args) {
Loan person = new Loan ();
person.getInfo ();
try {
person.checkEligibility ();
}
catch (Loan l) {
System.out.println (l);
}
}
}