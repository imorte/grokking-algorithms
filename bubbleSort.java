import java.util.Arrays;

public class Main {
    public static void main(String... args) {
        int[] data = {
                9, 2, 4, 1, 6
        };

        System.out.println(Arrays.toString(bubbleSort(data)));
    }

    private static int[] bubbleSort(int[] data) {
        for(int i = 0; i < data.length - 1; i++) {
            for(int j = 0; j < (data.length - 1) - i; j++) {
                if(data[j] > data[j + 1]) {
                    int v = data[j];
                    data[j] = data[j + 1];
                    data[j + 1] = v;
                }
            }
        }

        return data;
    }
}