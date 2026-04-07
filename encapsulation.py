class ScoreBoard:
  def __init__(self, score):
    self.__score = score

  def get_score(self):
    return self.__score
  
  def set_score(self, score):
    if score == 100:
      self.__score = 200
    else:
      self.__score = score    

s1 = ScoreBoard(100)    # private value storedd
print(s1.get_score())   # private value printed
score = s1.get_score()  # private value stored in variable
s1.set_score(score)     # private value changed
print(s1.get_score())   # updated value print


