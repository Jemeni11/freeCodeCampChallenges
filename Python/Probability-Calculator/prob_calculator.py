import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs) -> None:
        self.contents = [key for key,value in kwargs.items() for i in range(value)]

    def draw(self, number_of_balls) -> list:
        if number_of_balls > len(self.contents):
            return self.contents
        else:
            balls_picked = list()
            for i in range(number_of_balls):
                picked = random.choice(self.contents)
                balls_picked.append(picked)
                self.contents.remove(picked)
            return balls_picked


def experiment(hat, expected_balls, num_balls_drawn, num_experiments) -> float:
    
    count = 0

    for i in range(0, num_experiments):
        bag = copy.deepcopy(hat)
        ball_choice = bag.draw(num_balls_drawn)
        final_count = 0           
        
        for i in expected_balls.keys():
            if ball_choice.count(i)>= expected_balls[i]:
                final_count += 1 
        if final_count == len(expected_balls):
            count += 1
        
    return count/num_experiments

