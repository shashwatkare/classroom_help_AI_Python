# Image Classification for a City Dog Show

NOTE: We ask you to focus on Python and not on the actual classifier.

#### Quick Description: There is a Dog Show and people are submitting their dog pictures for registration approvals.The pre-trained classifier will be used to determine if the dog is a dog or not and what are the additional infomration provided with the pictures.

### Overall Objective:

1. Correctly identify which pet images are of dogs (even if the breed is misclassified) and which pet images aren't of dogs. 
2. Correctly classify the breed of dog, for the images that are of dogs. 
3. Determine which CNN model architecture (ResNet, AlexNet, or VGG), "best" achieve objectives 1 and 2.
4. Consider the time resources required to best achieve objectives 1 and 2, and determine if an alternative solution would have given a "good enough" result, given the amount of time each of the algorithms takes to run.

##### Tech Jargon to remember:
* Deep Learning Model: Convolutional Neural Network (CNN) - Great for image classification as it can detect features like color, shape, and texture.
* Differnet CNN architectures:
    * AlexNet
    * VGGNet
    * ResNet


The classifier code logic is in classifier.py and you need to use python knowledge learned till date to complete it.
To test how original classifier should work, you can use the test_classifier.py script.

NOTE: There are few dog breeds that looks similar which are but not limited to Great Pyrenees and Kuvasz, German Shepherd and Malinois, Beagle and Walker Hound, amongst others.

-----------------------------------------------------------------------------------------------------------------------

### TODO's 

Project can be easily solved by following TODO's below.

A. **TODO 0's can be found in check_images.py file. [Timing the code]**
1. Line 5: Add your information below for Programmer & Date Created - {put your name and date you started working on this project}
2. Line 42: Measures total program runtime by collecting start time - {Think if you can use time Library and provide a value to start_time variable}
3. Line 118: Measure total program runtime by collecting end time - {Provide value to end_time variable} 
4. Line 121: Computes overall runtime in seconds & prints it in hh:mm:ss format - {Simple math calculation to compute overall runtime in seconds}

#### If any confusion head here to check the detailed explanation ![LINK](https://classroom.udacity.com/nanodegrees/nd089/parts/cd0184/modules/172bc12e-2000-484d-8095-33899ed05418/lessons/7846dc05-3417-4e32-b0f2-afd7aa6fe0aa/concepts/3ee000f9-1867-4fc9-9a23-da442d7f9f39)

-----------------------------------------------------------------------------------------------------------------------
B. **TODO 1's can be found in get_input_args.py file. [Command Line Arguments]**

1. For function get_input_args you will be using a library called argparse.
2. Remember this module argparse is used to allow arguments to be passed withing the command line. same as you do "python --version", this --version part is added using argparse.
3. To understand easily you can check get_input_args_hint.py script.
4. Be mindful to return correct output from the function.
5. To do a test run you can run the check_images.py script using terminal and provide arguments with it OR provide no arguments and check if it picks the default args.

#### Detailed explanation can be found here ![LINK](https://classroom.udacity.com/nanodegrees/nd089/parts/cd0184/modules/172bc12e-2000-484d-8095-33899ed05418/lessons/7846dc05-3417-4e32-b0f2-afd7aa6fe0aa/concepts/74777926-d1bf-4a25-a77c-d7340c836467)


-----------------------------------------------------------------------------------------------------------------------
C. **TODO 2's can be found in get_pet_labels() file.**

1. You need to take in input as image_dir path and read the data from the directory to return dictionary with 'key' as image filename and 'value' as a List. The list contains for following item: index 0 = pet image label (string)
2. You can try checking the code by running check_creating_pet_image_labels function within check_images.py 

#### Detailed explanation is down below in here ![LINK](https://classroom.udacity.com/nanodegrees/nd089/parts/cd0184/modules/172bc12e-2000-484d-8095-33899ed05418/lessons/7846dc05-3417-4e32-b0f2-afd7aa6fe0aa/concepts/346cea04-36cb-4353-b1ea-27f084ef1b03)


### TO BE CONTINUED ...
