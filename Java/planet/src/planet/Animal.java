package planet;

public abstract class Animal {
		
	String specie;
	int age;
	char gender;
		
	public Animal(String specie, int age, char gender)
	{
		this.age = age;
		this.specie = specie;
		this.gender = gender;
	}

	public void eating()
	{
		System.out.println("eating...");
	}
	
	public void sleeping()
	{
		System.out.println("sleeping..");
	}
	
	public void gimp()
	{
		System.out.println("eeeeeIIieiie mooooo");
		System.out.println("im "+ age);
		System.out.println("moooo im a" + specie);
		System.out.println("meeeehhh im " + gender);
	}
	
	public abstract void move();
	
}
