package planet;

public class Human {
	String name;
	int age;
	int heightInInches;
	String eyeColor;
	
	public Human()
	{
		
	}
	
	public void speak()
	{
		System.out.println("My name is " + name);
		System.out.println("My height is " + heightInInches + " in inches.");
		System.out.println("I am " + age + " years old");
		System.out.println("My eye color is " + eyeColor);
	}
	
	public void eat()
	{
		System.out.println("eating...");
	}
	
	public void walk()
	{
		System.out.println("walking...");
	}
	
	public void work()
	{
		System.out.println("working..");
	}
}
