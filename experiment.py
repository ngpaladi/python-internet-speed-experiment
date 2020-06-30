import matplotlib.pyplot as plt
import numpy as np


# Define function of approximate time (in hours)
# it takes to drive to someone a certain distance
# (in miles) away

def time_to_drive(distance):
    # If total distance is less than 10 miles, you average 30 mph
    if(distance <= 10):
        return distance/30
    # For distances less than 40 miles, you average 50 mph for the middle miles
    elif (distance <= 40):
        return (10)/30 + (distance-10)/50
    # For greater distances, we hit the interstate at 70 mph
    else:
        return (10)/30 + (40-10)/50 + (distance-40)/70


INTERNET_DOWNLOAD_SPEED = 140 # Mb/s
INTERNET_UPLOAD_SPEED = 50 # Mb/s

# Convert to GB/hr
INTERNET_DOWNLOAD_SPEED = INTERNET_DOWNLOAD_SPEED/8/1000*60*60
INTERNET_UPLOAD_SPEED = INTERNET_UPLOAD_SPEED/8/1000*60*60

N=5000
x = np.linspace(0., N, N)
y = np.zeros(N)

filesizes = [10,25, 50, 1000] #GB
filesize_lines = []

for i in range(len(filesizes)):
    filesize_lines.append(np.zeros(N))

for i in range(N):
    y[i] = time_to_drive(x[i])

    for j in range(len(filesizes)):
        filesize_lines[j][i] = filesizes[j]/INTERNET_UPLOAD_SPEED + filesizes[j]/INTERNET_DOWNLOAD_SPEED

plt.plot(x,y, color="blue", label="Time To Drive")
plt.plot(x,filesize_lines[3], color="red", label="100 GB File Transfer")
plt.plot(x,filesize_lines[2], color="purple", label="50 GB File Transfer")
plt.plot(x,filesize_lines[1], color="orange", label="25 GB File Transfer")
plt.plot(x,filesize_lines[0], color="green", label="10 GB File transfer")
plt.legend()
plt.xlabel("Distance (mi)")
plt.ylabel("Time (hr)")
plt.title("Data Transfer Times")
plt.tight_layout()
plt.show()