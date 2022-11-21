from gridmap import OccupancyGridMap
import cv2
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from utils import png_to_ogm





def canny(image):
    src = cv2.imread(image)
   
    gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    (k,thresh) = cv2.threshold(gray,250,255,cv2.THRESH_BINARY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    canny = cv2.Canny(gray, 125, 175)
    return thresh




# grid = OccupancyGridMap.from_png(r'C:\Users\Admin\OneDrive\Desktop\Capstone Project\bw_imgs\pod.png', 1)
# print (grid.get_data(0,0))
#ogm_data = png_to_ogm(r'C:\Users\Admin\OneDrive\Desktop\Capstone Project\bw_imgs\image.png', normalized=True)
#ogm_data_arr = np.array(ogm_data)

#mat = OccupancyGridMap(ogm_data_arr,5)
#print(mat.plot())

from gridmap import OccupancyGridMap
import matplotlib.pyplot as plt
from a_star import a_star
from utils import plot_path


if __name__ == '__main__':
    # load the map
    ans = canny(r'C:\Users\Admin\OneDrive\Desktop\Capstone Project\images\obs1.png')
    res = cv2.imwrite(r'C:\Users\Admin\OneDrive\Desktop\Capstone Project\bw_imgs\image.png',ans)
    gmap = OccupancyGridMap.from_png('bw_imgs\image.png', 0.01)
    #gmap.plot()
    start_node = (0.0,0.0)
    goal_node = (3.5,3.5)

    # run A*
    path, path_px = a_star(start_node, goal_node, gmap, movement='4N')

    gmap.plot()

    if path:
        # plot resulting path in pixels over the map
        print(path_px)
        plot_path(path_px)
        res = canny(r'C:\Users\Admin\OneDrive\Desktop\Capstone Project\image_plot.png')
        k = cv2.imwrite(r'C:\Users\Admin\OneDrive\Desktop\Capstone Project\canny_img.png',res)
        img1 = cv2.imread(r'C:\Users\Admin\OneDrive\Desktop\Capstone Project\canny_img.png')
        img2 = cv2.imread(r'C:\Users\Admin\OneDrive\Desktop\Capstone Project\bw_imgs\image.png')
        width1 = img1.shape[0]
        height1 = img1.shape[1]
        print((width,height))
        width2 = img2.shape[0]
        height2 = img2.shape[1]
        print((width2,height2))
        cropped_img = img2[0:0,img1.shape[1]:img1.shape[0]]
        or_ = cv2.bitwise_or(img1,cropped_img)
        cv2.imshow("Image ",or_)

        
    else:
        print('Goal is not reachable')

        # plot start and goal points over the map (in pixels)
        start_node_px = gmap.get_index_from_coordinates(start_node[0], start_node[1])
        goal_node_px = gmap.get_index_from_coordinates(goal_node[0], goal_node[1])

        plt.plot(start_node_px[0], start_node_px[1], 'ro')
        plt.plot(goal_node_px[0], goal_node_px[1], 'go')
    

    
    