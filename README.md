# About this Project

Danio rerio, also known as the zebrafish, is a common model organism for its clear larval stage, high fecundity, and rich library of available mutants. While working with zebrafish for my master's project, I found conventional behavioral analysis tools lacking. To address this issue, I began writing simple scripts that interpret raw XY-coordinate output from excellent, open-source animal tracking projects such as IdTrackerAI and DeepLabCut. As my labmates and I learned more about Python programming, our modules became more ambitious. Though still in its infancy, we hope OpenDanio inspires you to contribute to our project, incorporate our tools, and take full control of your own data processing workflow!

It's your data. You should decide what the computer does with it.

# Prerequisites

Open Danio gives researchers a way to interpret the framewise XY corrdinates generated from animal tracking tools. Therefore, users have to provide their own animals, video files, and tracking output data. As previously stated, we recommend using either DeepLabCut or IdTrackerAI, depending on your available hardware and research requirements. For example, DeepLabCut is excellent at pose estimation, but in our experience, requires a strong GPU and a lot of time to train. Moreover, DeepLabCut has been better for our single-animal tracking experiments, whereas IdTrackerAI is great for simultaneous multi-animal tracking in the same region of interest. This is because IdTrackerAI was specifically designed to keep track of animal identity in a group, which becomes a non-trivial challenge when you record multiple crossing zebrafish from a top-down angle.
Getting Started

Download this repository by going up to the green "Code" button at the top right and clicking "Download ZIP".


## 2D_trajectory.py

Open-source tracking solutions didn't have readily-available trajectory image generators when I was doing my masters, so I made my own. Whatever tracking solution you use should spit out a video frame-wise XY coordinate table, which 2D_trajectory.py converts into a linear path the object (zebrafish) moved (swam). The input file assumes only two columns, with the first column representing X position and the second column representing Y position (often in pixel units). It's rudimentary, and perhaps my colleague Connor and I will fancy it up later. For now, I hope this script gives you ideas for writing your own trajectory mappper.

## novel_tank_dive.py

The Novel Tank Dive (NTD) is a standard zebrafish anxiety experiment. Ideally, the zebrafish spends more time at the bottom of a tank when first introduced and then gradually builds up the courage to poke around at the top as it begins to feel safe. Fish experiencing higher therefore spend more time on the bottom and venture upwards at a slower rate than "normal" fish. The novel_tank_dive.py script takes an XY output from a single-fish NTD video recorded side-on such that the Y value reflects fish depth in the tank. My thesis experiements considered a 5-minutes test duration, so I chopped up each video into five 1-minute segments based on the recording frame rate used at the time of filming. Feel free to adapt the base script to your own needs.

## shoal_analysis.py

I also worked a lot with zebrafish larvae. 5 days after fertilization, zebrafish have hatched from their egg and are capable of twitchy swim bursts when agitated. 5-day-old zebrafish also display shoaling --- the tendency to swim in close proximity to one another. The shoal_analysis.py script takes a 2-column table of paired data containing the X pixel position in the first column and Y pixel position in the second column. This data is obtained from static images of petri dishes housing larval zebrafish. The images were processed using ImageJ to make an XY coordinate list of each fish. While the image processing step is time-consuming and could be automated, I chose to do it the slow but reliable way. Still, this script saves time by automating the calculation of inter-fish distance for each individual with respect to every other individual present. Then, the arithmetic mean of all the unique inter-fish euclidean distances is calculated to generate a single "shoal cohesion" value.
