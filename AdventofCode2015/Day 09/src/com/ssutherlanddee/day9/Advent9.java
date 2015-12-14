package com.ssutherlanddee.day9;

import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class Advent9 {
	
    	static ArrayList<City> cities = new ArrayList<City>();
    	static Map<String,Integer> routes = new HashMap<String,Integer>();

	    public static void main(String[] args) throws IOException{
	        Scanner scan = new Scanner(new File("src/com/ssutherlanddee/day9/input.txt"));
	        
	        // Create the cities.
	        while(scan.hasNext()) {
	            String[] lineSplit = scan.nextLine().split(" ");
	            City c = getCity(lineSplit[0]);
	            c.addDist(getCity(lineSplit[2]),Integer.parseInt(lineSplit[4]));
	        }
	        
	        scan.close();

	        // Find valid routes for all starting cities.
	        for(City c : cities) {
	            getRoutes(c,new ArrayList<String>(),0);
	        }
	        
	        
	        Integer[] ar = routes.values().toArray(new Integer[0]);
	        Arrays.sort(ar);
	        System.out.println("Part 1: " + ar[0] + " Part 2: " + ar[ar.length-1]); 
	    }
	    
	    public static City getCity(String s) {
	        for(City c : cities)
	        	// If the city exists, return it.
	            if(c.name.equals(s)) {
	                return c;
	            }
	        
	        // else, create the new city and return it.
	        City city = new City(s);
	        cities.add(city);
	        return city;
	    }

	    public static void getRoutes(City city, ArrayList<String> list, int length) {
	        list.add(city.name);
	        
	        for(City c : city.dist.keySet()) {
	            if(!list.contains(c.name)) {
	            	// If the city hasn't been visited then visit it.
	                getRoutes(c, new ArrayList<String>(list), length + city.dist.get(c));
	            } else if(list.size() == cities.size()) {
	            	// If all cities have been visited then add it as a valid route.
	                routes.put(Arrays.toString(list.toArray()), length);
	            }
	        }
	    }
}
