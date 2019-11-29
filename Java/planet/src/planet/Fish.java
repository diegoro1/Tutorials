package planet;

public class Fish extends Animal {

	public Fish(String specie, int age, char gender) {
		super(specie, age, gender);
	}

	public void swim()
	{
		System.out.println("Swimming...");
	}

	@Override
	public void move() {
		// TODO Auto-generated method stub
		
	}
}
