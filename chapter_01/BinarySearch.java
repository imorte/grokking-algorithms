public class BinarySearch {
    public static void main(String... args) {
        int[] array = {1, 6, 8, 20, 53, 65, 77, 87, 95};

        System.out.println(search(array, 65));
    }

    private static int search(int[] array, int item) {
        int low = 0;
        int high = array.length;

        while(low <= high) {
            int mid = (low + high) / 2;
            int guess = array[mid];
            
            if(guess == item) {
                return mid;
            };
            if(guess > item) {
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }

        return item;
    }
}