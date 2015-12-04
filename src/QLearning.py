from State import State
from Cheesboard import ChessBoard
from random import randint
import ramdom

class QLearning:
	
    def __init__(self,params):
        self.params = params
        self.gamma = 0.5
        self.all_params = self.params.get_all_params()
        self.R = self.params.get_possible_nxt_prms()

    def learning(self, epochs):
    	while epochs > 0:
	    	rnd_num = randint(0,len(self.all_params))
	    	current_state_id = self.all_params[rnd_num]
	    	current_state = self.R[current_state_id]
	    	rnd_action_id = random.choice(current_state.keys())
	    	rnd_action = current_state[rnd_action_id]
	    	if selct_rnd_action[1] != -2:
	    		self.cal_learning_step(current_state_id, rnd_action_id)
	    	epochs -= 1	


    def cal_learning_step(self, state, action):
    	mx = 0
    	for reward, q in self.R[action]:
    		if reward > mx:
    			mx = reward

    	r = self.R[state][action][0]
		self.R[state][action] = (r, mx*self.gamma)
        
if __name__ == '__main__':

    q = QLearning()

    board = ChessBoard.get_random_chessboard()
