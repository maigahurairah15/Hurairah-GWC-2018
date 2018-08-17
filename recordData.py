import state_crime
list_of_report = state_crime.get_all_crimes()

print(list_of_report[0])

for i in list_of_report:
    print(i["Data"]["Rates"]["Violent"]["Robbery"])
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

states = ('New York', 'Virginia', 'Washington', 'Vermont', 'Utah', 'Texas')
y_pos = np.arange(len(states))
performance = [10,8,6,4,2,1]

plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, states)
plt.ylabel(number of )
plt.title('Programming language usage')
