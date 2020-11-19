import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Random;

public class Main {

    public static void reduceTo(ArrayList<Integer> lst, int last) {
        for (int i = lst.size() -1; i > last; --i) {
            lst.remove(i);
        }
    }

    // Supprime élément d'une liste à l'index pos
    public static void supAtPos(ArrayList<Integer> lst, int pos) {
        if (pos < 0 || pos >= lst.size()) {
            throw new RuntimeException("pos: " + pos + " pas dans la liste");
        }

        while (pos < lst.size() - 1 ) {
            lst.set(pos, lst.get(pos + 1));
            ++pos;
        }
        reduceTo(lst, lst.size() - 2);
    }

    // Supprime toutes les valeurs val de la liste et retourne une liste rétrécie
    // complexité O(n) ? (dépend de manière linéaire du nombre d'éléments dans la liste)
    public static void supAllVal(ArrayList<Integer> lst, int val) {
        int insertPos = 0;
        int lectPos = 0;

        while (lectPos < lst.size()) {
            int currVal = lst.get(lectPos);

            if (currVal != val) {
                lst.set(insertPos, currVal);
                ++insertPos;
            }
            ++lectPos;
        }
        reduceTo(lst, insertPos - 1);
    }

    // crée une liste de taille `size` comprenant environ p% de valeurs `val`
    public static ArrayList<Integer> randList(int size, int p, int val) {
        ArrayList<Integer> result = new ArrayList<>();
        Random rand = new Random();

        for (int i = 0; i < size; ++i) {
            int proba = rand.nextInt(100);

            if (proba < p) {
                result.add(val);
            } else {
                result.add(rand.nextInt(10));
            }
        }
        return result;
    }

    //effectue `nbrRuns` de 'supAllVal' sur liste de taille `lstSize` et retourne le temps total en milisecondes
    public static double timeSupAllVal(int lstSize, int nbrRuns) {
        long totTime = 0;

        var lst = randList(lstSize, 50, 0);

        for (int i = 0; i < nbrRuns; ++i) {
            var tstLst = new ArrayList<>(lst);

            var t0 = System.nanoTime();
            supAllVal(tstLst, 0);
            var elapsed = System.nanoTime() - t0;

            totTime += elapsed;
        }
        return totTime/1000000.0;
    }

    public static void timeSupAllValAllSizes() {
        timeSupAllValAllSizes(null, 0);
    }

    // effectue nbr_runs de `timeSupAllVal`
    public static void timeSupAllValAllSizes(int[] sizes, int nbr_runs) {
        if (sizes == null) {
            sizes = new int[] {10000,20000,40000,80000};
        }

        if (nbr_runs == 0) {
            nbr_runs = 4;
        }

        for (int n = 1; n <= nbr_runs; ++n) {
            System.out.println("--- run " + n + " ---" );
            for (int size : sizes) {
                var time_ms = timeSupAllVal(size, 100);
                System.out.printf("%d: %.2f millisecondes\n", size, time_ms);
            }
            System.out.println("");
        }
    }

    public static void main(String[] args) {

        //exercice 4
        int[] sizes = new int[] {1000000, 2000000, 4000000, 8000000};
        timeSupAllValAllSizes(sizes, 4);
    }
}
