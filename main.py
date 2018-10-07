import gym

env = gym.make("CartPole-v0") # create the environment for cartpole sim

def basic_policy(obs): # policy determines the actions for the agent to take based
    angle = obs[2] # on the observations it makes of the environment
    return 0 if angle < 0 else 1

    # our policy determines the direction in which we move to balance the pole
    # our cart can only take two actions, it can either move left or right along the x axis

totals = [] # list of the total reward accumulated for each run

for trial in range(1000):
    trial_rewards = 0 # the rewards for the trial in this case for keeping the pole balanced or running as long as possible
    obs = env.reset() # initial observation, carts horizontal position (0.0 for center), returns observations in current frame state
    action = 1 # move the cart left or right
    for step in range(1000): # we want to keep balance for 1000 timesteps
        action = basic_policy(obs) # perform ana ction based on the policy and observed env
        env.render()
        obs, reward, done, info = env.step(action) # update the observations and reward with the action
        trial_rewards += reward # add the reward at the current time step, 1 in this case
        if done:
            totals.append(trial_rewards)
            break

print(totals)
print("Record timesteps pole balanced: " + str(max(totals)))
