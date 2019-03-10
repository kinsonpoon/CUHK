

public class Shape {

    protected int type;

    /**
     * Constructor creating a new Shape object of a given type.
     *
     * @param newShapeType int; 1 means circle; 2 means square; 3 means triangle
     */
    public Shape(int newShapeType) {
        if (newShapeType < 0) {
            type = 0;
        } else {
            type = newShapeType;
        }
    }

    /**
     * shapeObject.contains(x, y) tells if a given point (x, y) falls in a shape
     * object. Type of the shape object shall be determined during object
     * creation.
     *
     * @param x double in [0.0, 1.0)
     * @param y double in [0.0, 1.0)
     * @return boolean
     */
    public boolean contains(double x, double y) {
        // non-OO treatment as an learning example
        double baseSize = 1.0;
        switch (type) {
            case 1:
                return formula_circle(x, y, 0.5, 0.5, baseSize * 0.5);
            case 2:
                return formula_square(x, y, baseSize * 0.5);
            case 3:
                return formula_right_triangle(x, 1.0 - y, 1.0, 0.0); // flip-y
        }
        // default:
        return true;
    }

    protected boolean formula_circle(double x, double y, double centerX, double centerY, double radius) {
        return ((x - centerX) * (x - centerX) + (y - centerY) * (y - centerY) < radius * radius);
    }

    protected boolean formula_square(double x, double y, double side) {
        return (-side < x && x < side && -side < y && y < side);
    }

    protected boolean formula_right_triangle(double x, double y, double slope, double interceptY) {
        // line equation y = m x + c
        return (y > x * slope + interceptY);
    }
}
