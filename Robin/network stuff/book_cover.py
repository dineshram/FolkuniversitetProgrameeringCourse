# coding: utf-8
"""
    This script demonstrates how to build a url that points to the
    image of a book cover in amazon.

    It will display the book cover of any book
    as long as you give it the ISBN-10 number of the book.
"""
import webbrowser


def cover_url(isbn10):
    " cover_url generates a url based on the isbn10 number of\
     a book and returns the amazon url for the book cover image"
    # For details about amazon url, see: http://aaugh.com/imageabuse.html
    # the url requires no whitespace or dashes in the isbn10 format.
    stripped_isbn10 = strip_isbn10(isbn10)
    return "http://images.amazon.com/images/P/%s.01.jpg" % (stripped_isbn10)


def strip_isbn10(isbn10):
    # example input:
    # ISBN  0 - 7195 - 4400
    # output:
    #    "071954400"
    # More on isbn: http://www-math.ucdenver.edu/~wcherowi/jcorner/isbn.html
    return "111890866X"


if __name__ == '__main__':
    url = cover_url(" ISBN-10: 111890866X ")
    print(url)
    webbrowser.open(url)
