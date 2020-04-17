/**
 * Programme to access load shedding information using a binary search tree (fixed)
 * @author Calvin Nyoni
 * @since 13 March 2019
 * @version 2.0 revised from original to fix bugs/issues
 */

import java.io.File;
import java.util.Iterator;
import java.util.Scanner;
import java.io.FileNotFoundException;

public class LSBSTApp {

    /**
     * Function to obtain all load shedding data, and input it into a binary search tree in the form of loadShedding objects
     * @return data a binary search consisting of loadShedding objects
     * @see BinarySearchTree
     * @see loadShedding
     *@throws FileNotFoundException returns FileNotFoundException if data set not found
     */
    public static BinarySearchTree<loadShedding> getData() throws FileNotFoundException {

        BinarySearchTree<loadShedding> data = new BinarySearchTree<loadShedding>(); //create empty binary search tree

        File file = new File("C:/Users/calvin.nyoni/Desktop/Assignment_2/src/Load_Shedding_All_Areas_Schedule_and_Map.clean.final.txt");

        Scanner scanner = new Scanner(file);

        while (scanner.hasNextLine()) {

            String currentLine = scanner.nextLine();
            String[] partsOfLine = currentLine.split(" ", 2); //Split obtained line from into 2 useful parts

            String searchID = partsOfLine[0];

            partsOfLine[1] = partsOfLine[1].strip();
            String[] areasAffected = partsOfLine[1].split(",");

            data.add(new loadShedding(searchID, areasAffected));
        }

        scanner.close();

        return data;
    }

     /**
     * Function to print out all loadshedding data from the binary search tree
     * Note order of loadShedding objects is according to the iterator (which is in the correct order)
     *@throws FileNotFoundException returns FileNotFoundException if data set not found
     */
     public static void printAllAreas() throws FileNotFoundException {

         BinarySearchTree<loadShedding> data = getData();

         Iterator<loadShedding> iterate = data.iterator();

         while (iterate.hasNext()) {
             System.out.println(iterate.next().toString());
         }
     }
     
     /**
      * Function to obtain load shedding details for a corresponding search query prints "Area not found"
      *Prints corresponding search if found, otherwise
      *@param stage in which search query occurs
      *@param day on which search query occurs
      *@param startTime at which search query occurs
      *@param test for testing search 
      *@throws FileNotFoundException returns FileNotFoundException if data set not found
      */
     public static void printAreas(String stage, String day, String startTime, boolean test)
             throws FileNotFoundException {

         //Trace statement for testing purposes
         if (test == true) {
             System.out.println("Input supplied: " + stage + " " + " " + day + " " + startTime);
         }

         //Format args into string for search
         String searchID = stage + "_" + day + "_" + startTime;

         BinarySearchTree<loadShedding> data = getData();

         loadShedding searchItem = new loadShedding(searchID, new String[0]);

         loadShedding result = data.get(searchItem);

         if (result == null) {
             System.out.println("Areas not found");
         } else {
             System.out.println(result.toString());
         }
     }
     
     /**
      * Execute loadShedding Binary Search Tree Application
      *Enter no args to see all load shedding details
      *Enter 3 args for search in 'stage' 'date' 'starting time' formart
      *Enter 4 args for testing
      *Invalid number arguments are caught
      *@throws FileNotFoundException returns FileNotFoundException if data set not found
      */
     public static void main(String[] args) throws FileNotFoundException {

        
        if (args.length == 0) {
           printAllAreas();
        }
        
	    else if (args.length > 0 && args.length < 3) {
           System.out.println("Invalid arguments");
        }	

        else if (args.length == 3) {
            printAreas(args[0], args[1], args[2], false);
        }
        
        else if (args.length == 4) {
            printAreas(args[0], args[1], args[2], true);
        }

	    else {
	        System.out.println("Invalid arguments");
        }
    }
}