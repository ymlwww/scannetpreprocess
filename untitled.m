ptCloud = pcread('scene0000_00_vh_clean_2.labels.ply');
colormatrix=ptCloud.Color;
locationmatrix=ptCloud.Location;
totalnum = ptCloud.Count;
newlocation=[];
for i=1:totalnum
    if(colormatrix(i,1) == 189 && colormatrix(i,2) == 198 && colormatrix(i,3) == 255)
        newlocation=[newlocation(1:end,:);locationmatrix(i,:)];
    end
end
floorcloud=pointCloud(newlocation);
pcshow(floorcloud);     
[model,inlierIndices,outlierIndices]  = pcfitplane(floorcloud,0.03);
floorplane = select(floorcloud,inlierIndices);
remainCloud = select(floorcloud,outlierIndices);
pcshow(floorplane);
disp(model);
%pcshow(ptCloud);
%disp(ptCloud);
%disp(unique(ptCloud.Color,'row'))
%  189,198,255 is floor
%  190,153,112 is wall

