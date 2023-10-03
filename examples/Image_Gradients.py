
import cv2 as cv

def gradients(image: str):
    assert image is not None, "file could not be read, check with os.path.exists()"
    img = cv.imread(image)
    laplacianMatLike = cv.Laplacian(img, cv.CV_64F, ksize=25)
    sobelxMatLike = cv.Sobel(img,cv.CV_64F,1,0,ksize=25)
    sobelyMatLike = cv.Sobel(img,cv.CV_64F,0,1,ksize=25)

    name, ext =  image.split('.')
    output_laplacian = name + '_laplacian.' + ext
    output_sobelx = name + '_sobelx.' + ext
    output_sobely = name + '_sobely.' + ext
    

    cv.imwrite(output_laplacian, laplacianMatLike)
    cv.imwrite(output_sobelx, sobelxMatLike)
    cv.imwrite(output_sobely, sobelyMatLike)

    print(
        '\tThe following new files was created:\n',
        '\t\t + ' + output_laplacian + '\n',
        '\t\t + ' + output_sobelx + '\n',
        '\t\t + ' + output_sobely  + '\n')


if __name__ == '__main__':
    gradients('../data/images/sample.png')
