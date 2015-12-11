package com.ssutherlanddee.day4;

import java.io.UnsupportedEncodingException;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public class Advent4 {

	public static void main(String[] args) throws UnsupportedEncodingException, NoSuchAlgorithmException {
		String puzzleInput = "bgvyzdsv";
		int i = 0;
		
		while(!hasFiveZeroes(puzzleInput)) {
			puzzleInput = "bgvyzdsv" + Integer.toString(i);
			i++;
		}
		
		byte[] textToDigest =puzzleInput.getBytes("8859_1");
		byte[] digest = MD5(textToDigest);
		
		// dump out the hash
		for(byte b: digest){
			System.out.printf("%02X", b & 0xff);
		}
		System.out.println("\n" + (i -1));
		
	}
	
	public static byte[] MD5(byte[] textToDigest) throws NoSuchAlgorithmException, UnsupportedEncodingException {
		
		MessageDigest md = MessageDigest.getInstance("MD5");
		md.update(textToDigest);
		byte[] digest = md.digest();
		System.out.println(digest);
		return digest;
	}
	
	public static Boolean hasFiveZeroes(String text) throws UnsupportedEncodingException, NoSuchAlgorithmException {
		byte[] textToDigest = text.getBytes("8859_1");
		byte[] digest = MD5(textToDigest);
		
		if(((digest[0] & 0xff) == 0) && ((digest[1] & 0xff) == 0) && ((digest[2] & 0xff) == 0)){
			return true;
		}
		
		return false;
	}
}
