package com.ssutherlanddee.day3;

public class House {
	
	public int x;
	public int y;
	
	public House(int x, int y) {
		this.x = x;
		this.y = y;
	}
	
    @Override
    public boolean equals(Object object)
    {
        boolean sameSame = false;

        if (object != null && object instanceof House)
        {
            sameSame = this.x == ((House) object).x && this.y == ((House) object).y;
        }

        return sameSame;
    }
}
