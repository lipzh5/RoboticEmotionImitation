# -*- coding:utf-8 -*-
# @Author: Peizhen Li
# @Desc: extract frames from facial expression animation
import cv2
import os
import os.path as osp

cwd = os.getcwd()
VIDEO_ROOT = 'assets/vid2frames/videos'
RAW_FRAMES_DIR = 'assets/vid2frames/frames'
CROPPED_FRAMES_DIR = 'assets/vid2frames/cropped_frames'
HEIGHT_MARGIN = 55
WIDTH_MARGIN = 70


def vid2frames(video_path='assets/vid2frames/videos/Chat_G2_Angry_1_FaceOnly (1).mov'):
	# Create a folder to save the frames if it doesn't exist

	vid_name = video_path.split('/')[-1].split('.')[0]
	output_folder = osp.join(RAW_FRAMES_DIR, vid_name)
	if not osp.exists(output_folder):
		os.makedirs(output_folder)

	# Open the video file
	cap = cv2.VideoCapture(video_path)
	# fps = cap.get(cv2.CAP_PROP_FPS)   ~60
	total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

	# Check if the video opened successfully
	if not cap.isOpened():
		print("Error: Could not open video.")
		exit()

	frame_rate = 60  # Frames per second (fps) of the video
	skip_frames = 3  # Number of frames to skip  # reduce to 20 fps

	frame_count = 0
	extracted_count = 0

	while True:
		# Read a frame from the video
		ret, frame = cap.read()
		if not ret:
			break  # No more frames to read

		# Save only every 'skip_frames' frames
		if frame_count and frame_count % skip_frames == 0 or frame_count == (total_frames - 1) or frame_count == 1:
			frame_filename = osp.join(output_folder, f"frame_{extracted_count:04d}.jpg")
			cv2.imwrite(frame_filename, frame)
			extracted_count += 1

		frame_count += 1

	# Release the video capture object
	cap.release()

	print(f"Extracted {extracted_count} frames.")


# print(f"Extracted {frame_count} frames based on the original FPS of {fps}.")


def crop_frames(vid_name):
	"""crop frames for one project"""
	frames_dir = osp.join(RAW_FRAMES_DIR, vid_name)
	print(f'vid name: {vid_name}, frames dir: {frames_dir}')
	output_folder = osp.join(CROPPED_FRAMES_DIR, vid_name)
	if not os.path.exists(output_folder):
		os.makedirs(output_folder)
	for root, dirnames, filenames in os.walk(frames_dir):
		for filename in filenames:
			image = cv2.imread(osp.join(root, filename))
			h, w, c = image.shape  # (216, 228, 3)
			cropped_image = image[0:h - HEIGHT_MARGIN, 0:w - WIDTH_MARGIN]
			cv2.imwrite(osp.join(output_folder, filename), cropped_image)


def batch_vid2frames():
	"""extract frames from video and then crop them to approapriate size"""
	for root, dirnames, filenames in os.walk(VIDEO_ROOT):
		print(f'root: {root}, dirnames: {dirnames}, filenames: {len(filenames)}')
		for filename in filenames:
			vid_path = osp.join(root, filename)
			vid2frames(vid_path)
			crop_frames(vid_name=filename.split('.')[0])


if __name__ == "__main__":
	batch_vid2frames()
# vid2frames()
# crop_frames()




