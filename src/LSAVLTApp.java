/**
 * Programme to access load shedding information using a binary search tree (fixed)
 * @author Calvin Nyoni
 * @since 14 March 2019
 * @version 1.0
 */

import java.io.File;
import java.util.Iterator;
import java.util.Scanner;
import java.io.FileNotFoundException;

public class LSAVLTApp {
    public static AVLTree<loadShedding> getData() throws FileNotFoundException {

        AVLTree<loadShedding> data = new AVLTree<loadShedding>(); //create empty binary search tree

        File file = new File("C:/Users/calvin.nyoni/Desktop/Assignment_2/src/n4");

        Scanner scanner = new Scanner(file);

        while (scanner.hasNextLine()) {

            String currentLine = scanner.nextLine();
            String[] partsOfLine = currentLine.split(" ", 2); //Split obtained line from into 2 useful parts

            String searchID = partsOfLine[0];

            partsOfLine[1] = partsOfLine[1].strip();
            String[] areasAffected = partsOfLine[1].split(",");

            data.insert(new loadShedding(searchID, areasAffected));
        }

        scanner.close();

        data.getLargest().getElement().clearCount();

        return data;
    }

    public static void printAllAreas() throws FileNotFoundException {

        AVLTree<loadShedding> data = getData();
        
        data.inOrder();
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

        //Format args into string for search
        String searchID = stage + "_" + day + "_" + startTime;

        AVLTree<loadShedding> data = getData();

        loadShedding searchItem = new loadShedding(searchID, new String[0]);

        //Trace statement for testing purposes
        if (test == true) {
            //System.out.println("Input supplied: " + stage + " " + " " + day + " " + startTime);
            System.out.println(data.get(searchItem).getElement().getCount());
        }
        else {
            if (data.get(searchItem) != null) {
                System.out.println(data.get(searchItem).getElement().toString());
            } else {
                System.out.println("Areas not found");
            }
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