import java.util.*;

class findMedianSortedArray {
	public static void main(String argv[]) throws Exception {
			Scanner scanner = new Scanner(System.in);
			boolean validArray = false;
			int arrcount = 0;
			int alistlen = 0;
			int blistlen = 0;
			List<List<String>> allnums = new ArrayList<>();

			do {
				try {
					if(arrcount == 0) {
						System.out.println("Enter a List of Numbers (separated by commas):");
						String[] nums1 = scanner.nextLine().split(",");
						List<String> alist = Arrays.asList(nums1);
						allnums.add(alist);
						alistlen += alist.size();
						arrcount++;
					}
					else if(arrcount == 1) {
						System.out.println("Enter a Second List of Numbers (separated by commas):");
						String[] nums2 = scanner.nextLine().split(",");
						List<String> blist = Arrays.asList(nums2);
						allnums.add(blist);
						blistlen += blist.size();
						arrcount++;
					}
					else {
						List<Integer> numlist = new ArrayList<>();

						for(List<String> subset : allnums) {
							for(String each : subset) {
								numlist.add(Integer.parseInt(each.trim()));
							}
						}
						List<Integer> sortedNums = mergeSort(numlist);

						int median = sortedNums.size()/2;

						String result = String.join(" | ", sortedNums.toString());
						System.out.println("Combined Sorted Lists:\n" + result + "\nMedian:\n" + sortedNums.get(median));

						validArray = true;
					}
				}
				catch(InputMismatchException e) {
					System.out.println("Error.");
				}
			}
			while(validArray == false);
	}
	
	public static List<Integer> mergeSort(List<Integer> nums) {
		List<Integer> sorted = new ArrayList<>();
		if(nums.size() > 1) {

			int mid = nums.size()/2;
			List<Integer> low = nums.subList(0, mid);
			List<Integer> high = nums.subList(mid, nums.size());

			List<Integer> sortedLow = mergeSort(low);
			List<Integer> sortedHigh = mergeSort(high);

			int x = 0;
			int y = 0;

			while(x<sortedLow.size() && y<sortedHigh.size()) {
				if(sortedLow.get(x) < sortedHigh.get(y)) {
					sorted.add(sortedLow.get(x));
					x++;
				}
				else {
					sorted.add(sortedHigh.get(y));
					y++;
				}
			}
			while(x<sortedLow.size()) {
				sorted.add(sortedLow.get(x));
				x++;
			}
			while(y<sortedHigh.size()) {
				sorted.add(sortedHigh.get(y));
				y++;
			}
			return sorted;
		}
		else {
			return nums;
		}
	}
}