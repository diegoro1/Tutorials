package planet;

public class bird extends Animal {
	
	public bird(String specie, int age, char gender)
	{
		super(specie, age, gender);
	}
	
	public void fly()
	{
		System.out.println("Flying...");
	}

	@Override
	public void move() {
		// TODO Auto-generated method stub
		
	}
}
