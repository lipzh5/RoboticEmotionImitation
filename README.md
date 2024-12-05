# Robotic Emotion Imitation
- **Summer Research Internship Project, School of Computing, Macquarie University.**
- **Advisor:** Prof. Longbing Cao, Distinguished Chair in AI
- **Supervisors:** Penny (Peizhen Li), Michael (Runze Yang)

## Stage 1: Dataset Collection (01.Dec.2024~14.Dec.2024)

### 1. Setup Environment
```commandline
git clone git@github.com:lipzh5/RoboticEmotionImitation.git
cd RoboticEmotionImitation
conda create -n emotionimitation python=3.9 -y
conda activate emotionimitation
# Optional, for cuda-12.1, feel free to install the appropriate version of PyTorch based on your CUDA version.
conda install pytorch==2.4.0 torchvision==0.19.0 torchaudio==2.4.0 pytorch-cuda=12.1 -c pytorch -c nvidia
pip install -r requirements.txt
```

### 2. Tasks
- 2.1 Extract frames from the video using the provided script (get_frames_from_vid.py). Feel free to modify it according 
      to your needs, and submit any issues on GitHub if you encounter any.
- 2.2 Generate new animation files using the [Animator tool](https://drive.google.com/file/d/1IDELUro-fQxjhQR1KcO4uETLxsm4JMBw/view?usp=drive_link).
      Instructions will be provided in person. Please bring your laptop and meet @Penny.
  - 📣 **Notices for Animation Filming:**
    1. Include the full cycle of the animation.
    2. Maintain the same image size as in the [example videos](assets/vid2frames/videos/Chat_G2_Angry_1_FaceOnly%20(1).mov).
        

- 2.3 **(Optional)** Check out the code from [LivePortrait](https://liveportrait.github.io/) and animate assets/images/ameca_neutral.jpeg using any driving videos.
      The animated videos should resemble [this](https://drive.google.com/file/d/1n7bLr458SKh1Z3u_NCWwTnCfJgngKW5L/view?usp=sharing).
      Then, extract frames from these animated videos.

## Stage 2: Real-World Deployment (06.Jan.2025~19.Jan.2025)
Coming soon!!!
