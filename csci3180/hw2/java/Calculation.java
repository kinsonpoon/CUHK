/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */


import javax.swing.ImageIcon;
import javax.swing.JOptionPane;

public class Calculation {
        
    protected int number;    
    
    public Calculation(int expNumber) {
        
        if (expNumber < 0) {
            number = 0;
        } 
        else {
            number = expNumber;
        }
    }    
    
            public String title() {
            switch (number) {
                case 1:
                    return "Monte Carlo Experiment 1";
                case 2:
                    return "Monte Carlo Experiment 2";
                default:
                    return "Monte Carlo Experiment 3";
            }
    }
}

