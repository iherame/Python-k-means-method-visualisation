import PIL as pl
from random import randint
from math import dist

MAX_ITER = 10


def get_mean_of_cluster(cluster):
    sum_x = sum(p[0] for p in cluster)
    sum_y = sum(p[1] for p in cluster)
    return (int(sum_x / len(cluster)), int(sum_y / len(cluster)))

COLORS = [
    (255, 0, 0),
    (0, 255, 0),      
    (0, 0, 255),      
    (255, 255, 0),    
    (0, 255, 255),    
    (255, 0, 255),   
    (255, 165, 0),    
    (255, 192, 203),  
    (128, 0, 128),    
    (64, 224, 208)     
]

def get_means(count_of_clusters, w, h):
    yield from ((randint(0, w), randint(0, h)) for _ in range(count_of_clusters))

def black_or_white(power):
    rand_num = randint(0, 110)
    if power > rand_num:
        return True


def get_image(w, h, power):
    counter = 0
    pixels = []
    img = pl.Image.new("RGB", (w, h), "white")
    for i in range(0, h):
        for j in range(0, w):
            if black_or_white(power):
                counter += 1
                img.putpixel((j, i), (0,0,0))
                pixels.append((j, i))
    img.save("1.png")


    return counter, pixels

def k_means_method(count_of_clusters, w, h, pixels):
    iteration = 0
    means = list(get_means(count_of_clusters, w, h))
    while True:
        if iteration == MAX_ITER:
            break
        
        clusters = [[] for _ in means]

        for pixel in pixels:
            dist_list = [dist(pixel,mean) for mean in means]
            min_ind = dist_list.index(min(dist_list))
            clusters[min_ind].append(pixel)

        new_means = [get_mean_of_cluster(cluster) for cluster in clusters]
        if means == new_means:
            break

        means = new_means
        iteration += 1

    img = pl.Image.new("RGB", (w, h), "white")
    for i in range(len(clusters)):
        for pixel in clusters[i]:
            img.putpixel(pixel, COLORS[i])
    img.save("2.png")

