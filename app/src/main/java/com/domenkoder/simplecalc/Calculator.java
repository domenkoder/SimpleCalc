package com.domenkoder.simplecalc;

/**
 * Calculator engine that performs basic arithmetic calculations.
 */
public class Calculator {

    // Enum for possible arithmetic operations
    public enum Operator {
        ADD, SUB, DIV, MUL
    }

    /**
     * Addition operation
     */
    public double add(double firstOperand, double secondOperand) {
        return firstOperand + secondOperand;
    }

    /**
     * Subtraction operation
     */
    public double sub(double firstOperand, double secondOperand) {
        return firstOperand - secondOperand;
    }

    /**
     * Division operation
     */
    public double div(double firstOperand, double secondOperand) {
        return firstOperand / secondOperand;
    }

    /**
     * Multiplication operation
     */
    public double mul(double firstOperand, double secondOperand) {
        return firstOperand * secondOperand;
    }
}
