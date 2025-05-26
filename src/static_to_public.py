import os
import shutil


    #pub_exists = os.path.exists("public")  #Determine if public exists already
    #print("Public Exists:", pub_exists)

    #join_ex = os.path.join(current_filepath, dir_list[1])
def static_to_public(static, public):
    if os.path.exists(public):
        ###if delete == 'yes':
        shutil.rmtree(public)
        ###if delete != "no" and delete != "yes":
            ###raise Exception("Delete public directory? Third argument must be yes or no, argument defaults to no.")
    if os.path.exists(public) != True:
        os.mkdir(public) ###commented out unnecessary complexity
    
    def copy_static_to_public(static, public):
        #For directories, call recurisvely
        #For files, do not
        if os.path.isfile(static):
            shutil.copy(static, public)
        elif os.path.isdir(static):
            if os.path.exists(static):
                os.makedirs(public, exist_ok=True)  #can substitute for os.mkdir(public_item) in loop, is generally preferred method
                for item in os.listdir(static):
                    static_item = os.path.join(static, item)#static + '/' + item
                    public_item = os.path.join(public, item)#public + '/' + item
                    #if os.path.isdir(static_item) and os.path.exists(public_item) != True: 
                        #os.mkdir(public_item)
                    copy_static_to_public(static_item, public_item)
        return
    return copy_static_to_public(static, public)

    
    
                  
static_to_public("static", "public")

"""filepath_storage = os.listdir(parent_directory)
    

    for directories in parent_directory:
        filepath = current_filepath + '/' + directories
    
    if parent_directory[directories] is None:  #Base case, break the recursion loop         
            filepath_storage.append(filepath)      # add filepath to filepath storage list
    else:
          
        filepath_storage.extend(static_to_public(parent_directory[directories], filepath))

    return filepath_storage   
"""