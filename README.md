# ASCII Regular Polygon Generator

This script was written as a part our PA work for the **Programming Languages and Compiler Construction**
course running in the 2<sup>nd</sup> semester, 2012 at [BITS - Pilani, KK Birla Goa Campus][1], under the
guidance of Mr. Ramprasad Joshi and Mr. Durgesh Samant

## Synopsis

Students were asked to develop a parser with flex and bison which could identify and name regular polygons.
This script was meant to aid the process of evaluation by generating input to test the students' code. 

It takes the number of sides of the polygon as input and outputs the corresponding bitmap.
For drawing the bitmap, [Bresenham's Line Algorithm is used][2]. For larger shapes like octagon and nonagon,
the bitmaps are not very clear unless the size of the overall bitmap is made bigger.

[1]: http://universe.bits-pilani.ac.in/Goa/ 
[2]: http://en.wikipedia.org/wiki/Bresenham%27s_line_algorithm

## Usage

    $ python shape-generator.py -h
    Usage: generator.py [options]
    Options:
    -h, --help                  show this help message and exit
    -n N, --sides=N             number of sides in the polygon
    -r R, --radius=R            radius of circle into which the polygon is inscribed
    -t THETA, --theta=THETA     angle to rotate the polygon by (in degrees), for eg: 90

## Example

    $ python generator.py -n 3 -r 10
    000000000000000000000000000000
    000000000000000000000000000000
    000000000000000000000000000000
    000000000000000000000000000000
    000000000000000000000000000000
    000000000010000000000000000000
    000000000011100000000000000000
    000000000010011000000000000000
    000000000010000100000000000000
    000000000010000011000000000000
    000000000010000000110000000000
    000000000010000000001000000000
    000000000010000000000110000000
    000000000010000000000001100000
    000000000010000000000000010000
    000000000010000000000001100000
    000000000010000000000110000000
    000000000010000000001000000000
    000000000010000000110000000000
    000000000010000011000000000000
    000000000010000100000000000000
    000000000010011000000000000000
    000000000011100000000000000000
    000000000010000000000000000000
    000000000000000000000000000000
    000000000000000000000000000000
    000000000000000000000000000000
    000000000000000000000000000000
    000000000000000000000000000000
    000000000000000000000000000000

## Contact

  * rachee.singh@gmail.com
  * emaadmanzoor@gmail.com
