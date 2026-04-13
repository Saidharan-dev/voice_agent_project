// AddNumbers.java - A simple Java class to add two numbers together.
public class AddNumbers {
    /**
     * Adds two integers together and returns the result.
     *
     * @param num1 First number to add.
     * @param num2 Second number to add.
     * @return The sum of num1 and num2.
     */
    public static int add(int num1, int num2) {
        return num1 + num2;
    }

    /**
     * Adds two double precision numbers together and returns the result.
     *
     * @param num1 First number to add.
     * @param num2 Second number to add.
     * @return The sum of num1 and num2.
     */
    public static double add(double num1, double num2) {
        return num1 + num2;
    }

    /**
     * Adds two strings together (concatenation) and returns the result.
     *
     * @param str1 First string to concatenate.
     * @param str2 Second string to concatenate.
     * @return The concatenation of str1 and str2.
     */
    public static String add(String str1, String str2) {
        return str1 + str2;
    }

    public static void main(String[] args) {
        System.out.println("2 + 3 = " + add(2, 3));
        System.out.println("2.5 + 3.8 = " + add(2.5, 3.8));
        System.out.println("Hello, World! " + add("Hello", "World!"));
    }
}