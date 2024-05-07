import matplotlib.pyplot as plt
import numpy as np
import csv

d = np.loadtxt('/content/report.csv', delimiter=',', dtype=str)

print (d)
print (d.dtype)

time = d[1:, 0]
steering_wheel = d[1:, 1].astype(int)
break_value = d[1:, 2].astype(int)
activating_signal = d[1:, 3].astype(int)

## 시간에 따른 Steering Wheel, Break 변화값
fig, ax1 = plt.subplots(figsize=(10, 5))

ax1.set_xlabel('Time')

# Plot the 'Steering Wheel' data on the primary y-axis
ax1.plot(time, steering_wheel, label='Steering Wheel', color='b')
ax1.set_ylabel('Steering Wheel', color='b')
ax1.tick_params(axis='y', labelcolor='b')

# Create a secondary y-axis
ax2 = ax1.twinx()

# Plot the 'Break' data on the secondary y-axis
ax2.plot(time, break_value, label='Break', color='r')
ax2.set_ylabel('Break', color='r')
ax2.tick_params(axis='y', labelcolor='r')


# Add a legend
lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax2.legend(lines + lines2, labels + labels2, loc='upper left')

# Rotate x-axis labels for better readability
# plt.xticks(rotation=45)
plt.tick_params(bottom = False)

# Show the plot
plt.title('Steering Wheel and Break values over Time')
plt.tight_layout()
plt.show()

## Signal에 따른 Steering Wheel 변화값
fig, ax1 = plt.subplots(figsize=(10, 5))

ax1.set_xlabel('Time')

# Plot the 'Steering Wheel' data on the primary y-axis
ax1.plot(time, steering_wheel, label='Steering Wheel', color='b')
ax1.set_ylabel('Steering Wheel', color='b')
ax1.tick_params(axis='y', labelcolor='b')

# Create a secondary y-axis
ax2 = ax1.twinx()

# Plot the 'Break' data on the secondary y-axis
ax2.plot(time, activating_signal, label='Activating Signal', color='r')
ax2.set_ylabel('Activating Signal', color='r')
ax2.tick_params(axis='y', labelcolor='r')


# Add a legend
lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax2.legend(lines + lines2, labels + labels2, loc='upper left')

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Show the plot
plt.title('Steering Wheel value according to the Signal change')
plt.tight_layout()
plt.show()

## Signal에 따른 Break 변화값
fig, ax1 = plt.subplots(figsize=(10, 5))

ax1.set_xlabel('Time')

# Plot the 'Steering Wheel' data on the primary y-axis
ax1.plot(time, break_value, label='Break', color='b')
ax1.set_ylabel('Break', color='b')
ax1.tick_params(axis='y', labelcolor='b')

# Create a secondary y-axis
ax2 = ax1.twinx()

# Plot the 'Break' data on the secondary y-axis
ax2.plot(time, activating_signal, label='Activating Signal', color='r')
ax2.set_ylabel('Activating Signal', color='r')
ax2.tick_params(axis='y', labelcolor='r')


# Add a legend
lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax2.legend(lines + lines2, labels + labels2, loc='upper left')

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Show the plot
plt.title('Break value according to the Signal change')
plt.tight_layout()
plt.show()

