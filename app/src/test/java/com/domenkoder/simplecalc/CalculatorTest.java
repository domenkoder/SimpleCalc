package com.domenkoder.simplecalc;

import org.junit.Before;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.junit.runners.JUnit4;

import static org.junit.Assert.assertEquals;

@RunWith(JUnit4.class)
public class CalculatorTest {

    private Calculator mCalculator;

    @Before
    public void setUp() {
        mCalculator = new Calculator();
    }

    @Test
    public void addTwoNumbers() {
        double resultAdd = mCalculator.add(1d, 1d);
        assertEquals(2d, resultAdd, 0.01);
    }

    @Test
    public void addTwoNumbersNegative() {
        double resultAdd = mCalculator.add(-1d, 2d);
        assertEquals(1d, resultAdd, 0.01);
    }

    @Test
    public void addTwoNumbersFloats() {
        double resultAdd = mCalculator.add(1.111d, 1.111d);
        assertEquals(2.22, resultAdd, 0.01);
    }

    @Test
    public void subTwoNumbers() {
        double resultSub = mCalculator.sub(1d, 1d);
        assertEquals(0d, resultSub, 0.01);
    }

    @Test
    public void subWorksWithNegativeResult() {
        double resultSub = mCalculator.sub(1d, 17d);
        assertEquals(-16d, resultSub, 0.01);
    }

    @Test
    public void mulTwoNumbers() {
        double resultMul = mCalculator.mul(3d, 3d);
        assertEquals(9d, resultMul, 0.01);
    }

    @Test
    public void divTwoNumbers() {
        double resultDiv = mCalculator.div(32d, 2d);
        assertEquals(16d, resultDiv, 0.01);
    }

    @Test
    public void divZeroDenominator() {
        double resultDiv = mCalculator.div(32d, 0d);
        assertEquals(Double.POSITIVE_INFINITY, resultDiv, 0.01);
    }
}
