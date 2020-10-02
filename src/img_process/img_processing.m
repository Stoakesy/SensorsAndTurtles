
load('Calib_Results.mat', 'fc', 'cc', 'nx', 'ny');

intrinsics = cameraIntrinsics(fc', cc', [ny nx]);

tagSize = 0.128;

worldPoints = [0 0 0; tagSize/2 0 0; 0 tagSize/2 0; 0 0 tagSize/2];

posepub = rospublisher('/target_pose', 'geometry_msgs/Pose');

rosimg = rossubscriber('/camera/color/image_raw');

pause(2);

posemsg = rosmessage(posepub);

while(1)
    imgdata = receive(rosimg, 5);
    
    I = readImage(imgdata);

    I = undistortImage(I,intrinsics,"OutputView","same");

    [id,loc,pose] = readAprilTag(I,"tag36h11",intrinsics,tagSize);
    
    posemsg.Position.X = pose.Translation(1);
    posemsg.Position.Y = pose.Translation(2);
    posemsg.Position.Z = pose.Translation(3);
    quat = rotm2quat(pose.Rotation);
    posemsg.Orientation.W = quat(1);
    posemsg.Orientation.X = quat(2);
    posemsg.Orientation.Y = quat(3);
    posemsg.Orientation.Z = quat(4);
    
    send(posepub, posemsg);
    
    pause(0.5);

%     for i = 1:length(pose)
%         % Get image coordinates for axes.
%         imagePoints = worldToImage(intrinsics,pose(i).Rotation, ...
%                       pose(i).Translation,worldPoints);
% 
%         % Insert markers to indicate the locations
%         markerRadius = 8;
%         numCorners = size(loc,1);
%         markerPosition = [loc(:,:,i),repmat(markerRadius,numCorners,1)];
%         I = insertShape(I,"FilledCircle",markerPosition,"Color","red","Opacity",1);
% 
%         % Draw colored axes.
%         I = insertShape(I,"Line",[imagePoints(1,:) imagePoints(2,:); ...
%             imagePoints(1,:) imagePoints(3,:); imagePoints(1,:) imagePoints(4,:)], ...
%             "Color",["red","green","blue"],"LineWidth",7);
% 
%     %     I = insertText(I,loc(1,:,i),id(i),"BoxOpacity",1,"FontSize",25);
%     end
 end
