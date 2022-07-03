class Incubator: 
    def get_all_embryo_ids(self): 
        """ 
        :return: returns a list of embryo_ids 
        """ 
        pass 
 
    def get_image(self, requested_embryo_id, requested_image_index): 
        """ 
        returns the image of the reqeusted index for an embryo 
        if the requested index does not exist, the value of image will  
        be None/Null 
        in addition, also returns if the embryo video has been completed 
        (boolean value) 
        :param requested_embryo_id: embryo_id to get the image of 
        :param requested_image_index: index of the requested image 
        :return: tuple(image -> bytes, completed -> boolean) 
        """ 
        pass 
 
    def get_all_images(self, requested_embryo_id): 
        """ 
        returns a list of all the images for a requested embryo 
        when requesting a large amount of images (50+) - 
            this method is much more efficient than using "get_image" method  
            or the same amount of images   
        :param requested_embryo_id: embryo_id to get the images of 
        :return: tuple(images -> list[bytes, bytes, bytes..], completed ->  
        boolean) 
        """ 
        pass 
 
class VideoBuilder: 
    def append_images(self, embryo_video, images_list): 
        """ 
        appends the images in images_list to an existing video file 
        :param embryo_video: embryo video file to append the images to 
        :param images_list: the images that need to be appended 
        :return: void 
        """ 
        pass 
 
 
# start script 
inc = Incubator() 
vid_builder = VideoBuilder() 
 
embryo_stats = dict() 
while True: 
   # start iteration 
   for embryo_id in inc.get_all_embryo_ids(): 
 
        if embryo_id not in embryo_stats.keys(): 
            # never-seen-before embryo; start getting images from image 0 
         
            embryo_stats[embryo_id] = dict() 
            request_index = 0 
            image,completed = inc.get_image(embryo_id, request_index) 
 
            while image is not None: 
                embryo_stats[embryo_id]['last_request_time'] = datetime.now() 
                embryo_stats[embryo_id]['last_index'] = request_index 
                embryo_stats[embryo_id]['completed'] = completed 
                vid_builder.append_images(embryo_id, [image]) 
                request_index+=1 
                image,completed = inc.get_image(embryo_id, request_index) 
 
        elif embryo_stats[embryo_id]['completed']: 
            # embryo is already completed - pass 
            pass 
 
        elif not embryo_stats[embryo_id]['completed']: 
            # embryo is in progress, and may have new images since last fetch 
            request_index = embryo_stats[embryo_id]['last_index'] + 1 
 
            image,completed = inc.get_image(embryo_id, request_index) 
 
            while image is not None: 
                embryo_stats[embryo_id]['last_request_time'] = datetime.now() 
                embryo_stats[embryo_id]['last_index'] = request_index 
                embryo_stats[embryo_id]['completed'] = completed 
                vid_builder.append_image(embryo_id, [image]) 
 
                request_index+=1 
                image,completed = inc.get_image(embryo_id, request_index) 
    # finish iteration 
 
# end script 