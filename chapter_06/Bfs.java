import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;

public class Bfs {
    public static void main(String[] args) {
        HashMap<String, String[]> graph = new HashMap<>(10);

        graph.put("you", (new String[] {"alice", "bob", "claire"}));
        graph.put("bob", (new String[] {"anuj", "peggy"}));
        graph.put("alice", (new String[] {"peggy"}));
        graph.put("claire", (new String[] {"thom", "jonny"}));
        graph.put("anuj", (new String[] {}));
        graph.put("peggy", (new String[] {}));
        graph.put("thom", (new String[] {}));
        graph.put("jonny", (new String[] {}));

        search(graph);
    }

    private static void search(HashMap<String, String[]> graph) {
        ArrayDeque<String> deque = new ArrayDeque<>();
        ArrayList<String> searched = new ArrayList<>();
        deque.addAll(Arrays.asList(graph.get("you")));

        while(!deque.isEmpty()) {
            String current = deque.pollFirst();
            if(!searched.contains(current)) {
                if(isSeller(current)) {
                    System.out.println(current + " is seller!");
                    return;
                } else {
                    searched.add(current);
                    deque.addAll(Arrays.asList(graph.get(current)));
                }
            }
        }
    }

    private static boolean isSeller(String name) {
        return name.charAt(name.length() - 1) == 'm';
    }
}
