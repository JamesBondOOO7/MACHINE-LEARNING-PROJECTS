    /* package codechef; // don't place package name! */

    import java.util.*;
    import java.lang.*;
    import java.io.*;

    /* Name of the class has to be "Main" only if the class is public. */
    public class Main
    {
        public static void main (String[] args) throws java.lang.Exception
        {
                Scanner sc = new Scanner(System.in);
                int t = sc.nextInt();
                for(int q = 0 ; q<t ; q++)
                {
                        int n = sc.nextInt();
                        PriorityQueue<Integer> heap = new PriorityQueue<>(Collections.reverseOrder());
                        for(int i = 0 ; i<n ; i++)
                        {
                                int p = sc.nextInt();
                                heap.add(p);
                        }
                        long ans = 0;
                        int i = 0;
                        while(heap.size() != 0)
                        {
                               int rv = heap.poll();
                               if( rv > i)
                               {
                                       rv = rv - i;
                               }
                               else
                               {
                                       rv = 0;
                               }
                               ans += rv;
                               i++;
                        }
                        ans = ans % (1000000007);
                        System.out.println(ans);
                }
    }
    }
