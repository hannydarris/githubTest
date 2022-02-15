import java.util.*;

public class findSubstringPermutation {
	public static void main(String argv[]) {
		Scanner input = new Scanner(System.in);
		System.out.println("Enter a substring:");
		String sub = input.nextLine();
		System.out.println("Enter the longer string:");
		String longer = input.nextLine();

		List<String> perms = new ArrayList<>();
		perms = permutate("", sub, perms);
		List<String> exists = new ArrayList<>();

		for(int j=0; j<longer.length()-sub.length(); j++) {
			String window = longer.substring(j, j+sub.length());
			if(perms.contains(window)) {
				exists.add(window);
			}
		}
		System.out.println("Possible permutations: ");
		System.out.println(perms);
		System.out.println("Contains: ");
		System.out.println(exists);
	}
	public static List<String> permutate(String prefix, String s, List<String> perms) {
		for(int i=0; i<s.length(); i++) {
			String perm = prefix + s.charAt(i) + s.substring(0,i) + s.substring(i+1, s.length());
			if(!perms.contains(perm)) {
				perms.add(perm);
			}
			permutate(prefix + s.charAt(i), s.substring(0,i) + s.substring(i+1, s.length()), perms);
		}
		return(perms);
	}
}