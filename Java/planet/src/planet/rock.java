package planet;

public class rock {
	int age;
	String type;
	
	public rock(int age, String type)
	{
		this.age = age;
		this.type = type;
	}
	
	public void action()
	{
		System.out.println("Rocks don't do anyting :/");
	}
}
