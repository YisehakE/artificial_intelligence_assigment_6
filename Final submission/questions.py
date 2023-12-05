


'''
  ## retrieve_feature_choices_and_index_map

  Need to do:
    * Consider combine these maps and storing value as a tuple, where 1st value would be set of choices and 2nd value would be the index mapping


  Questions
    Q: Can we assume that the indices of attribute names wilh match the placement of values in dataset?
    A: 

'''

'''
## retrieve_majority_label

  Need to do:
    * Consider using get_mode()
  Question:
    Q:
    A:
'''


'''
## retrive_best_feature
  Need to do:
    * Need to have a feature index map since features_left will shrink each time, not representing the correct column index for feature attribute in data
    * Need to consider retrieve max info gain along with best feat and associated choice entropy map in same for loop
'''



'''
  ## Train  

  Need to do:
    * How to translate id3 pseudocode to conform to nested dictionary structure
        => I think I figured this out

    * Consider the depth limit into the id3 recursive function
        => I will integrate this once I find that the current solution works

    * Tweak code to account for supervised classification data that contain
      more than 2 type of target values...
        => Fix retrieve_target_sizes ()
        => Fix get_target_answers_and_types ()
        => Fix entropy_hx ()
        => Fix retrieve_majority_label ()

    Questions:
      Q: What happens if training data is empty? D
      A:

      Q: Do I account for supervised classification data that contain
      more than 2 type of target values...
      A:

'''

