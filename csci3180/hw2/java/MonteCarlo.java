/**
 * CSCI1530 Computer Principals and Java Programming
 * Assignment 4 Monte Carlo Simulator
 * Aims: 1. Implementing a practical simulator using Monte Carlo method.
 *       2. Practising object-oriented programming.
 *       3. Generating random numbers.
 *       4. Creating and using simple GUI components.
 *
 * Declaration:
 * I declare that the assignment here submitted is original
 * except for source material explicitly acknowledged,
 * and that the same or closely related material has not been
 * previously submitted for another course.
 * I also acknowledge that I am aware of University policy and
 * regulations on honesty in academic work, and of the disciplinary
 * guidelines and procedures applicable to breaches of such
 * policy and regulations, as contained in the website.
 * 
 * University Guideline on Academic Honesty:
 *   http://www.cuhk.edu.hk/policy/academichonesty/
 * 
 * Student Name : Kwok Kan Hang
 * Student ID   : 1155094268
 * Date: 13th March 2018
 * 
 */


import java.awt.Color;
import java.awt.Graphics;
import java.awt.image.BufferedImage;
import javax.swing.ImageIcon;
import javax.swing.JOptionPane;
import java.util.Random;

public class MonteCarlo {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        
        int imageWidth = 250;
        int imageHeight = 250;
        
        BufferedImage img;
        Graphics pen;
        img = new BufferedImage(imageWidth, imageHeight, BufferedImage.TYPE_INT_ARGB);
        pen = img.createGraphics();
        pen.clearRect(0, 0, imageWidth, imageHeight); 
        
        
        
        Shape object1, object2, object3;
        object1 = new Shape(1);
        object2 = new Shape(2);
        object3 = new Shape(3);
        
        Random rngObj = new Random();
        int cnt = 0;
		pen.setColor(Color.GREEN);
		pen.fillRect(1, 1, 250, 250);
        for (int i = 1; i < 100000; i++) {
            double x = rngObj.nextDouble();
            double y = rngObj.nextDouble();
            int j = (int) x * 250;
            int k = (int) y * 250;

            if (object1.contains(x, y)) {
                pen.setColor(Color.RED);
				pen.fillOval(j, k, 250, 250);
                cnt++;
            }
        }
       
        ImageIcon icon = new ImageIcon(img);
        Calculation exp1, exp2, exp3;
        exp1 = new Calculation(1);
        exp2 = new Calculation(2);
        exp3 = new Calculation(3);        
        String title = exp1.title();
        String result = cnt + " in 100000 = " + (double) cnt / 100000 + " [times 4 = " + (double) cnt * 4 / 100000 + "]";
        JOptionPane.showConfirmDialog(null, result, title, JOptionPane.CLOSED_OPTION, JOptionPane.INFORMATION_MESSAGE, icon);
        
        System.out.println(title + ": " + cnt + " in 100000 = " + (double) cnt / 100000 + " [times 4 = " + (double) cnt * 4 / 100000 + "]");
         
    }
    
}
