import numpy as np
import random

# Define the environment (Maze)
class MazeEnvironment:
    def __init__(self):
        # 0: Empty cell, 1: Wall, 2: Start, 3: Goal
        self.maze = np.array([[0, 1, 0, 0, 0],
                              [0, 1, 0, 1, 0],
                              [0, 0, 0, 1, 0],
                              [1, 1, 0, 0, 0],
                              [0, 0, 0, 1, 3]])
        self.start_pos = (0, 0)  # Start position
        self.agent_pos = self.start_pos  # Agent starts here
    
    def reset(self):
        self.agent_pos = self.start_pos  # Reset agent to start
        return self.agent_pos
    
    def get_state(self):
        return self.agent_pos
    
    def step(self, action):
        row, col = self.agent_pos
        
        # Define movement actions: [Up, Down, Left, Right]
        if action == 0:  # Up
            next_pos = (row - 1, col)
        elif action == 1:  # Down
            next_pos = (row + 1, col)
        elif action == 2:  # Left
            next_pos = (row, col - 1)
        elif action == 3:  # Right
            next_pos = (row, col + 1)
        
        # Check boundaries and walls
        if next_pos[0] < 0 or next_pos[0] >= self.maze.shape[0] or next_pos[1] < 0 or next_pos[1] >= self.maze.shape[1] or self.maze[next_pos] == 1:
            next_pos = self.agent_pos  # Invalid move, stay in place

        self.agent_pos = next_pos
        
        # Check if the agent reached the goal
        if self.maze[self.agent_pos] == 3:
            return self.agent_pos, 10, True  # Goal reached, reward 10, done
        else:
            return self.agent_pos, -1, False  # Penalty for each move

# Define the Q-Learning agent
class QLearningAgent:
    def __init__(self, env, learning_rate=0.1, discount_factor=0.9, exploration_rate=1.0, exploration_decay=0.99):
        self.env = env
        self.q_table = np.zeros((env.maze.shape[0], env.maze.shape[1], 4))  # Q-table with 4 possible actions (Up, Down, Left, Right)
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.exploration_rate = exploration_rate
        self.exploration_decay = exploration_decay
    
    def choose_action(self, state):
        # Epsilon-greedy strategy for exploration
        if random.uniform(0, 1) < self.exploration_rate:
            return random.randint(0, 3)  # Explore: choose random action
        else:
            row, col = state
            return np.argmax(self.q_table[row, col])  # Exploit: choose best action from Q-table
    
    def learn(self, state, action, reward, next_state):
        row, col = state
        next_row, next_col = next_state
        best_next_action = np.argmax(self.q_table[next_row, next_col])
        
        # Q-learning update rule
        self.q_table[row, col, action] = self.q_table[row, col, action] + self.learning_rate * (
            reward + self.discount_factor * self.q_table[next_row, next_col, best_next_action] - self.q_table[row, col, action]
        )
    
    def train(self, episodes):
        for episode in range(episodes):
            state = self.env.reset()  # Reset environment for each episode
            done = False
            total_reward = 0
            
            while not done:
                action = self.choose_action(state)  # Choose an action
                next_state, reward, done = self.env.step(action)  # Take action, observe reward and next state
                self.learn(state, action, reward, next_state)  # Update Q-table
                state = next_state  # Move to next state
                total_reward += reward
            
            # Decay exploration rate
            self.exploration_rate *= self.exploration_decay
            
            # Print progress
            print(f"Episode {episode + 1}: Total Reward = {total_reward}")
        
        print("Training complete!")

# Main function
if __name__ == "__main__":
    env = MazeEnvironment()  # Create the maze environment
    agent = QLearningAgent(env)  # Create the Q-learning agent
    agent.train(episodes=100)  # Train the agent for 100 episodes
    
    # Test the learned policy
    state = env.reset()
    done = False
    print("\nAgent's path:")
    while not done:
        action = np.argmax(agent.q_table[state[0], state[1]])  # Choose best action from Q-table
        next_state, reward, done = env.step(action)
        print(state, " -> ", next_state)
        state = next_state
