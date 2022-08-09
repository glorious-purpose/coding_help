"""Use OPs code to determine why isorighttri() is printing incorrectly."""


class isosceles_triangle:

    def isotri(self):
        if len(set([self.q, self.e, self.w])) < 3:
            return True
        else:
            return False


class right_triangle:

    def righttri(self):
        if self.q == 90 or self.w == 90 or self.e == 90:
            return True
        else:
            return False


class isosceles_right_triangle(isosceles_triangle,right_triangle):

    def __init__(self,q,w,e):
         self.q=q
         self.w=w
         self.e=e


    def isorighttri (self):
        if self.isotri() is True and self.righttri() is True:
            print ('Triangle is a Isosceles Right Triangle')
        else:
            print ('Triangle is not an Isosceles Right Triangle')

Tri1 = isosceles_right_triangle(45,45,90)
Tri1.isorighttri()
