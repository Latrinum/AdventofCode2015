package com.ssutherlanddee.day9;

import java.util.HashMap;
import java.util.Map;

class City {
    String name;
    Map<City,Integer> dist = new HashMap<City,Integer>();

    City(String n) {
        name = n;
    }
    public void addDist(City c,int d) {
        dist.put(c,d);
        c.dist.put(this,d);
    }
}