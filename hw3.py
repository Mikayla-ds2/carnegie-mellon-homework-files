### CS Scholars - Programming Hw3 - Code
### Due Date: Friday 07/12 EOD
### Name: Mikayla Solomon
### andrewID: mikaylas

import math
import tkinter
import random

### Review Problems ###

''' #5 - getAllWords '''
def getAllWords(text):
    s = 'the quick brown fox jumps over the lazy dog'
    lowercaseString = s.lower()
    s = lowercaseString
    splitString = s.split()
    finalString = splitString
    finalString = ""
    word = ""

    while word in finalString:
        if word not in finalString:
            finalString += word
    return finalString
    finalResultString = finalString.sort()
    return finalResultString


''' #6 - Book Class '''
class Book:
   def __init__(self,title,author,pages):
    self.title = title
    self.author = author
    self.pages = pages
    self.currentPage = 1 
    self.bookmarkedPage = None
    def turnPage(self, destination):
        if destination >0:
            self.currentPage += destination
        elif destination <0:
            self.currentPage -= destination
        if self.currentPage >= self.pages and self.currentPage <0:
            self.currentPage = 1 
        return None
    def placeBookmark():
        self.bookmarkedPage = self.currentPage
        return None
    def removeBookmark():
        self.bookmarkedPage = None
        return None
    def __repr__(self):
        return str(title) + 'by' + str(author) + 'with' + str(pages) + 'pages' + 'currently on page' + str(self.currentPage)
    def __repr__(self):
        return str(title) + 'by' + str(author) + 'with' + str(pages) + 'pages' + 'currently on page' + str(self.currentPage) + 'page' + str(self.bookmarkedPage)

### Core Problems ###

''' #7 - getSecretMessage '''
def getSecretMessage(s, key):
    s = ''
    l = s.split('q')
    ans = ''
    for item in l:
        ans += item[0]


''' #8 - sumAnglesAsDegrees '''
def sumAnglesAsDegrees(angles):
    degreeAngles = [] 
    sumOfAngles = 0
    for angle in angles:
        sumOfAngles += math.degrees(angle)
    return sumOfAngles

''' #9 - makeIMDB '''
def makeIMDB(actorList, movieList):
    d = {}
    for i in range(len(actorList)):
        if actorList[i] not in d:
            d[actorList[i]] = movieList[i]  
    return


''' #10 - Inheritance '''
''' Define your classes under this line and before demoClasses '''
class Students:
    def __init__(self,name, age,year,GPA):
        self.age = age
        self.year = year
        self.GPA = GPA
        self.name = name
    def completeAssignment(grade):
        GPA = 0
        if 0 <= grade <= 50:
            print('Fail')
            if GPA <0: 
                GPA = 0
            else: GPA -= 1
        elif 51 <= grade <= 100:
            print('Pass')
            if GPA >4:
                GPA = 4
            else: GPA += 1
    def completeTest(grade):
        GPA = 0
        if 0 <= grade <= 50:
            print('Fail')
            if GPA <0: 
                GPA = 0
            else: GPA -= 2
        elif 51 <= grade <= 100:
            print('Pass')
            if GPA >4:
                GPA = 4
            else: GPA += 2
class Senior(Students):
    def __init__(self, name, age, year, GPA, collegeList):
        self.age = age
        self.year = year
        self.GPA = GPA
        self.name = name
        self.collegeList = collegeList
    def graduate(name):
        print('I am done with high school')
    def completeTest(grade):
        GPA = 0
        extraCredit = True
        if extraCredit == True:
            GPA += 0.5
        else: return GPA
        if 0 <= grade <= 50:
            print('Fail')
            if GPA <0: 
                GPA = 0
            else: GPA -= 2
        elif 51 <= grade <= 100:
            print('Pass')
            if GPA >4:
                GPA = 4
            else: GPA += 2
    def __repr__(self):
        return f"[{self.name}, who is {self.age} years old, and I want to go to these colleges: {self.collegeList}]"
    
def demoClasses():
    Nadia = Students("Nadia", 16,11,3)
    print(Nadia.completeAssignment(89))
    Grace = Senior('Grace', 17,12,4,'HCC')
    print(Grace.__repr__)
    return


### Spicy Problems ###

''' #11 - getCharacterLines '''
def getCharacterLines(script, character):
    return


''' #12 - Radio Class '''
class Radio:
    pass


### Bonus Problems ###

''' Advanced Programming 1 - Trees '''
def getInitialTeams(bracket):
    return


''' Advanced Programming 2 - Graphs '''
def getPrereqs(g, course):
    return


##############################################################
### Test Functions ###

def testGetAllWords():
    print("Testing getAllWords()...", end="")
    assert(getAllWords("Hello and Welcome to CS Scholars") == [ "and", "cs", "hello", "scholars", "to", "welcome" ])
    assert(getAllWords("I like to repeat REPEAT myself I like to repeat Repeat") == [ "i", "like", "myself", "repeat", "to" ])
    assert(getAllWords("coding CODING Coding codinG") == [ "coding" ])
    assert(getAllWords("WOW") == [ "wow" ])
    print("... done!")

def testBookClass():
    print("Testing Book class...", end="")
    # A Book has a title, and author, and a number of pages.
    # It also has a current page, which always starts at 1. There is no page 0!
    book1 = Book("Harry Potter and the Sorcerer's Stone", 
                 "J. K. Rowling", 309)
    assert(book1.title == "Harry Potter and the Sorcerer's Stone")
    assert(book1.author == "J. K. Rowling")
    assert(book1.pages == 309)
    assert(book1.currentPage == 1)
    assert(str(book1) == "Book<Harry Potter and the Sorcerer's Stone by " + 
                         "J. K. Rowling: 309 pages, currently on page 1>")
    
    book2 = Book("Carnegie Mellon Motto", "Andrew Carnegie", 2)
    assert(book2.title == "Carnegie Mellon Motto")
    assert(book2.author == "Andrew Carnegie")
    assert(book2.pages == 2)
    assert(book2.currentPage == 1)
    assert(str(book2) == "Book<Carnegie Mellon Motto by Andrew Carnegie: " +
                         "2 pages, currently on page 1>")
                         
    # You can turn pages in a book. Turning a positive number of pages moves
    # forward; turning a negative number moves backwards. You can't move past
    # the first page going backwards or the last page going forwards
    book1.turnPage(4) # turning pages does not return
    assert(book1.currentPage == 5)
    book1.turnPage(-1)
    assert(book1.currentPage == 4)
    book1.turnPage(400)
    assert(book1.currentPage == 309)
    assert(str(book1) == "Book<Harry Potter and the Sorcerer's Stone by " + 
                         "J. K. Rowling: 309 pages, currently on page 309>")
    book2.turnPage(-1)
    assert(book2.currentPage == 1)
    book2.turnPage(2)
    assert(book2.currentPage == 2)
    
    # You can also put a bookmark on the current page. This lets you turn
    # back to it easily. The book starts out without a bookmark.
    book3 = Book("The Name of the Wind", "Patrick Rothfuss", 662)
    assert(str(book3) == "Book<The Name of the Wind by Patrick Rothfuss: " + \
                         "662 pages, currently on page 1>")
    assert(book3.bookmarkedPage == None)
    book3.turnPage(9)
    book3.placeBookmark() # does not return
    assert(book3.bookmarkedPage == 10)
    book3.turnPage(7)
    assert(book3.bookmarkedPage == 10)
    assert(book3.currentPage == 17)
    assert(str(book3) == "Book<The Name of the Wind by Patrick Rothfuss: " + \
                         "662 pages, currently on page 17, page 10 bookmarked>")
    book3.turnToBookmark()
    assert(book3.currentPage == 10)
    book3.removeBookmark()
    assert(book3.bookmarkedPage == None)
    book3.turnPage(25)
    assert(book3.currentPage == 35)
    book3.turnToBookmark() # if there's no bookmark, don't turn to a page
    assert(book3.currentPage == 35)
    assert(str(book3) == "Book<The Name of the Wind by Patrick Rothfuss: " + \
                         "662 pages, currently on page 35>")
    
    print("Done!")

def testGetSecretMessage():
    print("Testing getSecretMessage()...", end="")
    assert(getSecretMessage("orupqcrzypqomqmhcyqpwhhqutqtxtqeyeqrpa", "q") == "computer")
    assert(getSecretMessage("cowkscaoktbphakebakltvklmtkau", "k") == "stella")
    assert(getSecretMessage("xwuexoerxwdf", "x") == "wow")
    assert(getSecretMessage("faqfxwuexoerxw", "x") == "wow")
    assert(getSecretMessage("faqfxwuexoxwdf", "x") == "wow")
    assert(getSecretMessage("xwxoxw", "x") == "wow")
    assert(getSecretMessage("", "a") == "")
    print("... done!")

def testSumAnglesAsDegrees():
    print("Testing sumAnglesAsDegrees()...", end="")
    assert(sumAnglesAsDegrees([math.pi/6, math.pi/4, math.pi]) == 255)
    assert(sumAnglesAsDegrees([math.pi/4, math.pi/4, math.pi/4, math.pi/4]) == 180)
    assert(sumAnglesAsDegrees([math.pi/6, math.pi/6]) == 60)
    assert(sumAnglesAsDegrees([math.pi/2]) == 90)
    assert(sumAnglesAsDegrees([math.pi/6, math.pi/3, math.pi/3, math.pi, math.pi/6]) == 360)
    assert(sumAnglesAsDegrees([]) == 0)
    print("... done!")

def testMakeIMDB():
    print("Testing makeIMDB()...", end="")
    assert(makeIMDB(["Ni Ni", "Sofia Vergara", "Ni Ni"], ["Suddenly Seventeen", "Hot Pursuit", "Love Will Tear Us Apart"]) == { "Ni Ni" : "Suddenly Seventeen", "Sofia Vergara" : "Hot Pursuit" })
    assert(makeIMDB(["Ni Ni", "Chen Kun", "Sofia Vergara", "Halle Berry"], ["The flowers of War", "Beautiful Accident", "Modern Family", "Robots"]) == { "Ni Ni" : "The flowers of War", "Chen Kun" : "Beautiful Accident", "Sofia Vergara" : "Modern Family", "Halle Berry" : "Robots" })
    assert(makeIMDB(["Will Smith", "Will Smith", "Will Smith"], ["Man in Black 3", "Man in Black 2", "Man in Black 1"]) == { "Will Smith" : "Man in Black 3" })
    assert(makeIMDB(["Keanu Reeves"], ["The Matrix"]) == { "Keanu Reeves" : "The Matrix" })
    assert(makeIMDB(["Ni Ni", "Ni Ni", "Sofia Vergara"], ["Suddenly Seventeen", "Love Will Tear Us Apart", "Hot Pursuit"]) == { "Ni Ni" : "Suddenly Seventeen", "Sofia Vergara" : "Hot Pursuit" })
    assert(makeIMDB([ ], [ ]) == { })
    print("... done!")

def testGetCharacterLines():
    print("Testing getCharacterLines()...", end="")
    s1 = '''
Buttercup: You mock my pain.
Man in Black: Life is pain, Highness.
Man in Black: Anyone who says differently is selling something.
'''.strip()
    assert(getCharacterLines(s1, "Buttercup") == [ "You mock my pain." ])
    assert(getCharacterLines(s1, "Man in Black") == [ "Life is pain, Highness.",
        "Anyone who says differently is selling something." ])
    assert(getCharacterLines(s1, "Inigo Montoya") == [ ])

    s2 = '''
Burr: Can I buy you a drink?
Hamilton: That would be nice.
Burr: While we're talking, let me offer you some free advice: talk less.
Hamilton: What?
Burr: Smile more.
Hamilton: Ha.
Burr: Don't let them know what you're against or what you're for.
Hamilton: You can't be serious.
Burr: You want to get ahead?
Hamilton: Yes.
Burr: Fools who run their mouths oft wind up dead.
'''.strip()
    assert(getCharacterLines(s2, "Hamilton") == [ "That would be nice.",
        "What?", "Ha.", "You can't be serious.", "Yes." ])
    assert(getCharacterLines(s2, "Burr") == [ "Can I buy you a drink?",
        "While we're talking, let me offer you some free advice: talk less.", "Smile more.", "Don't let them know what you're against or what you're for.", "You want to get ahead?", "Fools who run their mouths oft wind up dead." ])

    s3 = '''
Luke: Look at him. He's headed for that small moon.
Han: I think I can get him before he gets there... he's almost in range.
Ben: That's no moon! It's a space station.
Han: It's too big to be a space station.
Luke: I have a very bad feeling about this.
'''.strip()
    assert(getCharacterLines(s3, "Luke") == [ "Look at him. He's headed for that small moon.", "I have a very bad feeling about this." ])
    assert(getCharacterLines(s3, "Han") == [ "I think I can get him before he gets there... he's almost in range.", "It's too big to be a space station." ])
    assert(getCharacterLines(s3, "Ben") == [ "That's no moon! It's a space station." ])

    s4 = '''
Threepio: Did you hear that? They've shut down the main reactor. We'll be destroyed for sure. This is madness!
Threepio: We're doomed!
Threepio: There'll be no escape for the Princess this time.
Threepio: What's that?
'''.strip()
    assert(getCharacterLines(s4, "Threepio") == [ "Did you hear that? They've shut down the main reactor. We'll be destroyed for sure. This is madness!", "We're doomed!", "There'll be no escape for the Princess this time.", "What's that?"])

    print("... done!")

def testRadioClass():
    print("Testing Radio class...", end="")
    # A Radio has a list of channels, a volume, and a current channel
    # The current channel defaults to the first channel in the list
    radio1 = Radio([94.5, 96.1, 102.5, 104.7, 105.9], 5)
    assert(radio1.channels == [94.5, 96.1, 102.5, 104.7, 105.9])
    assert(radio1.volume == 5)
    assert(radio1.current == 94.5)
    assert(str(radio1) == "Radio<Channels 94.5, 96.1, 102.5, 104.7, 105.9. " + \
                          "Current channel is 94.5. Volume set to 5.>")
    
    radio2 = Radio([93.3, 96.7, 97.1, 100.3, 101.3, 102, 102.5, 108], 9)
    assert(radio2.channels == [93.3, 96.7, 97.1, 100.3, 101.3, 102, 102.5, 108])
    assert(radio2.volume == 9)
    assert(radio2.current == 93.3)
    assert(str(radio2) == "Radio<Channels 93.3, 96.7, 97.1, 100.3, 101.3, 102, 102.5, 108. " + \
                          "Current channel is 93.3. Volume set to 9.>")
    
    # Properties can be modified directly
    radio1.volume += 3
    assert(radio1.volume == 8)
    assert(str(radio1) == "Radio<Channels 94.5, 96.1, 102.5, 104.7, 105.9. " + \
                          "Current channel is 94.5. Volume set to 8.>")
    
    # Seeking a new channel works both forward and backward, and with wrap-around
    radio2.seek(2)
    assert(radio2.current == 97.1)
    radio2.seek(-5)
    assert(radio2.current == 102)
    assert(str(radio2) == "Radio<Channels 93.3, 96.7, 97.1, 100.3, 101.3, 102, 102.5, 108. " + \
                          "Current channel is 102. Volume set to 9.>")
    
    # Going directly to a channel goes to that channel if it exists,
    # or the nearest channel if it doesn't
    radio1.goToChannel(104.7)
    assert(radio1.current == 104.7)
    radio2.goToChannel(100.1)
    assert(radio2.current == 100.3)
    radio2.goToChannel(101.5)
    assert(radio2.current == 101.3)
    
    # The user can keep track of their favorite channels in a list.
    # Each channel can only appear once.
    assert(radio1.favorites == [])
    radio1.addFavorite() # adds the current channel, 104.7
    assert(radio1.favorites == [104.7])
    radio1.addFavorite()
    assert(radio1.favorites == [104.7]) # no duplicates
    radio1.seek(2) # moved to 94.5
    radio1.addFavorite()
    assert(radio1.favorites == [104.7, 94.5])
    assert(str(radio1) == "Radio<Channels 94.5, 96.1, 102.5, 104.7, 105.9. " + \
                          "Current channel is 94.5. Volume set to 8. " + \
                          "Favorite channels are 104.7, 94.5.>")
    
    # The user can go directly to a favorite channel based on its index
    radio1.goToFavorite(0)
    assert(radio1.current == 104.7)
    radio1.goToFavorite(2) # invalid indexes are ignored
    assert(radio1.current == 104.7)
    print("Done!")

def testGetInitialTeams():
    print("Testing getInitialTeams()...", end="")
    # An order of teams is not specified, so we'll
    # sort your result before checking it
    t1 = { "contents" : "United States",
           "left"  : { "contents" : "United States",
                       "left"  : { "contents" : "England",
                                   "left"  : None,
                                   "right" : None
                                 },
                       "right" : { "contents" : "United States",
                                   "left"  : None,
                                   "right" : None
                                 }
                     },
            "right" : { "contents" : "Netherlands",
                        "left"  : { "contents" : "Netherlands",
                                    "left"  : None,
                                    "right" : None
                                  },
                        "right" : { "contents" : "Sweden",
                                    "left"  : None,
                                    "right" : None
                                  }
                     }
         }
    assert(sorted(getInitialTeams(t1)) == [ "England", "Netherlands", "Sweden", "United States" ])
    t2 = { "contents" : "CMU",
           "left"  : { "contents" : "CMU",
                       "left"  : None,
                       "right" : None
                     },
            "right" : { "contents" : "MIT",
                        "left"  : None,
                        "right" : None
                     }
         }
    assert(sorted(getInitialTeams(t2)) == [ "CMU", "MIT" ])
    t3 = { "contents" : "Kansas City",
           "left"  : { "contents" : "Kansas City",
                       "left"  : { "contents" : "Tennessee",
                                   "left"  : { "contents" : "Tennessee",
                                               "left"  : None,
                                               "right" : None
                                             },
                                   "right" : { "contents" : "Baltimore",
                                               "left"  : None,
                                               "right" : None
                                             }
                                 },
                       "right" : { "contents" : "Kansas City",
                                   "left"  : { "contents" : "Houston",
                                               "left"  : None,
                                               "right" : None
                                             },
                                   "right" : { "contents" : "Kansas City",
                                               "left"  : None,
                                               "right" : None
                                             }
                                 }
                     },
            "right" : { "contents" : "San Francisco",
                        "left"  : { "contents" : "San Francisco",
                                    "left"  : { "contents" : "Minnesota",
                                               "left"  : None,
                                               "right" : None
                                             },
                                    "right" : { "contents" : "San Francisco",
                                               "left"  : None,
                                               "right" : None
                                             }
                                  },
                        "right" : { "contents" : "Green Bay",
                                    "left"  : { "contents" : "Seattle",
                                               "left"  : None,
                                               "right" : None
                                             },
                                    "right" : { "contents" : "Green Bay",
                                               "left"  : None,
                                               "right" : None
                                             }
                                  }
                     }
         }
    assert(sorted(getInitialTeams(t3)) == [ "Baltimore", "Green Bay", "Houston", "Kansas City", "Minnesota", "San Francisco", "Seattle", "Tennessee" ])
    t4 = { "contents" : "Five Guys",
           "left"  : { "contents" : "Five Guys",
                       "left"  : { "contents" : "Five Guys",
                                   "left"  : None,
                                   "right" : None
                                 },
                       "right" : { "contents" : "Shake Shack",
                                   "left"  : { "contents" : "Steak 'n Shake",
                                               "left"  : None,
                                               "right" : None
                                             },
                                   "right" : { "contents" : "Shake Shack",
                                               "left"  : None,
                                               "right" : None
                                             }
                                 }
                     },
            "right" : { "contents" : "Culver's",
                        "left"  : { "contents" : "In-n-Out",
                                    "left"  : None,
                                    "right" : None
                                  },
                        "right" : { "contents" : "Culver's",
                                    "left"  : None,
                                    "right" : None
                                  }
                     }
         }
    assert(sorted(getInitialTeams(t4)) == [ "Culver's", "Five Guys", "In-n-Out", "Shake Shack", "Steak 'n Shake" ])
    t5 = { "contents" : "Stella",
           "left"  : None,
           "right" : None
         }
    assert(getInitialTeams(t5) == [ "Stella" ])
    print("... done!")

def testGetPrereqs():
    print("Testing getPrereqs()...", end="")
    g = { "110" : [],
        "112" : ["122", "150"],
        "122" : ["213", "210", "251", "281"],
        "150" : ["210", "251"],
        "151" : ["150", "251", "281"],
        "210" : [],
        "213" : [],
        "251" : [],
        "281" : [] }
    # An order of courses is not specified, so we'll
    # sort your result before checking it
    assert(getPrereqs(g, "210") != None)
    assert(sorted(getPrereqs(g, "210")) == ["122", "150"])
    assert(sorted(getPrereqs(g, "251")) == ["122", "150", "151"])
    assert(getPrereqs(g, "213") == ["122"])
    assert(getPrereqs(g, "150") == ["112", "151"])
    assert(getPrereqs(g, "112") == [])
    assert(getPrereqs(g, "110") == [])

    g2 = { "Differential and Integral Calculus" : ["Integration and Approximation",
                                                   "Multivariate Analysis"],
           "Integration and Approximation" : ["Calculus in Three Dimensions",
                                              "Differential Equations",
                                              "Operations Research I"],
           "Concepts of Mathematics" : ["Discrete Mathematics"],
           "Discrete Mathematics" : ["Operations Research I"],
           "Matrices and Linear Transformations" : ["Operations Research I"],
           "Multivariate Analysis" : [],
           "Calculus in Three Dimensions" : [],
           "Differential Equations" : [],
           "Operations Research I" : [] }
    assert(sorted(getPrereqs(g2, "Operations Research I")) == ["Discrete Mathematics", "Integration and Approximation", "Matrices and Linear Transformations"])
    assert(getPrereqs(g2, "Discrete Mathematics") == ["Concepts of Mathematics"])
    assert(getPrereqs(g2, "Matrices and Linear Transformations") == [])
    print("... done!")


def testReview():
    testGetAllWords()
    testBookClass()

def testCore():
    testGetSecretMessage()
    testSumAnglesAsDegrees()
    testMakeIMDB()

    print("Running demoClasses()... manually check your work.")
    demoClasses()

def testSpicy():
    testGetCharacterLines()
    testRadioClass()

def testAdvanced():
    testGetInitialTeams()
    testGetPrereqs()

def testAll():
    # Uncomment this if you're doing Review + Core
    #testReview()

    testCore()

    # Uncomment this if you're doing Core + Spicy
    #testSpicy()
    
    # Uncomment this is you're doing the bonus problems
    #testAdvanced()

testAll()