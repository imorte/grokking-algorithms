import java.util.LinkedList;

public class SelectionSort {
    public static void main(String... args) {
        LinkedList<Integer> data = new LinkedList<>();
        data.add(9); data.add(8);
        data.add(7); data.add(6);
        data.add(5); data.add(4);
        data.add(3); data.add(2);
        data.add(1);

        System.out.println(selectionSort(data));
    }

    private static LinkedList<Integer> selectionSort(LinkedList<Integer> data) {
        LinkedList<Integer> sortedData = new LinkedList<>();

        while(data.size() > 0) {
            int lowestIndex = 0;
            int lowestElement = data.get(lowestIndex);

            for(Integer i : data) {
                if(i < lowestElement) {
                    lowestElement = i;
                    lowestIndex = data.indexOf(lowestElement);
                }
            }

            sortedData.add(lowestElement);
            data.remove(lowestIndex);
        }

        return sortedData;
    }
}