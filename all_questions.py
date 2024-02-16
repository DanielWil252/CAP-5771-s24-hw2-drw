# Answer found in Q5 in Question Bank 1 (Tan et al, 2nd ed)

# import student_code_with_answers.utils as u
import utils as u


# Example of how to specify a binary with the structure:
# See the file INSTRUCTIONS.md
# ----------------------------------------------------------------------


def question1():
    """
    Note 1: Each attribute can appear as a node in the tree AT MOST once.
    Note 2: For level two, fill the keys for all cases left and right. If and attribute
    is not considered for level 2, set the values to -1. For example, if "flu" were the
    choice for level 1 (it is not), then set level2_left['flu'] = level2_right['flu'] = -1.,
    and the same for keys 'flu_info_gain'.
    """
    answer = False
    answer = {}
    level1 = {}
    level2_left = {}
    level2_right = {}

    level1["smoking"] = 1.
    level1["smoking_info_gain"] = 0.9278071905112637

    level1["cough"] = -1.
    level1["cough_info_gain"] = -1.

    level1["radon"] = -1.
    level1["radon_info_gain"] = -1.

    level1["weight_loss"] = -1.
    level1["weight_loss_info_gain"] = -1.

    level2_left["smoking"] = -1.
    level2_left["smoking_info_gain"] = -1.
    level2_right["smoking"] = -1.
    level2_right["smoking_info_gain"] = -1.

    level2_left["radon"] = -1.
    level2_left["radon_info_gain"] = -1.

    level2_left["cough"] = 1.
    level2_left["cough_info_gain"] = 0.7219280948873623

    level2_left["weight_loss"] = -1.
    level2_left["weight_loss_info_gain"] = -1.

    level2_right["radon"] = 1.
    level2_right["radon_info_gain"] = 0.7219280948873623

    level2_right["cough"] = -1.
    level2_right["cough_info_gain"] = -1.

    level2_right["weight_loss"] = -1.
    level2_right["weight_loss_info_gain"] = -1.

    answer["level1"] = level1
    answer["level2_left"] = level2_left
    answer["level2_right"] = level2_right

    # Fill up `construct_tree``
    # tree, training_error = construct_tree()
    tree = u.BinaryTree("smoke")  # MUST STILL CREATE THE TREE *****
    A = tree.insert_left("cough")
    A.insert_left("y")
    A.insert_right("n")
    B = tree.insert_right("radon")
    B.insert_left("y")
    B.insert_right("y")
    answer["tree"] = tree  # use the Tree structure
    # answer["training_error"] = training_error
    answer["training_error"] = 0.0  

    return answer


# ----------------------------------------------------------------------


def question2():
    answer = {}

    # Answers are floats
    answer["(a) entropy_entire_data"] = 1.4253642047367425
    # Infogain
    answer["(b) x < 0.2"] = 0.17739286055515846
    answer["(b) x < 0.7"] = 0.3557029418697566
    answer["(b) y < 0.6"] = 1.1206115813673811

    # choose one of 'x=0.2', 'x=0.7', or 'x=0.6'
    answer["(c) attribute"] = "y=0.6"  

    # Use the Binary Tree structure to construct the tree
    # Answer is an instance of BinaryTree
    tree = u.BinaryTree("y<=0.6")

    A = tree.insert_left("x<=0.7")
    A.insert_left("B")
    C = A.insert_right("y<=0.3")
    C.insert_left("A")
    C.insert_right("C")#pure nodes

    B = tree.insert_right("x<=0.2")
    B.insert_right("A")
    D = B.insert_left("y<=0.8")
    D.insert_left("C")
    D.insert_right("B")#pure nodes

    answer["(d) full decision tree"] = tree

    return answer


# ----------------------------------------------------------------------


def question3():
    answer = {}

    # float
    answer["(a) Gini, overall"] = 0.5

    # float
    answer["(b) Gini, ID"] = 0.
    answer["(c) Gini, Gender"] = 0.48
    answer["(d) Gini, Car type"] = 0.1625
    answer["(e) Gini, Shirt type"] = 0.4914

    answer["(f) attr for splitting"] = "Car"

    # Explanatory text string
    answer["(f) explain choice"] = "It has the lowest gini value."

    return answer


# ----------------------------------------------------------------------
# Answers in th form [str1, str2, str3]
# If both 'binary' and 'discrete' apply, choose 'binary'.
# str1 in ['binary', 'discrete', 'continuous']
# str2 in ['qualitative', 'quantitative']
# str3 in ['interval', 'nominal', 'ratio', 'ordinal']


def question4():
    answer = {}

    # [string, string, string]
    # Each string is one of ['binary', 'discrete', 'continuous', 'qualitative', 'nominal', 'ordinal',
    #  'quantitative', 'interval', 'ratio'
    # If you have a choice between 'binary' and 'discrete', choose 'binary'

    answer["a"] = ['binary','qualitative','ordinal']

    # Explain if there is more than one interpretation. Repeat for the other questions. At least five words that form a sentence.
    answer["a: explain"] = "AM and PM are binary representations of time. They dont distincly represent numbers, so they are qualitative. Since AM naturally comes first before PM, it is ordinal."

    answer["b"] = ['continuous','quantitative','ratio']
    answer["b: explain"] = "Light meters measure light in continous numerical values, and there is a clear zero."

    answer["c"] = ['discrete','qualitative','ordinal']
    answer["c: explain"] = "People measuring light based on their eyesight would wont have specific values in mind, but generalizations. The generalizations are ordinal since they would still be ranked by the brightness of light."

    answer["d"] = ['continuous','quantitative','ratio']
    answer["d: explain"] = "Degrees can be continuous, and have a specific zero point."

    answer["e"] = ['discrete','qualitative','ordinal']
    answer["e: explain"] = "The medals themselves do not represent any numerical value, so they are qualitative. They are ordinal because there is a distinct ranking between their value."

    answer["f"] = ['countinuous','quantitative','interval']
    answer["f: explain"] = "The height above sea level is measured in a continuous, quantitative manner. However, ratio vs interval can be debated because zero sea level can be different around the world."

    answer["g"] = ['discrete','quantitative','ratio']
    answer["g: explain"] = "the amount of patients in a hospital is discrete and measured numerically. There can also be zero patients, so it can be ratioed."

    answer["h"] = ['discrete','qualitative','nominal']
    answer["h: explain"] = "isbn numbers dont necessarily represent anything other than the book they are assigned to. there also isnt a clear ranking for them (Im not sure if isbn numbers are in order of release)"

    answer["i"] = ['discrete','qualitative','ordinal']
    answer["i: explain"] = "the words used to describe the light cannot be continuous, and dont hold a specific value. They can, however, can be ranked in order."

    answer["j"] = ['discrete','qualitative','ordinal']
    answer["j: explain"] = "Military ranks are clear in level of power, but dont represent numbers and are not continuous."

    answer["k"] = ['continuous','quantitative','ratio']
    answer["k: explain"] = "the distance from a certain point is continuous and holds numerical value. Whether or not it is a ratio or an interval depends on whether that distance is considered a zero point or not (I think it is in this case)"

    answer["l"] = ['discrete','quantitative','ratio']
    answer["l: explain"] = "density is a measurement that is continuous and quantitative. There is also a set zero point."

    answer["m"] = ['discrete','qualitative','nominal']
    answer["m: explain"] = "A count number would have to be discrete and does not really represent anything numerically. Since Id like to imagine there isnt an order of coats, it would be nominal."

    return answer


# ----------------------------------------------------------------------


def question5():
    explain = {}

    # Read appropriate section of book chapter 3

    # string: one of 'Model 1' or 'Model 2'
    explain["a"] = "Model 2"
    explain["a explain"] = "While model 1 is more accurate in on Dataset A, that dataset was used to train the data itself. Since dataset B is a seperate testing set, Model 2's higher score in classification accuracy than A in this dataset shows that it would be more accurate for new data than model 1."

    # string: one of 'Model 1' or 'Model 2'
    explain["b"] = "Model 1"
    explain["b explain"] = "Given just the accuracies, I would choose model 1 over model 2."

    explain["c similarity"] = ""
    explain["c similarity explain"] = "Both MDL and the pessimistic error estimate aim to prevent overfitting by penalizing the model if it is overcomplex."

    explain["c difference"] = ""
    explain["c difference explain"] = "MDL and pessimistic error estimate operate differently to achieve a similar goal. MDL achieves this by selecting a model that compresses the data to the smallest size, while pessimistic error estimate directly adds penalties to the error rate based on the complexity of the model."

    return explain


# ----------------------------------------------------------------------
def question6():
    answer = {}
    # x <= ? is the left branch
    # y <= ? is the left branch

    # value of the form "z <= float" where "z" is "x" or "y"
    #  and "float" is a floating point number (notice: <=)
    # The value could also be "A" or "B" if it is a leaf
    answer["a, level 1"] = "y<=.4"
    answer["a, level 2, right"] ="x<=.5"
    answer["a, level 2, left"] = "A"
    answer["a, level 3, left"] = "x<=.2"
    answer["a, level 3, right"] = "A"

    # run each datum through the tree. Count the number of errors and divide by number of samples. .
    # Since we have areas: calculate the area that is misclassified (total area is unity)
    # float between 0 and 1
    answer["b, expected error"] = 0.060

    # Use u.BinaryTree to define the tree. Create your tree.
    # Replace "root node" by the proper node of the form "z <= float"
    tree = u.BinaryTree("y<=.4")
    tree.insert_left("A")
    
    A = tree.insert_right("x<=.5")
    A.insert_right("A")

    B = A.insert_left("x<=.2")
    B.insert_right("B")
    B.insert_left("A")#Either one has the same odds.


    answer["c, tree"] = tree

    return answer


# ----------------------------------------------------------------------
def question7():
    answer = {}

    # float
    answer["a, info gain, ID"] = 1. #same as root entropy, since entropy for ID is 0
    answer["b, info gain, Handedness"] = 0.9531004406410719

    # string: "ID" or "Handedness"
    answer["c, which attrib"] = "ID"

    # answer is a float
    answer["d, gain ratio, ID"] = 0.23137821315975915
    answer["e, gain ratio, Handedness"] = 0.4321928094887363

    # string: one of 'ID' or 'Handedness' based on gain ratio
    # choose the attribute with the largest gain ratio
    answer["f, which attrib"] = "Handedness"

    return answer


# ----------------------------------------------------------------------

if __name__ == "__main__":
    answers = {}
    answers["q1"] = question1()
    answers["q2"] = question2()
    answers["q3"] = question3()
    answers["q4"] = question4()
    answers["q5"] = question5()
    answers["q6"] = question6()
    answers["q7"] = question7()

    u.save_dict("answers.pkl", answers)

