%load the calibration data of the real sense camera
load('Calib_Results.mat', 'fc', 'cc', 'nx', 'ny');
%create the camera intrinsicts values from calibration data
intrinsics = cameraIntrinsics(fc', cc', [ny nx]);

makerSize = 0.128; %size of marker in m

worldPoints = [0 0 0; makerSize/2 0 0; 0 makerSize/2 0; 0 0 makerSize/2];
%create ros publisher for pose of front robot
posePub = rospublisher('/target_pose', 'geometry_msgs/Pose');
%create ros publisher for camera on tb
rosImg = rossubscriber('/camera/color/image_raw');

pause(2); %allow for connectionof publisher and subscriber
%enable ros message
poseMsg = rosmessage(posePub);

check = 0;

while (1)
    %recieve incoming ros message of camera image
    imgData = receive(rosImg, 5);
    tic
    %convert from ros image format to Matlab image format
    img = readImage(imgData);
    imgRead = toc;
    %apply camera intrinsics data to image
    img = undistortImage(img,intrinsics,"OutputView","same");
    imgProcessed = toc;
    %read the image to find april tag
    [id,loc,pose] = readAprilTag(img,"tag36h11",intrinsics,makerSize);
    tagFound = toc;
    
    %if no data send 0,0,0 as pose
    if (isempty(pose))
        check = check + 1;
        if (check >= 3)
            check = 0;
            %populate ros message
            poseMsg.Position.X = 0;
            poseMsg.Position.Y = 0;
            poseMsg.Position.Z = 0;

            poseMsg.Orientation.W = 0;
            poseMsg.Orientation.X = 0;
            poseMsg.Orientation.Y = 0;
            poseMsg.Orientation.Z = 0;
        end
    else
        %populate ros message
        poseMsg.Position.X = pose.Translation(1);
        poseMsg.Position.Y = pose.Translation(2);
        poseMsg.Position.Z = pose.Translation(3);
        quat = rotm2quat(pose.Rotation);
        poseMsg.Orientation.W = quat(1);
        poseMsg.Orientation.X = quat(2);
        poseMsg.Orientation.Y = quat(3);
        poseMsg.Orientation.Z = quat(4);
    end
        
    %publish ros message
    send(posePub, poseMsg);
    msgSent = toc;
    
    pause(0.01);
    pauseDone = toc;
    
    hi=1;
    
 end
