package planet;

public class Chicken extends bird{

	public Chicken(String specie, int age, char gender) {
		super(specie, age, gender);
	}
	
	public void fly()
	{
		System.out.println("Not able to fly...");
	}
	

}
