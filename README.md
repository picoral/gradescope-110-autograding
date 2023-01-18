# Creating Gradescope Autograded Practice Problems for CSc 110

1. Check contents for modules on [website](https://adrianapicoral.com/csc-110/)
1. Following the pattern of [other problems](https://adrianapicoral.com/csc-110/assignments-02.html), create the wording of your practice problem
1. Once you have the first draft of the problem prompt, create a solution for your problem.
1. Open the [autograder folder example](assignment-04/autograder/) and modify:
  * [run_autograder](assignment-04/autograder/run_autograder) to match the filename you expect students to submit
  * [test_return.py](assignment-04/autograder/tests/test_return.py) to import the correct module and run your tests
1. Compress all contents of the autograder folder into one .zip file
1. Access practice Gradescope course (ask Adriana for the Entry Code) and create a new programming assignment
1. Add a title and number of points to your programming assignment settings, and release and due dates and click on "create assignment"
1. To configure the autograder, click on "Upload Autograder (.zip)" button and upload the .zip file you created
1. Wait for it to build
1. Once built, click on "Test Autograder" and submit your solution

For more information on creating autograders for gradescope:

* https://gradescope-autograders.readthedocs.io/en/latest/specs
* https://gradescope-autograders.readthedocs.io/en/latest/python/