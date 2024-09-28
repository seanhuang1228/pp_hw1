import matplotlib.pyplot as plt

main_time = [3327, 1893, 1372, 701]
total_time = [5030, 3535, 3290, 2397]
core = [1, 2, 4, 8]

fig = plt.figure()
plt.title("Used time with different number of cores")
plt.plot(core, main_time, color='blue', marker='o', label='main time')
plt.plot(core, total_time, color='red', marker='o', label='total time')
plt.legend(loc='upper right')
plt.xlabel("core count")
plt.ylabel("used time (ms)")

for pt in zip(core, main_time):
    plt.annotate(f"{pt[1]}", xy=pt, xytext=(0, 10), textcoords='offset points')

for pt in zip(core, total_time):
    plt.annotate(f"{pt[1]}", xy=pt, xytext=(0, 10), textcoords='offset points')

plt.xlim(0.5, 9)
plt.ylim(0, 5500)

plt.savefig("asset/statistic.png")
