/**
 Carrotland
 ==========

 The rabbits are free at last, free from that horrible zombie science experiment.
 They need a happy, safe home, where they can recover.

 You have a dream, a dream of carrots, lots of carrots, planted in neat rows and columns!
 But first, you need some land. And the only person who's selling land is Farmer Frida.
 Unfortunately, not only does she have only one plot of land, she also doesn't know how
 big it is - only that it is a triangle. However, she can tell you the location of the three vertices,
 which lie on the 2-D plane and have integer coordinates.

 Of course, you want to plant as many carrots as you can.
 But you also want to follow these guidelines: The carrots may only be planted at points with integer
 coordinates on the 2-D plane. They must lie within the plot of land and not on the boundaries.
 For example, if the vertices were (-1,-1), (1,0) and (0,1), then you can plant only one carrot at (0,0).

 Write a function answer(vertices), which, when given a list of three vertices,
 returns the maximum number of carrots you can plant.

 The vertices list will contain exactly three elements, and each element will be a list of two integers
 representing the x and y coordinates of a vertex. All coordinates will have absolute value no greater than 1000000000.
 The three vertices will not be collinear.

 Test cases
 ==========

 Inputs:
 (int) vertices = [[2, 3], [6, 9], [10, 160]]
 Output:
 (int) 289

 Inputs:
 (int) vertices = [[91207, 89566], [-88690, -83026], [67100, 47194]]
 Output:
 (int) 1730960165
 */

public class Answer {
    
    public static int answer(int[][] vertices){
        /* Use Pick's Theorem and Heron's Formula to isolate the number of interior points
           area = B/2 + I - 1              */
        double area = areaCalc(vertices);
        if(area == 0){
            return 0;
        }
        double boundary_points = boundaryCalc(vertices);
        double carrots = area - boundary_points/2 + 1;
        int new_carrots = (int) Math.round(carrots);
        return new_carrots;
    }

    private static double areaCalc(int[][] vertices){
        int[] point0 = vertices[0];
        int[] point1 = vertices[1];
        int[] point2 = vertices[2];
        double distance01 = Math.sqrt(Math.pow(point1[0]-point0[0], 2)+Math.pow(point1[1]-point0[1], 2));
        double distance02 = Math.sqrt(Math.pow(point2[0]-point0[0], 2)+Math.pow(point2[1]-point0[1], 2));
        double distance12 = Math.sqrt(Math.pow(point2[0]-point1[0], 2)+Math.pow(point2[1]-point1[1], 2));
        /* Heron's Formula: area = sqrt(s*(s-a)*(s-b)*(s-c))*/
        double s = (distance01+distance02+distance12)/2;
        double a = distance01;
        double b = distance02;
        double c = distance12;
        double area = Math.sqrt(s*(s-a)*(s-b)*(s-c));
        return area;
    }

    private static double boundaryCalc(int[][] vertices){
        double boundaryPoints = 0;
        int[] point0 = vertices[0];
        int[] point1 = vertices[1];
        int[] point2 = vertices[2];
        /* number of lattice points on each line is equivalent to gcd(x,y)+1 when taken from (0,0) to (x,y)
           only use gcd(x,y) so you don't double count the vertices. */
        int[] line01 = {Math.abs(point1[0]-point0[0]), Math.abs(point1[1]-point0[1])};
        int[] line02 = {Math.abs(point2[0]-point0[0]), Math.abs(point2[1]-point0[1])};
        int[] line12 = {Math.abs(point2[0]-point1[0]), Math.abs(point2[1]-point1[1])};
        boundaryPoints += gcd(line01);
        boundaryPoints += gcd(line02);
        boundaryPoints += gcd(line12);
        return boundaryPoints;
    }

    private static int gcd(int[] input){
        int x = input[0];
        int y = input[1];
        if(y==0){
            return x;
        }
        int[] output = {y, x%y};
        return gcd(output);
    }
}
